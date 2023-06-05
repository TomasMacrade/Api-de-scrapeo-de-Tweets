# Flask

En esta carpeta y en sus carpetas hijas se encuentra todo lo necesario para que flask corra tomando lo obtenido en el proceso anterior.

# Carpetas

- app contiene los requirments de la api y la api propiamente dicha (app.py).

- app/static contiene las imágenes usadas en la página.

- app/templates contiene los templates usados en la página.

- app/static/styles el archivo .css.

# Archivos

- El archivo docker-compose.yaml es el que permite configurar los puertos de publicación y los volumenes de Flask.

- Dockerfile es la imagen de docker que se va a usar.

# Pasos para que corra el proceso

- Con un "docker-compose up -d " ya tenemos Flask funcionando (se entra por localhost:5000).