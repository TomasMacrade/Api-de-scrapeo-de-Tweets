# Requisitos

# snscrape
# pip install snscrape

import snscrape.modules.twitter as sntwitter

# Pandas
# pip install pandas

import pandas as pd

# datetime

import datetime

# Matplotlib
# pip install  matplotlib

import matplotlib.pyplot as plt

# psycopg2
import psycopg2 
import psycopg2.extras

#Me conecto a la base
conn = psycopg2.connect(dbname="tweets", user="postgres", host="host.docker.internal", password="airflow")

# Abro el cursor
cur = conn.cursor()

# Ejecuto la Qry
cur.execute("SELECT * FROM Candidatos join Espacio on Candidatos.Espacio = Espacio.ID")

# Me guardo el resultado
Qry = cur.fetchall()

conn.commit()

# Nombres candidatos
Candidatos = []
for row in Qry:
    Candidatos.append((row[2].replace(" ",""),row[4],row[-1]))




# Buscamos todos los tweets entre hoy y una semana para atrás, entonces guardamos variables con estas fechas
Hoy = datetime.date.today() + datetime.timedelta(days=1)
Ayer = datetime.date.today() - datetime.timedelta(days=1)
Una_Semana = Hoy - datetime.timedelta(days=8)

# Usamos TwitterSearchScraper para recoger la información de los tweets de un usario y meterlo en la lista


#Candidatos = [("DelCaño","NicolasdelCano","FIT"),("Villarruel","VickyVillarruel","LLA"),("Vidal","mariuvidal","JxC"),("Kicillof","Kicillofok","FdT"),("Marra","RAMIROMARRA","LLA"),("Espert","jlespert","LLA"),("Bullrich","PatoBullrich","JxC"),("Larreta","horaciorlarreta","JxC"),("Grabois","JuanGrabois","FdT"),("Massa","SergioMassa","FdT"),("Bregman","myriambregman","FIT"),("Solano","Solanopo","FIT")]



# Buscamos los tweets de cada candidato
for x in Candidatos:
    informacion = [[tweet.date - datetime.timedelta(hours=3), tweet.likeCount, tweet.retweetCount,tweet.quoteCount, tweet.rawContent,x[0],x[2],x[1],tweet.url] for tweet in sntwitter.TwitterSearchScraper('from:{} since:{} until:{}'.format(x[1],Una_Semana,Hoy)).get_items()]
    globals()['tweets_df_' + x[0]] = pd.DataFrame(informacion, columns=["Fecha-Hora", "Cantidad de Likes", "Cantidad de retweets","Veces citado", "Tweet","Candidato","Espacio","Usr","url"])
# Organizamos todo dentro de un dataframe
frames = [tweets_df_DelCaño,tweets_df_Villarruel,tweets_df_Vidal,tweets_df_Kicillof,tweets_df_Espert,tweets_df_Marra,tweets_df_Bullrich,tweets_df_Bregman,tweets_df_Grabois,tweets_df_Larreta,tweets_df_Massa,tweets_df_Solano]
final = pd.concat(frames)


# Guardamos el dataframe como .csv
final.to_csv('/opt/airflow/Data/Tweets.csv',index=False)  

final["Candidato"] = [0 if i == "DelCaño" else
 1 if i == "Villarruel" else
  2 if i == "Vidal" else
  3 if i == "Kicillof" else
  4 if i == "Marra" else
  5 if i == "Espert" else
  6 if i =="Bullrich" else
  7 if i == "Larreta" else
  8 if i == "Grabois" else
  9 if i == "Massa" else
  10 if i == "Bregman" else
  11 
  for i in final["Candidato"]]

final["Fecha-Hora"] = [str(i)[0:19] for i in final["Fecha-Hora"]]


# Veo si la tabla de tweets está vacía
cur.execute("select * from tweets")

cant = cur.fetchall()

conn.commit()

if len(cant)==0:
    # Si está vacía la lleno con todo lo que tengo

    diccionario = final.to_dict("record")

    psycopg2.extras.execute_batch(cur, """
                INSERT INTO Tweets (ID_Candidato ,
                Texto ,
                Rt ,
                Citas ,
                Likes ,
                FechaHora ,
                URL ) VALUES (
                    %(Candidato)s,
                    %(Tweet)s,
                    %(Cantidad de retweets)s,
                    %(Veces citado)s,
                    %(Cantidad de Likes)s,
                    %(Fecha-Hora)s,
                    %(url)s
                );
            """, diccionario)
    conn.commit()

