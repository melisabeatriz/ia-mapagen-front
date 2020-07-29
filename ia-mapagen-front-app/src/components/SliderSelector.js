import React, { useState } from "react";
import { Typography, Slider, Tooltip, Grid } from "@material-ui/core";
import HelpOutlineIcon from "@material-ui/icons/HelpOutline";

const SliderSelector = ({
  values,
  label,
  explanation,
  isPercentage = false,
}) => {
  const handleChange = (event, newValue) => values.setter(newValue);

  return (
    <>
      <Grid
        container
        direction="row"
        justify="space-between"
        alignItems="center"
      >
        <Typography variant="subtitle1">{label}</Typography>

        <Tooltip title={explanation} arrow placement="top-end">
          <HelpOutlineIcon />
        </Tooltip>
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
