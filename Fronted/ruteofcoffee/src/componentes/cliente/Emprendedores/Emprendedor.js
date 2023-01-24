import React from 'react'
import { useEffect, useState } from 'react' 


export  function Emprendedor() {
    const [data,setData]= useState([]);
    
    useEffect(()=>{
        fetch("http://localhost:8000/api/emprendedor/")
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
                <h2>{item.nombre}</h2>
                <p>{item.apellido}</p>
                </div>
                )
                
                )
            }
        ]
    </div>
  )
}
