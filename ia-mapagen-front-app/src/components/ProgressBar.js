  
import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';


function ProgressBar(props) {
    return (
        <div className="contenedorProgressBar">
            <span className="progressText">{props.estado ? props.estado : "..."}</span>        
            <div className="progress">
                <div className="progress-bar progress-bar-striped progress-bar-animated"
                role="progressbar"
                style={{backgroundColor: props.cancelado ? props.cancelado : props.cancelado, width: props.porcentaje ? props.porcentaje +"%": "100%"}}>
                {`${props.porcentaje}%`}    
                </div>
            </div>
             <span className="progressText"> &nbsp; Transcurrido: {props.transcurrido ? props.transcurrido : " - "}&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; </span> 
             <span className="progressText"> &nbsp; Restante: {props.restante ? props.restante : " - "}  </span> 
        </div>
    );
}

export default ProgressBar;

