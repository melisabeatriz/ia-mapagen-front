# ia-mapagen-front

### Repositorio del FrontEnd de ia-mapagen
Para iniciar la interfaz, desde la carpeta ia-mapagen-front-app correr el comando ```npm install```, para instalar todas las dependencias, y posteriormente ```npm run start```.
Para introducir cambios, crear una rama a partir de master, con el nombre de los combios a introducir, y crear un Pull Request.


Nico:

Borrar carpetas en api -> __pycache__, Include, Lib, Scripts
Ejecutar dentro de api: 
$ python -m venv venv
$ venv\Scripts\activate
Finalmente
(venv) $ pip install flask python-dotenv

Para correr el server flask ejecutar y el front end ejecutar dos consolas, en una correr "npm run start" y en la otra "npm run start-api"