import React from "react";
import { Backdrop, LinearProgress, Paper, Button } from "@material-ui/core";
//import ProgressBar from "../components/ProgressBar";
import ProcessingVideo from "../processingVideo"

const ProcessingProgress = ({ isOpen, close, estado, heatMap }) => {
  return (
    <Backdrop className="backdrop" open={isOpen}>
      <Paper className="backdrop-card" elevation={3}>
        <h3>Procesamiento del video</h3>
        <div style={{width: "100%"}}>
          {console.log("parametros á procesar", estado)}
          <ProcessingVideo parametros={estado} heatMap={heatMap}/>
        </div>
        <div>
        <p></p>
        </div>
        <Button variant="outlined" onClick={close}>
          Cerrar  
        </Button>
      </Paper>
    </Backdrop>
  );
};

export default ProcessingProgress;
