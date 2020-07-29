import React, { useState } from "react";
import { Button, FormControlLabel, Checkbox } from "@material-ui/core";
import FileUploader from "../components/FileUploader";
import FileSaver from "../components/FileSaver";
import SliderSelector from "../components/SliderSelector";
import ProcessingProgress from "../components/ProcessingProgress";

const HeatMapProcessor = () => {
  const [squaresQty, setSquaresQty] = useState(213);
  const [hRadius, setHRadius] = useState(179);
  const [maxIntensity, setMaxIntensity] = useState(50);
  const [processInProgress, setProcessInProgress] = useState(false);

  return (
    <div className="video-processor-container">
      <h1>IA MapaGen - Generador de mapa de calor</h1>
      <FileUploader
        buttonText="elegir archivo"
        legend="Video a analizar (se tomará la imagen para generar el mapa)"
      />
      <FileUploader buttonText="elegir archivo" legend="Archivo SCV" />
      {/* <FileSaver
        buttonText="elegir ubicación"
        legend="Ubicación de salida del video"
      />
      <FileSaver
        buttonText="elegir ubicación"
        legend="Ubicación de salida del video"
      /> */}
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

export default HeatMapProcessor;
