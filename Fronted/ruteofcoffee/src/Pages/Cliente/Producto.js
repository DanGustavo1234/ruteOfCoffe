import React from 'react'
import {Productos} from '../../componentes/cliente/Productos/Productos'
import { Footer} from "../../componentes/cliente/Footer";
import {Header} from "../../componentes/cliente/Header";
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

export function Producto() {
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
        <Col><Productos /> </Col>

      </Row>
      <Row>
        <Col>Hola</Col>

      </Row>
    </Container>
     <footer>
     <Footer/>
     </footer></div>
  )
}
