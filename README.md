# Scrapeo de perfiles elecciones 2023 Twitter
El siguiente repositorio busca hacer un scrapeo del twitter de los principales referentes/candidatos en la elección 2023 en Argentina de forma automática y mostrar los resultados de la última semana en un sitio web. Además de todo lo que este repositorio contiene, el host deberá tener una base de datos postgres con los creates e inserts especificádos en el archivo "Creates e Inserts.sql" para funcionar.

# Candidatos
- Villarruel
- Marra
- Espert
- Larreta
- Bullrich
- Vidal
- Massa
- Grabois
- Kicillof
- Bregman
- Solano
- Del Caño

Milei no aparece por problemas al scrapear su perfil.


# Carpetas

- En la carpeta Data se encontrará los csv que contiene la información del scrapping de cada candidato.

- En la carpeta Scripts, los scripts que hacen funcionar el scapping.

- En la carpeta dags se encuentran los DAGs de Airflow y su configuración.

- En la carpeta logs se encontrarán los logs de los procesos de Airflow.

- Las carpetas config y plugis fueron agregadas para seguir la documentación oficial de Airflow 2.2.4 que las sugerían.

- En la carpeta Flask, todo lo necesario para que la página web funcione (tiene su propio README.md).


# Archivos

- El archivo docker-compose.yaml es el que permite la automatización de los procesos vía airflow.

- Dockerfile es la imagen de docker que se va a usar.

- requirements.txt es el listado de paquetes que deben instalarse en el contenedor.

- Creates e Inserts.sql es el listado de Tablas y su llenado para que el postgres corriendo en la máquina local pueda estar listo para trabajar.


# Pasos para que corra el proceso

- Con un "docker-compose up -d " ya tenemos airflow funcionando (hay que activarlo entrando por localhost:8090).


# Diagrama de Arquitectura



<img src="CEN.drawio.png" style = "display: block;
  margin-left: auto;
  margin-right: auto;" />






