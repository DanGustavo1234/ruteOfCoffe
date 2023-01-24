import React, { Component } from 'react';
import Carousel from 'react-bootstrap/Carousel'
import gringos from '../../../assets/img/gringos.jpg'
import glamping from '../../../assets/img/glamping.jpg'
import milenial from '../../../assets/img/milenial.jpeg'
import './Carrusel.scss'


export  function Carrusel() {
  

  return (
    <Carousel>
      <Carousel.Item>
        <img
          className="img"
          src={gringos}
          alt="First slide"
        />
        <Carousel.Caption>
          <h3>La ruta del café</h3>
        </Carousel.Caption>
      </Carousel.Item>
      <Carousel.Item>
        <img
          className="img"
          src={glamping}
          alt="Second slide"
        />

        <Carousel.Caption>
          <h3>La ruta del café</h3>
        </Carousel.Caption>
      </Carousel.Item>
      <Carousel.Item>
        <img
          className="img"
          src={milenial}
          alt="Third slide"
        />

        <Carousel.Caption>
          <h3>La ruta del café</h3>
        </Carousel.Caption>
      </Carousel.Item>
    </Carousel>
  )
}

export default Carrusel;