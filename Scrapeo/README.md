# Scrapeo de perfiles elecciones 2023 Twitter
El siguiente repositorio busca hacer un scrapeo del twitter de los principales referentes/candidatos en la elección 2023 en Argentina de forma automática y mostrar los resultados de la última semana en un sitio web.

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

- En la carpeta Imagenes, las gráficos que se eligieron hacer en base a la información.


# Archivos

- El archivo docker-compose.yaml es el que permite la automatización de los procesos vía airflow.

- Dockerfile es la imagen de docker que se va a usar.

- requirements.txt es el listado de paquetes que deben instalarse en el contenedor.




# Pasos para que corra el proceso

- Con un "docker-compose up -d --build " ya tenemos airflow y docker funcionando.






