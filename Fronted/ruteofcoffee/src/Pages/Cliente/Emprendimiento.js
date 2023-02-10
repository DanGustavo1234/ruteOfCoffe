import React from 'react'
import { Emprendimiento } from "../../componentes/cliente/Emprendimiento";
import { Footer} from "../../componentes/cliente/Footer";
import {Header} from "../../componentes/cliente/Header";
import { AgregarEmprendimiento} from '../../componentes/cliente/AgregarEmprendimiento';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

 export function Emprendimientos() {
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
            <Col><Emprendimiento/> </Col>
    
          </Row>
          <Row>
            <Col><AgregarEmprendimiento/> </Col>
    
          </Row>
        </Container>
         <footer>
         <Footer/>
         </footer>
         </div>
    )
 }