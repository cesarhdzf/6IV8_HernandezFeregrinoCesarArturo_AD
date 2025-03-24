import numpy as np
import matplotlib.pyplot as plt

#vamos a crear una semilla random para reproductividad
np.random.seed(0)

#vamos a buscar los parametros para una distribucion
#media
media = 0
#desviaciones estandar 
sigma1 = 1
sigma2 = 2
sigma3 = 3

#el numero de muestras para el analisis
n_muestras = 1000

#vamos a generar los datos de las distribuciones normales
datos1 = np.random.normal(media, sigma1, n_muestras)
datos2 = np.random.normal(media, sigma2, n_muestras)
datos3 = np.random.normal(media, sigma3, n_muestras)

# Graficamos los histogramas
plt.figure(figsize=(10, 6))

#para que sirve un histograma?
#para representar frecuencias en barras

#vamos a cargar las frecuencias a partir de una grafica de histogramas
plt.hist(datos1, bins=30, color='blue', density=True, label='Desviacion estandar = 1', alpha=0.5)
plt.hist(datos2, bins=30, color='red', density=True, label='Desviacion estandar = 2', alpha=0.5)
plt.hist(datos3, bins=30, color='green', density=True, label='Desviacion estandar = 3', alpha=0.5)
plt.title('Comparación de distribuciones normales con una semillla random')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.legend()
plt.grid()

plt.show()