else:

    # Si no, le cargo solo la data del último día
    final["Fecha"] = [i[:10] for i in final["Fecha-Hora"]]
    print(final["Fecha"])
    print(Ayer)
    final = final[final["Fecha"] == str(Ayer) ]
    print(len(final))
    diccionario = final.to_dict("record")
    psycopg2.extras.execute_batch(cur, """
                INSERT INTO Tweets (ID_Candidato ,
                Texto ,
                Rt ,
                Citas ,
                Likes ,
                FechaHora ,
                URL ) VALUES (
                    %(Candidato)s,
                    %(Tweet)s,
                    %(Cantidad de retweets)s,
                    %(Veces citado)s,
                    %(Cantidad de Likes)s,
                    %(Fecha-Hora)s,
                    %(url)s
                );
            """, diccionario)

    conn.commit()


##### IMAGENES ##############
final = pd.read_csv("/opt/airflow/Data/Tweets.csv")
# Tweets por semana por candidato

Tw_x_Candidato =  final["Candidato"].value_counts().sort_values()

# Ploteo

with plt.style.context('fivethirtyeight'):
    for i in range(len(Tw_x_Candidato.index.tolist())):
        if Tw_x_Candidato.index.tolist()[i] in ["Bullrich","Larreta","Vidal"]:
            plt.barh(Tw_x_Candidato.index.tolist()[i], Tw_x_Candidato.values.tolist()[i], color ='Yellow',edgecolor='Black')
        elif Tw_x_Candidato.index.tolist()[i] in ["Massa","Grabois","Kicillof"]:
            plt.barh(Tw_x_Candidato.index.tolist()[i], Tw_x_Candidato.values.tolist()[i], color ='Blue',edgecolor='Black')
        elif Tw_x_Candidato.index.tolist()[i] in ["Solano","Bregman","DelCaño"]:
            plt.barh(Tw_x_Candidato.index.tolist()[i], Tw_x_Candidato.values.tolist()[i], color ='Red',edgecolor='Black')
        else:
            plt.barh(Tw_x_Candidato.index.tolist()[i], Tw_x_Candidato.values.tolist()[i], color ='Purple',edgecolor='Black')

    for i in range(len(Tw_x_Candidato.index.tolist())):
        plt.text(x = Tw_x_Candidato.values.tolist()[i]+2 , y = Tw_x_Candidato.index.tolist()[i], s = Tw_x_Candidato.values.tolist()[i], size = 10,va='center')
    plt.ylabel("Candidato")
    plt.xlabel("Cantidad de Tweets")
    plt.title("Tweets por candidato en la última semana")
    plt.savefig('/opt/airflow/Flask/app/static/TxC.png', bbox_inches='tight')
    plt.clf()


# Tweets por semana por espacio

Tw_x_Candidato =  final["Espacio"].value_counts().sort_values()

# Ploteo

with plt.style.context('fivethirtyeight'):
    for i in range(len(Tw_x_Candidato.index.tolist())):
        if Tw_x_Candidato.index.tolist()[i] in ["JxC"]:
            plt.barh(Tw_x_Candidato.index.tolist()[i], Tw_x_Candidato.values.tolist()[i], color ='Yellow',edgecolor='Black')
        elif Tw_x_Candidato.index.tolist()[i] in ["FdT"]:
            plt.barh(Tw_x_Candidato.index.tolist()[i], Tw_x_Candidato.values.tolist()[i], color ='Blue',edgecolor='Black')
        elif Tw_x_Candidato.index.tolist()[i] in ["FIT"]:
            plt.barh(Tw_x_Candidato.index.tolist()[i], Tw_x_Candidato.values.tolist()[i], color ='Red',edgecolor='Black')
        else:
            plt.barh(Tw_x_Candidato.index.tolist()[i], Tw_x_Candidato.values.tolist()[i], color ='Purple',edgecolor='Black')

    for i in range(len(Tw_x_Candidato.index.tolist())):
        plt.text(x = Tw_x_Candidato.values.tolist()[i]+2 , y = Tw_x_Candidato.index.tolist()[i],va='center', s = Tw_x_Candidato.values.tolist()[i], size = 10)
    plt.ylabel("Espacio")
    plt.xlabel("Cantidad de Tweets")
    plt.title("Tweets por espacio en la última semana")
    plt.savefig('/opt/airflow/Flask/app/static/TxE.png', bbox_inches='tight')
    plt.clf()


# (Mg promedio + Rt promedio + Citas promedio)/3 por candidato 

tw = final.groupby("Candidato").mean()
tw["Tot"] = (tw["Cantidad de Likes"] + tw["Cantidad de retweets"] + tw["Veces citado"])/3
Tw_x_Candidato = tw["Tot"].round(1).sort_values()
# Ploteo

