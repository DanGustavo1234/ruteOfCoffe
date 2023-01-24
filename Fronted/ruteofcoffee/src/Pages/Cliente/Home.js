import React from "react";
import { Footer} from "../../componentes/cliente/Footer";
import {Header} from "../../componentes/cliente/Header";
import {Carrusel} from "../../componentes/cliente/Carrusel"
import { Emprendimiento } from "../../componentes/cliente/Emprendimiento";
import { Categorias } from "../../componentes/cliente/Categorias";
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
 
export  function Home() {
  return (
    <div>

    <header>
    <Header/>
    </header>
    <div className="container">
      <div className="row">
        <Carrusel/>
      </div>
      <div className="row">
        <Categorias/>
      </div>
    </div>
     <footer>
     <Footer/>
     </footer>
    
    </div>
  )
}
