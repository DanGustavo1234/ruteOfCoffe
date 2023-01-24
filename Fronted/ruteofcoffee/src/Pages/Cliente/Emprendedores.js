import React from 'react'
import { Emprendedor } from "../../componentes/cliente/Emprendedores/Emprendedor";
import { Footer} from "../../componentes/cliente/Footer";
import {Header} from "../../componentes/cliente/Header";
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

export  function Emprendedores() {
  return (
    <div>  <header>
    <Header/>
    </header>
    <Container className="container">
      <Row>
        <Col>
          
        </Col>
      </Row>
      <Row>
        <Col><Emprendedor /> </Col>

      </Row>
      <Row>
        <Col>Favoritos</Col>

      </Row>
    </Container>
     <footer>
     <Footer/>
     </footer></div>
  )
}
