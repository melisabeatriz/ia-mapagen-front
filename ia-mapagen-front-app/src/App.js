import React from "react";
import VideoProcessor from "./screens/VideoProcessor";
import Home from "./screens/Home";
import HeatMapProcessor from "./screens/HeatMapProcessor";
import "./App.css";
import { BrowserRouter as Router, Route } from "react-router-dom";
import paths from "./constants/paths";

function App() {
  return (
    <Router>
      <div className="App">
        <Route exact path="/">
          <Home />
        </Route>
        <Route path={paths.videoProcessor}>
          <VideoProcessor />
        </Route>
        <Route path={paths.heatMapProcessor}>
          <HeatMapProcessor />
        </Route>
      </div>
    </Router>
  );
}

export default App;
