import React, { Component } from 'react';
import ProgressBar from "./components/ProgressBar";
import 'bootstrap/dist/css/bootstrap.min.css';
import * as data from "./salidaPython.json";

class processingVideo extends Component {
state={
  porcentaje: 0.0
}

simular=async()=>{
   const self=this;
  
  await fetch('/resetPorcentaje').then(res => res.json())
  .then((data) => {
    self.setState({ porcentaje: data.porcentaje })
  })
  console.log(self.state.porcentaje)

  for (let i = self.state.porcentaje; i < 100; i++) {  //mientras no llegue al 100%
    await setTimeout(function timer(){
    //  self.setState({porcentaje:  self.state.porcentaje+porcentajeUnitario,
      //archivosRestantes: self.state.archivosRestantes-1});
      
      fetch('/actualizarPorcentaje').then(res => res.json())
      .then((data) => {
        self.setState({ porcentaje: data.porcentaje })
      })

      console.log(self.state.porcentaje)
      console.log(i)

    }, (2000*i))
    
  }
}

 render(){
  return (
    <div className="App" margin-bottom="20px">
      <div className="btn btn-success" onClick={()=>this.simular()}>Simular </div>
      
      <div className="progressBar">
      {
      <ProgressBar 
        porcentaje={this.state.porcentaje}
        texto={"Procesando.."}        
      />
      }
      </div>
      
    </div>
  );
}
}
export default processingVideo;

/*
const a = data.archivosRestantes;
console.log(a); // output "testing"
const p = data.porcentaje;
console.log(p); // output "testing" */