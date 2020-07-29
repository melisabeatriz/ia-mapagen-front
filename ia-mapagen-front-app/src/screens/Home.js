import React from "react";
import { Button, Link, Grid, Typography } from "@material-ui/core";
import { useHistory } from "react-router-dom";
import Logo from "../img/abremate_unla.png";
import paths from "../constants/paths";

const Home = () => {
  let history = useHistory();

  const redirectToVideoProcessor = () => history.push(paths.videoProcessor);
  const redirectToHeatMapProcessor = () => history.push(paths.heatMapProcessor);

  return (
    <div className="home-background">
      <Grid
        container
        direction="row"
        justify="flex-end"
        alignItems="flex-start"
      >
        <Link href="#">Acerca de IA MapaGen</Link>
      </Grid>
      <h4 className="home-subtitle">¡BIENVENIDOS!</h4>
      <h1 className="home-title">IA MapaGen</h1>
      <p className="home-description">
        Este es un software de código abierto que permite analizar un video y
        detectar a las personas que se encuentran en cada frame.
      </p>
      <Button
        onClick={redirectToVideoProcessor}
        className="add-margin-right"
        variant="contained"
        color="primary"
      >
        analizar video
      </Button>
      <Button
        onClick={redirectToHeatMapProcessor}
        variant="outlined"
        color="primary"
      >
        analizar mapa de calor
      </Button>
      <div className="home-icons-container">
        <Typography variant="caption">En colaboración con </Typography>
        <img
          className="home-logo"
          src={Logo}
          alt="Logos Universidad Nacional de Lanús y Abremate"
        />
      </div>
    </div>
  );
};

export default Home;
