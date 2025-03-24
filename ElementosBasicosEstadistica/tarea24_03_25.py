import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

archivo_proyecto = pd.read_excel("ElementosBasicosEstadistica/proyecto1.xlsx")
archivo_suc = pd.read_excel("ElementosBasicosEstadistica/Catalogo_sucursal.xlsx")

print("1. Ventas totales del comercio: ", archivo_proyecto["ventas_tot"].sum())

adeudo_counts = archivo_proyecto['B_adeudo'].value_counts()
adeudo_porcentajes = (adeudo_counts / adeudo_counts.sum()) * 100

print("2. Porcentaje de adeudos ", adeudo_porcentajes)


columnas = ['ventas_tot']