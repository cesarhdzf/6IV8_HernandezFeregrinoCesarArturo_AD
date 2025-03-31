"""Calcularemos las distancias entre todos los pares de puntos y determinaremos
cuales estan mas alejados entre si y cuales estan mas cercanos utilizando las distancias 
Euclidiana, Manhattan y Chebyshev
"""

import numpy as np
import pandas as pd
from scipy.spatial import distance

puntos={
    'Punto A' :(2,3),
    'Punto B' :(5,4),
    'Punto C' :(1,1),
    'Punto D' :(6,7),
    'Punto E' :(3,5),
    'Punto F' :(8,2),
    'Punto G' :(4,6),
    'Punto H' :(2,1)
}

#Converti los puntos a un DataFrame
df_puntos=pd.DataFrame(puntos).T
df_puntos.columns=['X','Y']
print("Coordenadas de los puntos: ")
print(df_puntos)

def calcular_distancias(puntos):
    distancias=pd.DataFrame(index=df_puntos.index, columns=df_puntos.index)
    #Calculo de distancias
    for i in df_puntos.index:
        for j in df_puntos.index:
            if i!=j: #No calcula la distancia del mismo punto
                #Distancia euclidiana
                distancias.loc[i,j]=distance.euclidean(df_puntos.loc[i], df_puntos.loc[j])

    return distancias

distancias=calcular_distancias(puntos)
valor_maximo=distancias.values.max()
(punto1,punto2)=distancias.stack().idxmax()

print("Tabla de distancias")
print(distancias)
print("Distancia maxima: ",valor_maximo)
print("Entre el punto ", punto1, "; y el punto ", punto2)

#Otra manera
max_value=distancias.max().max()
#Obtener la columna que contiene el valor maximo
col_max=distancias.max().idxmax()

#Obtener el indice (fila) que contiene el valor maximo
id_max=distancias[col_max].idxmax()

print(f"Valor maximo: {max_value}")
print(f"Columna: {col_max}")
print(f"Indice: {id_max}")