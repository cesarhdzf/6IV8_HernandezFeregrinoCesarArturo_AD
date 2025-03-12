import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ElementosBasicosEstadistica/housing.csv")

df_subset = df.iloc[400:501].copy()

columnas = ['median_house_value', 'total_bedrooms', 'population']

estadisticas = {}

for col in columnas:
    media = df_subset[col].mean()
    mediana = df_subset[col].median()
    moda = df_subset[col].mode().iloc[0] if not df_subset[col].mode().empty else None
    rango_val = df_subset[col].max() - df_subset[col].min()
    varianza = df_subset[col].var()
    desviacion = df_subset[col].std()
    
    estadisticas[col] = {
        "Media": media,
        "Mediana": mediana,
        "Moda": moda,
        "Rango": rango_val,
        "Varianza": varianza,
        "Desviacion Estandar": desviacion
    }

df_estadisticas = pd.DataFrame(estadisticas).transpose()

bins = 10
df_subset['mhv_bins'] = pd.cut(df_subset['median_house_value'], bins=bins)
tabla_frecuencias = df_subset['mhv_bins'].value_counts().sort_index()

print("Estadísticas Descriptivas:")
print(df_estadisticas)
print("\nTabla de Frecuencias para 'median_house_value':")
print(tabla_frecuencias)

plt.figure(figsize=(8, 6))
plt.hist(df_subset['median_house_value'].dropna(), bins=20, edgecolor='black')
media_mhv = df_subset['median_house_value'].mean()
plt.axvline(media_mhv, color='red', linestyle='dashed', linewidth=1,
            label=f'Media: {media_mhv:.2f}')
plt.xlabel('median_house_value')
plt.ylabel('Frecuencia')
plt.title('Histograma de median_house_value (filas 400 a 500)')
plt.legend()
plt.show()

medias = [estadisticas[col]["Media"] for col in columnas]
plt.figure(figsize=(8, 6))
plt.bar(columnas, medias)
plt.ylabel('Valor Medio')
plt.title('Comparación de Medias: median_house_value, total_bedrooms, population')
for i, valor in enumerate(medias):
    plt.text(i, valor, f'{valor:.2f}', ha='center', va='bottom')
plt.show()