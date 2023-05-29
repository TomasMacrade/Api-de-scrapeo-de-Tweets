#Traigo las librerías

import pandas as pd

from flask import Flask
from flask import request

# Importo los datos

Data = pd.read_csv("/opt/airflow/src/Tweets.csv")

if __name__ == '__main__':

    app =  Flask(__name__)

    # El metodo ".route()" tiene en sus parametros por default el metodo GET. 

    # Ruta Principal
    @app.route("/") 
    def index():

 #       C_Tweets = len(Data)
 #       C_Candidatos = (len(Data["Candidato"].value_counts()))
        return "Encontramos {} tweets de {} candidatos".format("C_Tweets","C_Candidatos")


    # Ruta para consultar : http://localhost:5000//results?Nombrecandidato
    @app.route("/results") 
    def search(): 

        args = request.args # Recibe los argumentos que tiene la url al realizar la query
        query_values = args.to_dict() # Convierto los argumentos en el tipo de dato 'dict'
        print(list(query_values.keys())[0])

        return "Acá van a aparecer los resultados del candidato {}".format(list(query_values.keys())[0])

    app.run(debug=False, host='0.0.0.0', port=5000) # Ejecución del servidor/API


