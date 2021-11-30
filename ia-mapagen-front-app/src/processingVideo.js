import React, { Component } from 'react';
import ProgressBar from "./components/ProgressBar";
//import 'bootstrap/dist/css/bootstrap.min.css';
import * as data from "./salidaPython.json";
import {  LinearProgress, Button } from "@material-ui/core";

class processingVideo extends Component {
state={
  porcentaje: 0.0,
  pid: -1
}

performTimeConsumingTask = async() => {
  return new Promise((resolve) =>
    setTimeout(
      () => { resolve('result') },
      3000
    )
  )
  }

actualizarPorc=async()=>{
  const self=this;
  while (self.state.porcentaje < 100 ){
    const data = await this.performTimeConsumingTask();
    await fetch('/actualizarPorcentaje').then(res => res.json())
        .then((data) => {
          self.setState({ porcentaje: data.porcentaje })
        })
        console.log("Porcentaje: " + self.state.porcentaje)   
    }
}

simular=async()=>{
  const self=this;

  console.log("ejecuto heatMAP")
  await fetch('/resetPorcentaje').then(res => res.json())
  .then((data) => {
    self.state.pid = data.porcentaje
  })  
  //await fetch('/runHeatMap?pathCSVFile="C:\\pathCSVFile.csv"&pathVideoToAnalizer="C:\\pathVideoToAnalizer.avi"&squaresQuantity=10&radiusH=5&pathHeatMapGenerate="C:\\pathHeatMapGenerate.csv').then(res => res.json())
  await fetch('/runHeatMapWithParameters').then(res => res.json())
  .then((data) => {
    self.state.pid = data.proceso
  })  
  console.log("Porcentaje: " + self.state.porcentaje)   
  
  this.actualizarPorc()

  console.log("CREE PROCESO: " + self.state.pid)   
}


detener=async()=>{
  const self=this;  
  console.log("MATO PROCESO: " + self.state.pid)
    await fetch('/stopHeatMap?pidToKill=' + self.state.pid).then(res => res.json())
    .then((data) => {
      console.log("Resultado Detener: ", data.status )
    })  
  self.setState({ porcentaje: 100 })
  await fetch('/finalizarActualizarPorcentaje').then(res => res.json())
        .then((data) => {
          self.setState({ porcentaje: data.porcentaje })
        })
        console.log("Porcentaje: " + self.state.porcentaje)   
}


render(){
  return (
    <div>
    <div className="App" margin-bottom="20px">
        <Button variant="outlined" onClick={()=>this.simular()}>
          Simular
        </Button>
        <Button variant="outlined" onClick={()=>this.detener()}>
          Detener
        </Button>
      </div>  
      <div className="progressBar">
      {
      <ProgressBar variant="determinate" 
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
