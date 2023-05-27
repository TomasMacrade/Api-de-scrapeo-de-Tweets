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

#import matplotlib.pyplot as plt



# Buscamos todos los tweets entre hoy y una semana para atrás, entonces guardamos variables con estas fechas
Hoy = datetime.date.today() + datetime.timedelta(days=1)
Una_Semana = Hoy - datetime.timedelta(days=8)

# Usamos TwitterSearchScraper para recoger la información de los tweets de un usario y meterlo en la lista

# Nombres candidatos
Candidatos = [("DelCaño","NicolasdelCano","FIT"),("Villarruel","VickyVillarruel","LLA"),("Vidal","mariuvidal","JxC"),("Kicillof","Kicillofok","FdT"),("Marra","RAMIROMARRA","LLA"),("Espert","jlespert","LLA"),("Bullrich","PatoBullrich","JxC"),("Larreta","horaciorlarreta","JxC"),("Grabois","JuanGrabois","FdT"),("Massa","SergioMassa","FdT"),("Bregman","myriambregman","FIT"),("Solano","Solanopo","FIT")]

# Buscamos los tweets de cada candidato
for x in Candidatos:
    informacion = [[tweet.date - datetime.timedelta(hours=3), tweet.likeCount, tweet.retweetCount,tweet.quoteCount, tweet.rawContent,tweet.url,x[0],x[2]] for tweet in sntwitter.TwitterSearchScraper('from:{} since:{} until:{}'.format(x[1],Una_Semana,Hoy)).get_items()]
    globals()['tweets_df_' + x[0]] = pd.DataFrame(informacion, columns=["Fecha-Hora", "Cantidad de Likes", "Cantidad de retweets","Veces citado", "Tweet","url","Candidato","Espacio"])
# Organizamos todo dentro de un dataframe
frames = [tweets_df_DelCaño,tweets_df_Villarruel,tweets_df_Vidal,tweets_df_Kicillof,tweets_df_Espert,tweets_df_Marra,tweets_df_Bullrich,tweets_df_Bregman,tweets_df_Grabois,tweets_df_Larreta,tweets_df_Massa,tweets_df_Solano]
final = pd.concat(frames)

# Guardamos el dataframe como .csv
final.to_csv('/opt/airflow/Data/Tweets.csv',index=False)  
