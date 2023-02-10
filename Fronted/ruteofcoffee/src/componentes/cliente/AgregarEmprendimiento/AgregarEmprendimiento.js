import React from 'react'
import { Form } from 'reactstrap'
import { FormGroup, Label ,Input} from 'reactstrap'
import axios from 'axios'
export {AgregarEmprendimiento}

class  AgregarEmprendimiento extends React.Component {

  emprendimiento={
     'id':4,
    'tipo_emprendimiento' : 0,
    'nombre_emprendimiento': "",
    'direccion': "", 
    'telefono': "",
    'descripcion': "",
    'horario_apertura': null,
    'horario_cierre': null,
    'altitud': "",
    'latitud':"",
    'foto':"",
    'video': "",
    'instagram': "",
    'facebook': "",
    'twitter': "",
    'producto': "",
};

componentePermanente(){
  if(this.props.emprendimiento){
    const {  id,
    tipo_emprendimiento,
    nombre_emprendimiento,
    direccion, 
    telefono,
    descripcion,
    horario_apertura,
    horario_cierre,
    altitud,
    latitud,
    foto,
    video,
    instagram,
    facebook,
    twitter,
    producto
  }= this.emprendimiento

    this.setEmprendimiento({id,
      tipo_emprendimiento,
      nombre_emprendimiento,
      direccion, 
      telefono,
      descripcion,
      horario_apertura,
      horario_cierre,
      altitud,
      latitud,
      foto,
      video,
      instagram,
      facebook,
      twitter,
      producto})
  }
};

onChange=e=>{
  this.setEmprendimiento({[e.target.name]: e.target.value});
};

crearEmprendimiento=e=>{
  e.preventDefault();
  axios.post('http://127.0.0.1:8000/api/emprendimiento/'+ this.emprendimiento.id , this.emprendimiento).then(()=>{
    
  })
};

  render(){
    return (
      <div>
          <Form >
              <FormGroup>
                  <Label for='nombre_emprendimiento'>Nombre del emprendimiento </Label>
                  <Input type='text' name='nombre_emprendimiento' ></Input>
              </FormGroup>
              <FormGroup>
                  <Label for='tipo_emprendimiento'> Nombre del Emprendimiento </Label>
                  <Input type ='text' name='tipo_emprendimiento'  ></Input>
              </FormGroup>
              <FormGroup>
                  <Label for='nombre_emprendimiento'> Nombre del Emprendimiento </Label>
                  <Input type ='text' name='nombre_emprendimiento'  ></Input>
              </FormGroup>
              <FormGroup>
                  <Label for='direccion'> Dirección </Label>
                  <Input type ='text' name='direccion'  ></Input>
              </FormGroup>
              <FormGroup>
                  <Label for='Celular'> celular </Label>
                  <Input type ='text' name='celular' ></Input>
              </FormGroup>
              <FormGroup>
                  <Label for='telefono fijo'>Telefono fijo </Label>
                  <Input type ='text' name='telefono fijo'  ></Input>
              </FormGroup>
              <FormGroup>
                  <Label for='descripcion'> Descripcion </Label>
                  <Input type ='text' name='descripcion' ></Input>
              </FormGroup>
              <FormGroup>
                  <Label for='hora_Apertura'> Hora apertura </Label>
                  <Input type ='text' name='hora_Apertura' ></Input>
              </FormGroup>
              <FormGroup>
                  <Label for='hora_cierre'> Hora cierre </Label>
                  <Input type ='text' name='nombre_emprendimiento' ></Input>
              </FormGroup>
              <FormGroup>
                  <Label for='altitud'> Altitud </Label>
                  <Input type ='text' name='Altitud'  ></Input>
              </FormGroup>
              <FormGroup>
                  <Label for='Latitud'> Latitud</Label>
                  <Input type ='text' name='latitud'  ></Input>
              </FormGroup>
              <FormGroup>
                  <Label for='Foto'> Foto</Label>
                  <Input type ='text' name='foto'  ></Input>
              </FormGroup>
              <FormGroup>
                  <Label for='video '> video</Label>
                  <Input type ='text' name='video'  ></Input>
              </FormGroup>
              <FormGroup>
                  <Label for='instagram'> Instagram </Label>
                  <Input type ='text' name='instagram'  ></Input>
              </FormGroup>      
              <FormGroup>
                  <Label for='facebook'> Facebook</Label>
                  <Input type ='text' name='facebook'  ></Input>
            </FormGroup>
          </Form>
  
      </div>
    )

  }
 

} 
