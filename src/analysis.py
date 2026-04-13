import pandas as pd
import matplotlib.pyplot as plt

df_homicidios = pd.read_csv('data\\homicidios-UF.csv', sep=";", encoding='utf-8')

print(df_homicidios.head())

#Possiveis analises
#Estados com mais homicidios por ano
#Evolução dos homicidios por estado a cada ano 
#Estados com menos homicidios por ano