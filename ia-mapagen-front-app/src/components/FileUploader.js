import React from "react";
import { Button, Typography, Grid } from "@material-ui/core";

const FileUploader = ({ buttonText, legend }) => {
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
            No se eligió ningún archivo.
          </Typography>
          <Button variant="contained" color="primary">
            {buttonText}
          </Button>
        </Grid>
      </fieldset>
    </>
  );
};

export default FileUploader;
