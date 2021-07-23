import React, { useState } from "react";
import { Typography, Slider, Button, Grid, Modal } from "@material-ui/core";
import HelpOutlineIcon from "@material-ui/icons/HelpOutline";

const SliderSelector = ({
  values,
  label,
  explanation,
  isPercentage = false,
}) => {
  const handleChange = (event, newValue) => values.setter(newValue);
  const [tipOpen, setTipOpen] = useState(false);

  return (
    <>
      <Grid
        container
        direction="row"
        justify="space-between"
        alignItems="center"
      >
        <Typography variant="subtitle1">{label}</Typography>
        <Button onClick={() => setTipOpen(true)}>
          <HelpOutlineIcon />
        </Button>
        {tipOpen && (
          <Typography>
            <i>{explanation}</i>
          </Typography>
        )}
      </Grid>
      <div className="slider-container">
        <p>{`${values.min}${isPercentage ? "%" : ""}`}</p>
        <Slider
          value={values.default}
          min={values.min}
          max={values.max}
          onChange={handleChange}
          aria-labelledby="continuous-slider"
        />
        <p>{`${values.max}${isPercentage ? "%" : ""}`}</p>
      </div>
    </>
  );
};

export default SliderSelector;
