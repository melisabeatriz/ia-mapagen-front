import React, { useState } from "react";
import { Button } from "@material-ui/core";
import FileUploader from "../components/FileUploader";
import SliderSelector from "../components/SliderSelector";
import ProcessingProgress from "../components/ProcessingProgress";

const VideoProcessor = () => {
  const [personMatch, setPersonMatch] = useState(1);
  const [skippedFrames, setSkippedFrames] = useState(10);
  const [videoFile, setVideoFile] = useState("");
  const [neuralMap, setNeuralMap] = useState("");
  const [classFile, setClassFile] = useState("");
  const [processInProgress, setProcessInProgress] = useState(false);

  const videoProcessorSettings = {
    personMatch,
    skippedFrames,
    videoFile,
    neuralMap,
    classFile,
  };

  const onStartClick = () => {
    setProcessInProgress(true);
    // Acá tendríamos que esta info de alguna manera mandarla al programa para que la pueda interpretar
    console.log(JSON.stringify(videoProcessorSettings));
  };
  return (
    <div className="video-processor-container">
      <h1>IA MapaGen - Procesador de video</h1>
      <FileUploader legend="Video a analizar" uploadFile={setVideoFile} />
      <FileUploader legend="Red neuronal" uploadFile={setNeuralMap} />
      <FileUploader legend="Archivo de clases" uploadFile={setClassFile} />
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
      <Button variant="contained" color="primary" onClick={onStartClick}>
        Iniciar
      </Button>
      <ProcessingProgress
        isOpen={processInProgress}
        close={() => setProcessInProgress(false)}
        estado={FileUploader.setVideoFile}
        />
        {console.log("video ->" + setVideoFile.)}
    </div>
  );
};

export default VideoProcessor;
