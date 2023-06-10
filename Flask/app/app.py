#Traigo las librerías

import pandas as pd

from flask import Flask, render_template,request



if __name__ == '__main__':

    app =  Flask(__name__)

    # Ruta Principal
    @app.route("/") 
    def index():
        # Importo los datos

        Data = pd.read_csv("../Data/Tweets.csv")
        Data["Relevancia"] = (Data["Cantidad de Likes"] + Data["Cantidad de retweets"] +Data["Veces citado"])/3
        Data = Data.sort_values(by=['Relevancia'],ascending=False)
        Aux = Data.iloc[0]
        Texto_semana = Aux["Tweet"]
        Nombre_semana = Aux["Candidato"]
        Usr_Sem = Aux["Usr"]
        Url_Sem = Aux["url"]
        Fecha_Sem = Aux["Fecha-Hora"]
        Likes_Sem = Aux["Cantidad de Likes"]
        Rt_Sem = Aux["Cantidad de retweets"]
        Citas_Sem = Aux["Veces citado"]
        Cand_Tw = Data["Candidato"].value_counts().index.tolist()[0]
        Cand_Tw_Num = Data["Candidato"].value_counts().values.tolist()[0]
        Esp_Tw = Data["Espacio"].value_counts().index.tolist()[0]
        Esp_Tw_Num = Data["Espacio"].value_counts().values.tolist()[0]
        Cand_Rel = Data.groupby("Candidato").mean()["Relevancia"].sort_values(ascending=False).index.tolist()[0]
        Cand_Rel_Num = Data.groupby("Candidato").mean()["Relevancia"].sort_values(ascending=False).values.tolist()[0]
        Esp_Rel = Data.groupby("Espacio").mean()["Relevancia"].sort_values(ascending=False).index.tolist()[0]
        Esp_Rel_Num = Data.groupby("Espacio").mean()["Relevancia"].sort_values(ascending=False).values.tolist()[0]



        return render_template('Home.html',Texto_semana=Texto_semana,Nombre_semana=Nombre_semana,Usr=Usr_Sem,
                               Url=Url_Sem,Fecha_Sem=Fecha_Sem,Likes_Sem=Likes_Sem,
                               Rt_Sem=Rt_Sem,
                               Citas_Sem=Citas_Sem,
                               Cand_Tw=Cand_Tw,Cand_Tw_Num=Cand_Tw_Num,
                               Esp_Tw=Esp_Tw,Esp_Tw_Num=Esp_Tw_Num,
                               Cand_Rel=Cand_Rel,Cand_Rel_Num=round(Cand_Rel_Num,1),
                               Esp_Rel=Esp_Rel,Esp_Rel_Num=round(Esp_Rel_Num,1))


    # Ruta para consultar : http://localhost:5000//results?Nombrecandidato
    @app.route("/results") 
    def search(): 

        args = request.args # Recibe los argumentos que tiene la url al realizar la query
        query_values = args.to_dict() # Convierto los argumentos en el tipo de dato 'dict'

        if list(query_values.keys())[0] == "Massa":
            Nombre = "Sergio Tomás Massa"
        elif list(query_values.keys())[0] == "Grabois":
            Nombre = "Juan Grabois"
        elif list(query_values.keys())[0] == "Kicillof":
            Nombre = "Axel Kicillof"
        elif list(query_values.keys())[0] == "Larreta":
            Nombre = "Horacio Rodriguez Larreta"
        elif list(query_values.keys())[0] == "Bullrich":
            Nombre = "Patricia Bullrich"
        elif list(query_values.keys())[0] == "Vidal":
            Nombre = "María Eugenia Vidal"
        elif list(query_values.keys())[0] == "Bregman":
            Nombre = "Myriam Bregman"
        elif list(query_values.keys())[0] == "Solano":
            Nombre = "Gabriel Solano"
        elif list(query_values.keys())[0] == "DelCaño":
            Nombre = "Nicolas Del Caño"
        elif list(query_values.keys())[0] == "Villarruel":
            Nombre = "Victoria Villarruel"
        elif list(query_values.keys())[0] == "Espert":
            Nombre = "José Luis Espert"
        elif list(query_values.keys())[0] == "Marra":
            Nombre = "Ramiro Marra"
        else:
            Nombre = "Error!"
        Data = pd.read_csv("../Data/Tweets.csv")
        Data = Data[Data["Candidato"]==list(query_values.keys())[0]]
        Twitts=len(Data)
        Citas = Data["Veces citado"].sum()
        ReTweets = Data["Cantidad de retweets"].sum()
        Likes = Data["Cantidad de Likes"].sum()
        
        return render_template('Candidato.html',Candidato=list(query_values.keys())[0],Nombre=Nombre,Twitts=Twitts,
                               Citas=Citas, ReTweets = ReTweets, Likes=Likes)

    app.run(debug=True, host='0.0.0.0', port=5000) # Ejecución del servidor/API


