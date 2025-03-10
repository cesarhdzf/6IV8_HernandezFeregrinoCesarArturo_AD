import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ElementosBasicosEstadistica/housing.csv')

#Mostrar las primeras 5 filas 
print(df.head())

#Mostrar las ultimas 5 filas
print(df.tail())

#Mostrar fila en especifico
print(df.iloc[7])

#Mostrar la columna "ocean_proximity"
print(df["ocean_proximity"])

#Obtener la media de la columna "total_rooms"
mediadecuarto = df["total_rooms"].mean()
print('La media de total de rooms es: ' ,mediadecuarto)

#Obtener la mediana
medianadecuarto = df['median_house_value'].median()
print('La mediana de total de rooms es: ' ,medianadecuarto)

#La suma popular
salariototal = df['population'].sum()
print('El salario total es de: ', salariototal)

#para poder filtrar
vamoshacerunfiltro = df[df['ocean_proximity'] == 'ISLAND']
print(vamoshacerunfiltro)

#Vamos a hacer un grafico de dispersion
plt.scatter(df['ocean_proximity'][:10], df['median_house_value'][:10])
#nombramos los ejes
plt.xlabel("Proximidad")
plt.ylabel("Precio")

plt.title("Grafico de Dispersion de Proximidad al Oceano vs Precio")
plt.show()