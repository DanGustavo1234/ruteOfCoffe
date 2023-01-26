import React from 'react'
import { useEffect, useState } from 'react' 
import './Emprendimiento.scss'
import 'bootstrap/dist/css/bootstrap.min.css'
import { NavLink} from "react-router-dom";



export function Emprendimiento() {

    const [data, setData] = useState([]);

    useEffect(() => {
      fetch("http://127.0.0.1:8000/api/emprendimiento/")
        .then((response) => response.json())
        // .then((data)=> console.log(data));
        .then((data) => setData(data));
    });
    return (
      <div className="container">
   
   <div className="card-group" >
        
        {data.map((item) => (
          <div className="col-md-3">  
          <div className="card text-center" key={item.id}>
          
            <div className="card-body body">
              <img
                src={`${item.foto}`}
                ul={false}
                className="img_enprendimiento"
              ></img>

              <NavLink to="/" aria-current="page"><button class="button-38" role="button">{item.nombre_emprendimiento}</button></NavLink>
              

            <div className='row'>

            <ul className='iconos_rs'>
            <NavLink to="/" aria-current="page"><ion-icon name="logo-facebook"></ion-icon></NavLink>
            <NavLink to="/" aria-current="page"><ion-icon name="logo-instagram"></ion-icon></NavLink>
            <NavLink to="/" aria-current="page"><ion-icon name="logo-twitter"></ion-icon></NavLink>
            <NavLink to="/" aria-current="page"><ion-icon name="logo-tiktok"></ion-icon></NavLink>
          
            </ul>
          

            </div>
          
           
             
            </div>
            
           
  
          </div> 
          </div>
          
          

        ))}
        </div>
      </div>
  
     
      
    );
}



