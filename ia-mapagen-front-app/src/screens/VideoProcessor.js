import React, { useState } from "react";
import { Button, FormControlLabel, Checkbox } from "@material-ui/core";
import FileUploader from "../components/FileUploader";
import FileSaver from "../components/FileSaver";
import SliderSelector from "../components/SliderSelector";
import ProcessingProgress from "../components/ProcessingProgress";

const VideoProcessor = () => {
  const [personMatch, setPersonMatch] = useState(1);
  const [skippedFrames, setSkippedFrames] = useState(10);
  const [processInProgress, setProcessInProgress] = useState(false);

  return (
    <div className="video-processor-container">
      <h1>IA MapaGen - Procesador de video</h1>
      <FileUploader buttonText="elegir archivo" legend="Video a analizar" />
      <FileUploader buttonText="elegir archivo" legend="Red neuronal" />
      <FileUploader buttonText="elegir archivo" legend="Archivo de clases" />
      <FileSaver
        buttonText="elegir ubicación"
        legend="Ubicación de salida del video"
      />
      <FileSaver
        buttonText="elegir ubicación"
        legend="Ubicación de salida del video"
      />
      <SliderSelector
        label="Porcentaje de coincidencia para detecciones"
        explanation="Se recomienda ingresar un valor bajo para que se detecte a todas las personas de la imagen, por más que tenga una baja probabilidad de ser una persona."
        values={{
          min: 1,
          max: 99,
          default: personMatch,
          setter: setPersonMatch,
        }}
        isPercentage
      />
      <SliderSelector
        label="Cada cuantos frames analizar"
        explanation="Se saltearán varios frames para acelerar el procesamiento del video. A mayor número, procesamiento más rápido."
        values={{
          min: 1,
          max: 24,
          default: skippedFrames,
          setter: setSkippedFrames,
        }}
      />
      {/* <FormControlLabel
        control={
          <Checkbox
            checked={false}
            onChange={() => console.log("noop")}
            name="checkedB"
            color="primary"
          />
        }
        label="Visualizar mientras se renderiza"
      /> */}
      <Button
        variant="contained"
        color="primary"
        onClick={() => setProcessInProgress(true)}
      >
        Iniciar
      </Button>
      <ProcessingProgress
        isOpen={processInProgress}
        close={() => setProcessInProgress(false)}
      />
    </div>
  );
};

export default VideoProcessor;
