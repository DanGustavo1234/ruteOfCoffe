import React from "react";
import { useEffect, useState } from "react";
import './Categorias.scss'
import { NavLink,Link } from "react-router-dom";


export function Categorias() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/categoria/")
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
        <NavLink to="/" className="active" aria-current="page"> 
            <img
              src={`${item.foto}`}
              ul={false}
              className="img_categoria"
            ></img>
        </NavLink>
            <button class="button-38" role="button">{item.nombre}</button>  
          </div>
        </div> 
        </div>
        
    
    
       
      ))}
      </div>
    </div>

   
    
  );
}
