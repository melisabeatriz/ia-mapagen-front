import React from "react";
import { Button, Typography, Grid } from "@material-ui/core";

const FileSaver = ({ buttonText, legend }) => {
  return (
    <>
      <fieldset>
        <legend>{legend}</legend>
        <Grid
          container
          direction="row"
          justify="space-between"
          alignItems="center"
        >
          <Typography variant="subtitle1">
            No se eligió ninguna ubicación.
          </Typography>
          <Button variant="outlined" color="primary">
            {buttonText}
          </Button>
        </Grid>
      </fieldset>
    </>
  );
};

export default FileSaver;
