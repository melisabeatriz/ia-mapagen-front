import React from "react";
import { Button, Typography, Grid } from "@material-ui/core";
import { useFilePicker } from "use-file-picker";
import { isEmpty } from "lodash";

const FileUploader = ({ legend, uploadFile }) => {
  const [openFileSelector, { filesContent, loading, acceptedFileType }] =
    useFilePicker({
      // accept: acceptedFileType,
      multiple: false,
    });

  if (!isEmpty(filesContent)) {
    uploadFile(filesContent[0].name);
  }
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
          {loading ? (
            <Typography variant="subtitle1">Cargando...</Typography>
          ) : (
            <>
              <Typography variant="subtitle1">
                {isEmpty(filesContent)
                  ? "No se eligió ningún archivo."
                  : filesContent[0].name}
              </Typography>
              <Button
                variant="contained"
                color="primary"
                onClick={() => openFileSelector()}
              >
                {isEmpty(filesContent) ? "Elegir archivo" : "Modificar archivo"}
              </Button>
            </>
          )}
        </Grid>
      </fieldset>     

    </>
  );
};

export default FileUploader;
