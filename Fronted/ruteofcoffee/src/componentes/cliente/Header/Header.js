import React from 'react'

import { NavLink,Link } from "react-router-dom";
import "./Header.scss"
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import {faBarsStaggered} from '@fortawesome/free-solid-svg-icons'
import 'bootstrap/dist/css/bootstrap.min.css'
import { Dropdown,DropdownItem,DropdownMenu,DropdownToggle } from "reactstrap";
import { useState } from "react";
import imgsincolor from '../../../assets/img/imgsincolor.png'

export  function Header() {
  const[ dropdown,setDropdown]=useState(false);

    const abrirCerrarDropdown=()=>{
        setDropdown(!dropdown);
    }
  return (
    <div>
    
    
    
  
      
        <section>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>


        <nav class="menu">
        <Link class="logo" to="/"><img src={imgsincolor} className="imagen" /></Link>
              <ul class="menu_items">
                <li class="active">
                <NavLink to="/" className="active" aria-current="page">Home</NavLink>
                </li>
                <li class="active">
                <NavLink to="/emprendimientos" className="active" aria-current="page">Emprendimientos</NavLink>
               </li>
               <li class="active">
               <NavLink to="/emprendedores" className="active" aria-current="page">Emprendedores</NavLink>
               </li>
               <li class="active">
               <NavLink to="/" className="active" aria-current="page">Login</NavLink>
               </li>
               {/* <li class="active">
               <NavLink to="/Salasdelectura" className="active" aria-current="page">Salas de lectura</NavLink>
               </li>
               <li class="active">
               <NavLink to="/LoginAdmin" className="active" aria-current="page">Login</NavLink>
               </li> */}
              </ul>
            
            <span class="btn_menu">
            <Dropdown isOpen={dropdown} toggle={abrirCerrarDropdown}>
            <DropdownToggle  class="boton">
            <span class="boton">
            <FontAwesomeIcon  icon={faBarsStaggered} /> 
            </span>
            </DropdownToggle>
            <DropdownMenu>
            <ul class="items">

         
                <DropdownItem> <li class="active">
                <NavLink to="/" className="active" aria-current="page">Home</NavLink>
                </li></DropdownItem>
                <DropdownItem>  <li class="active">
                <NavLink to="/" className="active" aria-current="page">Laboratorios</NavLink>
               </li></DropdownItem>
                <DropdownItem>  <li class="active">
               <NavLink to="/" className="active" aria-current="page">Biblioteca</NavLink>
               </li></DropdownItem>
               
                {/* <DropdownItem>  <li class="active">
               <NavLink to="/Salasdelectura" className="active" aria-current="page">Salas de lectura</NavLink>
               </li></DropdownItem>
                <DropdownItem>  <li class="active">
               <NavLink to="/LoginAdmin" className="active" aria-current="page">Login</NavLink>
               </li></DropdownItem> */}
               </ul>
            </DropdownMenu>
            </Dropdown>
            </span>
        </nav>

      

    </section>
    </div>
  )
}
