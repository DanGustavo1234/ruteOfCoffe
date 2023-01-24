import React from 'react'
import { useEffect, useState } from 'react' 



export function Emprendimiento() {

    const [data,setData]= useState([]);
    
    useEffect(()=>{
        fetch("http://127.0.0.1:8000/api/emprendimiento/")
        .then((response)=> response.json())
        // .then((data)=> console.log(data));
        .then((data)=> setData(data))
    })

  return (
    <div>
        [
            {
                data.map(
                (item) => (
                <div key={item.id}>
                <h2>{item.nombre_emprendimiento}</h2>
                <p>{item.descripcion}</p>
                </div>
                )
                
                )
            }
        ]
    </div>
  )
}



