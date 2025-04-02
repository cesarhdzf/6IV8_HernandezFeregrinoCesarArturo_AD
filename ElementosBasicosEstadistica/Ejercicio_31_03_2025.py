"""Calcularemos las distancias entre todos los pares de puntos y determinaremos
cuales estan mas alejados entre si y cuales estan mas cercanos utilizando las distancias 
Euclidiana, Manhattan y Chebyshev
"""
import numpy as np
import pandas as pd
from scipy.spatial import distance

puntos = {
    'Punto A': (2, 3),
    'Punto B': (5, 4),
    'Punto C': (1, 1),
    'Punto D': (6, 7),
    'Punto E': (3, 5),
    'Punto F': (8, 2),
    'Punto G': (4, 6),
    'Punto H': (2, 1)
}

# Convertir los puntos a un DataFrame
df_puntos = pd.DataFrame(puntos).T
df_puntos.columns = ['X', 'Y']
print("Coordenadas de los puntos:")
print(df_puntos, "\n")

def calcular_distancias(puntos_df):
    dist_eu = pd.DataFrame(index=puntos_df.index, columns=puntos_df.index, dtype=float)
    dist_mh = pd.DataFrame(index=puntos_df.index, columns=puntos_df.index, dtype=float)
    dist_ch = pd.DataFrame(index=puntos_df.index, columns=puntos_df.index, dtype=float)

    for i in puntos_df.index:
        for j in puntos_df.index:
            if i != j:
                dist_eu.loc[i, j] = distance.euclidean(puntos_df.loc[i], puntos_df.loc[j])
                dist_mh.loc[i, j] = distance.cityblock(puntos_df.loc[i], puntos_df.loc[j])
                dist_ch.loc[i, j] = distance.chebyshev(puntos_df.loc[i], puntos_df.loc[j])
            else:
                dist_eu.loc[i, j] = 0.0
                dist_mh.loc[i, j] = 0.0
                dist_ch.loc[i, j] = 0.0

    return dist_eu, dist_mh, dist_ch

# Calcular distancias
dist_eu, dist_mh, dist_ch = calcular_distancias(df_puntos)

# Función para imprimir info de distancia máxima y mínima
def imprimir_extremos(nombre, matriz):
    max_val = matriz.max().max()
    min_val = matriz.replace(0, np.nan).min().min()  # evitar diagonales
    max_pair = matriz.stack().idxmax()
    min_pair = matriz.replace(0, np.nan).stack().idxmin()

    print(f"\nDistancia {nombre}:")
    print(matriz.round(2))
    print(f"Mayor distancia: {max_val:.2f} entre {max_pair}")
    print(f"Menor distancia (≠0): {min_val:.2f} entre {min_pair}")

# Imprimir resultados
imprimir_extremos("Euclidiana", dist_eu)
imprimir_extremos("Manhattan", dist_mh)
imprimir_extremos("Chebyshev", dist_ch)

# Otra manera de encontrar el valor máximo (comentado por el profesor Armando)
# -----------------------------------------------
print("\n# Otra manera (comentado por el Profesor Armando):")
max_value = dist_eu.max().max()
col_max = dist_eu.max().idxmax()
id_max = dist_eu[col_max].idxmax()

print(f"Valor máximo (otra manera): {max_value:.2f}")
print(f"Columna (punto destino): {col_max}")
print(f"Índice (punto origen): {id_max}")
print(f"Par con distancia máxima: ({id_max}, {col_max})")