with plt.style.context('fivethirtyeight'):
    for i in range(len(Tw_x_Candidato.index.tolist())):
        if Tw_x_Candidato.index.tolist()[i] in ["Bullrich","Larreta","Vidal"]:
            plt.barh(Tw_x_Candidato.index.tolist()[i], Tw_x_Candidato.values.tolist()[i], color ='Yellow',edgecolor='Black')
        elif Tw_x_Candidato.index.tolist()[i] in ["Massa","Grabois","Kicillof"]:
            plt.barh(Tw_x_Candidato.index.tolist()[i], Tw_x_Candidato.values.tolist()[i], color ='Blue',edgecolor='Black')
        elif Tw_x_Candidato.index.tolist()[i] in ["Solano","Bregman","DelCaño"]:
            plt.barh(Tw_x_Candidato.index.tolist()[i], Tw_x_Candidato.values.tolist()[i], color ='Red',edgecolor='Black')
        else:
            plt.barh(Tw_x_Candidato.index.tolist()[i], Tw_x_Candidato.values.tolist()[i], color ='Purple',edgecolor='Black')

    for i in range(len(Tw_x_Candidato.index.tolist())):
        plt.text(x = Tw_x_Candidato.values.tolist()[i]+10 , y = Tw_x_Candidato.index.tolist()[i], s = Tw_x_Candidato.values.tolist()[i], size = 12,va='center')
    plt.ylabel("Candidato")
    plt.xlabel("Índice de relevancia")
    plt.title("Relevancia por candidato en la última semana")
    plt.savefig('/opt/airflow/Flask/app/static/RxC.png', bbox_inches='tight')
    plt.clf()


# (Mg promedio + Rt promedio + Citas promedio)/3 por espacio

tw = final.groupby("Espacio").mean()
tw["Tot"] = (tw["Cantidad de Likes"] + tw["Cantidad de retweets"] + tw["Veces citado"])/3
Tw_x_Candidato = tw["Tot"].round(1).sort_values()
# Ploteo

with plt.style.context('fivethirtyeight'):
    for i in range(len(Tw_x_Candidato.index.tolist())):
        if Tw_x_Candidato.index.tolist()[i] in ["JxC"]:
            plt.barh(Tw_x_Candidato.index.tolist()[i], Tw_x_Candidato.values.tolist()[i], color ='Yellow',edgecolor='Black')
        elif Tw_x_Candidato.index.tolist()[i] in ["FdT"]:
            plt.barh(Tw_x_Candidato.index.tolist()[i], Tw_x_Candidato.values.tolist()[i], color ='Blue',edgecolor='Black')
        elif Tw_x_Candidato.index.tolist()[i] in ["FIT"]:
            plt.barh(Tw_x_Candidato.index.tolist()[i], Tw_x_Candidato.values.tolist()[i], color ='Red',edgecolor='Black')
        else:
            plt.barh(Tw_x_Candidato.index.tolist()[i], Tw_x_Candidato.values.tolist()[i], color ='Purple',edgecolor='Black')

    for i in range(len(Tw_x_Candidato.index.tolist())):
        plt.text(x = Tw_x_Candidato.values.tolist()[i]+2 , y = Tw_x_Candidato.index.tolist()[i],va='center', s = Tw_x_Candidato.values.tolist()[i], size = 12)
    plt.ylabel("Espacio")
    plt.xlabel("Índice de relevancia")
    plt.title("Relevancia por espacio en la última semana")
    plt.savefig('/opt/airflow/Flask/app/static/RxE.png', bbox_inches='tight')
    plt.clf()


# Actividad de los canidatos en la última semana
Normalizado = final
Normalizado["Fecha-Hora"]=pd.to_datetime(Normalizado["Fecha-Hora"]).dt.date

# Para cada candidato
for x in Candidatos:
     Aux = Normalizado[Normalizado["Candidato"]==x[0]]
     Aux = Aux["Fecha-Hora"].value_counts()
     if x[0] in ["Bullrich","Larreta","Vidal"]:
          c = "goldenrod"
     elif x[0] in ["Massa","Grabois","Kicillof"]:
          c = "blue"
     elif x[0] in ["Solano","Bregman","DelCaño"]:
          c= "red"
     else:
          c = "purple"
     with plt.style.context('fivethirtyeight'):
          Aux.plot(marker = "o",color = c,linestyle = "--")
          plt.ylabel("Candidato")
          plt.xlabel("Fecha")
          plt.xticks(rotation=50)
          plt.title("Cantidad de tweets de {} en la última semana".format(x[0]))
          plt.savefig('/opt/airflow/Flask/app/static/{}.png'.format(x[0]), bbox_inches='tight')
          plt.clf()
