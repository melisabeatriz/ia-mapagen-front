import React, { useState } from "react";
import { Button } from "@material-ui/core";
import FileUploader from "../components/FileUploader";
import SliderSelector from "../components/SliderSelector";
import ProcessingProgress from "../components/ProcessingProgress";

const HeatMapProcessor = () => {
  const [squaresQty, setSquaresQty] = useState(213);
  const [hRadius, setHRadius] = useState(179);
  const [maxIntensity, setMaxIntensity] = useState(50);
  const [videoFile, setVideoFile] = useState("");
  const [CSVFile, setCSVFile] = useState("");
  const [processInProgress, setProcessInProgress] = useState(false);

  const heatMapProcessorSettings = {
    videoFile,
    CSVFile,
    squaresQty,
    hRadius,
    maxIntensity,
  };

  const onStartClick = () => {
    setProcessInProgress(true);
    // Acá tendríamos que esta info de alguna manera mandarla al programa para que la pueda interpretar
    console.log(JSON.stringify(heatMapProcessorSettings));
  };
  return (
    <div className="video-processor-container">
      <h1>IA MapaGen - Generador de mapa de calor</h1>
      <FileUploader
        uploadFile={setVideoFile}
        legend="Video a analizar (se tomará la imagen para generar el mapa)"
      />
      <FileUploader uploadFile={setCSVFile} legend="Archivo SCV" />
      <SliderSelector
        label="Cantidad de cuadrados de la grilla"
        explanation="A mayor número, los cuadrados serán más chiquitos y tendrán mejor definición."
        values={{
          min: 85,
          max: 426,
          default: squaresQty,
          setter: setSquaresQty,
        }}
      />
      <SliderSelector
        label="Radio H"
        explanation="A mayor valor, las áreas rojas se harán más grandes."
        values={{
          min: 102,
          max: 204,
          default: hRadius,
          setter: setHRadius,
        }}
      />
      <SliderSelector
        label="Intensidad máxima"
        explanation="Define la escala de valores. Si se quiere generar mapas de calor de diferentes cámaras que mantengan el mismo límite
        máximo, debe ingresar el mismo límite máximo al generar todos los mapas de calor."
        values={{
          min: 30,
          max: 100,
          default: maxIntensity,
          setter: setMaxIntensity,
        }}
      />
      <Button variant="contained" color="primary" onClick={onStartClick}>
        Iniciar
      </Button>
      <ProcessingProgress
        isOpen={processInProgress}
        close={() => setProcessInProgress(false)}
      />
    </div>
  );
};

export default HeatMapProcessor;
