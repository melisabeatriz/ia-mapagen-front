import React, { Component } from 'react';
import ProgressBar from "./components/ProgressBar";
//import 'bootstrap/dist/css/bootstrap.min.css';
import * as data from "./salidaPython.json";
import {  LinearProgress, Button } from "@material-ui/core";

class processingVideo extends Component {
state={
  trascurrido: "",
  restante: "",
  porcentaje: 0.0,
  estado: "",
  pid: -1,
  cancelado: 'blue'
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
  while (self.state.porcentaje < 100 && self.state.estado != "Detenido" && self.state.estado != "Proceso Finalizado" && self.state.estado != "Proceso interrumpido por el usuario" && self.state.estado != "Ha ocurrido un error en el procesamiento"){
    const data = await this.performTimeConsumingTask();
    await fetch('/actualizarPorcentaje').then(res => res.json())
        .then((data) => {
          self.setState({ porcentaje: data.porcentaje, estado: data.estado, transcurrido: data.transcurrido, restante: data.restante })
        })
        console.log("Porcentaje: " + self.state.porcentaje)   
    }
}

simular=async()=>{
  const self=this;

  console.log("parametros en simular: " +  this.props.parametros.neuralMap)  //trato leer paramtetros

  console.log("ejecuto Video Processor")
  await fetch('/resetPorcentaje').then(res => res.json())
  .then((data) => {
    self.setState({ porcentaje: data.porcentaje, estado: data.estado, transcurrido: data.transcurrido, restante: data.restante })
  })  
  //http://localhost:5000/runVideoProcessor?
  //pathVideoToAnalizer="C:\pathVideoToAnalizer.csv"&pathVideoOutput="C:\pathVideoOutput.avi"&pathNeural="C:\pathNeural&pathClassFile="C:\pathClassFile&minPercentage=100&numberOfFrames=20"
  
  self.setState({ cancelado: 'blue' })
  
/*
    personMatch,
    skippedFrames,
    videoFile,
    neuralMap,
    classFile,
  */
  let parametros_run = 'pathVideoToAnalizer="'+ this.props.parametros.videoFile +'"&pathVideoOutput="'+ 'pathVideoOutput.avi' +'"&pathNeural="'+ this.props.parametros.neuralMap +
                          '"&pathClassFile="'+ this.props.parametros.classFile + '"&minPercentage="'+  this.props.parametros.personMatch +'"&numberOfFrames="'
                          + this.props.parametros.skippedFrames+'"';
  console.log("cadena enviada", parametros_run);                      

  await fetch('/runVideoProcessor?'+ parametros_run ).then(res => res.json()).then((data) => 
      {
        self.state.pid = data.proceso
      })  
  /*
  await fetch('/runHeatMapWithParameters').then(res => res.json())
  .then((data) => {
    self.state.pid = data.proceso
  })  */
  console.log("Porcentaje: " + self.state.porcentaje)   
  
  this.actualizarPorc()

  console.log("CREE PROCESO: " + self.state.pid)   
}

/* ejecutar Heat Map*/
simularHeatMap=async()=>{
  const self=this;

  console.log("parametros en simular Heat Map: " +  this.props.parametros)  //trato leer paramtetros

  console.log("ejecuto heatMAP")
  await fetch('/resetPorcentaje').then(res => res.json())
  .then((data) => {
    self.setState({ porcentaje: data.porcentaje, estado: data.estado, transcurrido: data.transcurrido, restante: data.restante })
  })  
  //http://localhost:5000/runHeatMap?
  //pathCSVFile="C:\pathCSVFile.csv"&pathVideoToAnalizer="C:\pathVideoToAnalizer.avi"&squaresQuantity=10&radiusH=5&pathHeatMapGenerate="C:\pathHeatMapGenerate.csv"

  self.setState({ cancelado: 'blue' })
  
/*
    videoFile,
    CSVFile,
    squaresQty,
    hRadius,
    maxIntensity,
  */
  let parametros_run = 'pathCSVFile="'+ this.props.parametros.CSVFile +'"&pathVideoToAnalizer="'+ this.props.parametros.videoFile +
                          '"&squaresQuantity="'+ this.props.parametros.squaresQty + '"&radiusH="'+  this.props.parametros.hRadius + '"&pathHeatMapGenerate="'  + 'pathHeatMapGenerate.map' +
                          '"&maxIntensity="' + this.props.parametros.maxIntensity +'"';
  console.log("cadena enviada", parametros_run);                      

  await fetch('/runHeatMap?'+ parametros_run ).then(res => res.json()).then((data) => 
      {
        self.state.pid = data.proceso
      })  
  /*
  await fetch('/runHeatMapWithParameters').then(res => res.json())
  .then((data) => {
    self.state.pid = data.proceso
  })  */
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
  self.setState({ cancelado: 'red' })

  await fetch('/finalizarActualizarPorcentaje').then(res => res.json())
        .then((data) => {
          self.setState({ porcentaje: data.porcentaje, estado: data.estado, transcurrido: data.transcurrido, restante: data.restante })
        })
        console.log("Porcentaje: " + self.state.porcentaje)   
}


render(){
  return (
    <div>
      {console.log("param en render" ,this.props.heatMap)}
    <div className="App" margin-bottom="20px">
        <Button variant="outlined" onClick={this.props.heatMap ? ()=>this.simularHeatMap() : ()=>this.simular() } param={this.props.parametros}>
          Comenzar
        </Button>
        <div>  &nbsp;
        </div>  

        <Button variant="outlined" onClick={()=>this.detener()}>
          Detener 
        </Button>
      </div>  
      <div className="progressBar">
      {
      <ProgressBar variant="determinate" 
        porcentaje={this.state.porcentaje}
        estado={this.state.estado}        
        cancelado={this.state.cancelado}
        transcurrido={this.state.transcurrido}  
        restante={this.state.restante}    
      />
      }    
      </div>      
    </div>
  );
}
}
export default processingVideo;
