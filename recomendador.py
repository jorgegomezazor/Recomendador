import pandas as pd
import re
def extract(pelis): #Leo el archivo
    df = pd.read_csv(pelis) 
    df.drop(columns=['tconst','isAdult','originalTitle','startYear','endYear','runtimeMinutes'], inplace=True) #Elimino columnas innecesarias
    return df
def transform(pelis, genero):
    pelis['genero'] = pelis['genres'].apply(lambda x: re.findall(genero, x)) #Busco el genero en la columna genres
    salida = pelis[pelis['genero'].apply(lambda x: len(x) > 0)] #Filtro las peliculas que tienen el genero
    peli_recomendada = salida['primaryTitle'].sample().values[0] #Elijo una pelicula al azar
    return peli_recomendada
def load(pelis):
    print(pelis) #Imprimo la pelicula recomendada
if __name__ == '__main__':
    pelis = 'title.basics.csv'
    fichero = extract(pelis)
    genero = input('Indique el género que quiera ver: ')
    peli_recomendada = transform(fichero, genero)
    load(peli_recomendada)
