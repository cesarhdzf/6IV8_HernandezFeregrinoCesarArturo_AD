import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel("ElementosBasicosEstadistica/proyecto1.xlsx")
sucursales = pd.read_excel("ElementosBasicosEstadistica/Catalogo_sucursal.xlsx")

for i in range(len(df)):
    for j in range(len(sucursales)):
        if df.loc[i, "id_sucursal"] == sucursales.loc[j, "id_sucursal"]:
            df.loc[i, "suc"] = sucursales.loc[j, "suc"]

# 1. Ventas totales
ventas_totales = df["ventas_tot"].sum()
print("1. Ventas totales del comercio: $", ventas_totales)

# 2. Socios con/sin adeudo
con_adeudo = 0
sin_adeudo = 0
for i in range(len(df)):
    if df.loc[i, "B_adeudo"] == "Con adeudo":
        con_adeudo += 1
    elif df.loc[i, "B_adeudo"] == "Sin adeudo":
        sin_adeudo += 1

total_socios = con_adeudo + sin_adeudo
porc_con = (con_adeudo / total_socios) * 100
porc_sin = (sin_adeudo / total_socios) * 100

print("2. Socios con adeudo:", con_adeudo, f"({porc_con}%)")
print("   Socios sin adeudo:", sin_adeudo, f"({porc_sin}%)")

# 3. Ventas por mes
df["B_mes"] = pd.to_datetime(df["B_mes"])
df["mes_str"] = df["B_mes"].dt.to_period("M").astype(str)

meses = []
for i in range(len(df)):
    mes = df.loc[i, "mes_str"]
    if mes not in meses:
        meses.append(mes)
meses.sort()

ventas_por_mes = []
for mes in meses:
    total = 0
    for i in range(len(df)):
        if df.loc[i, "mes_str"] == mes:
            total += df.loc[i, "ventas_tot"]
    ventas_por_mes.append(total)

plt.figure(figsize=(12, 6))
plt.bar(meses, ventas_por_mes, color="skyblue", width=0.6)
plt.title("Ventas Totales por Mes")
plt.xlabel("Mes")
plt.ylabel("Ventas")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 4. Desviación estándar de pagos por mes
desviaciones = []
for mes in meses:
    pagos = []
    for i in range(len(df)):
        if df.loc[i, "mes_str"] == mes:
            pagos.append(df.loc[i, "pagos_tot"])
    pagos_array = np.array(pagos)
    std = pagos_array.std()
    desviaciones.append(std)

plt.figure(figsize=(12, 6))
plt.bar(meses, desviaciones, color="orange", width=0.6)
plt.title("Desviación Estándar de Pagos por Mes")
plt.xlabel("Mes")
plt.ylabel("Desviación Estándar")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 5. Deuda total
deuda_total = df["adeudo_actual"].sum()
print("5. Deuda total de clientes: $", deuda_total)

# 6. Porcentaje de utilidad
utilidad = ventas_totales - deuda_total
porcentaje_utilidad = (utilidad / ventas_totales) * 100
print("6. Porcentaje de utilidad del comercio:", porcentaje_utilidad, "%")

# 7. Gráfico circular de ventas por sucursal
sucs = []
ventas_suc = []

for i in range(len(df)):
    suc = df.loc[i, "suc"]
    if suc not in sucs:
        sucs.append(suc)

for suc in sucs:
    total = 0
    for i in range(len(df)):
        if df.loc[i, "suc"] == suc:
            total += df.loc[i, "ventas_tot"]
    ventas_suc.append(total)

plt.figure(figsize=(8, 8))
colores = plt.cm.tab20.colors
plt.pie(ventas_suc, labels=sucs, autopct='%1.1f%%', startangle=90, colors=colores[:len(sucs)])
plt.title("Ventas por Sucursal")
plt.tight_layout()
plt.show()

# 8. Deuda vs Margen de utilidad como barras lado a lado
deuda_suc = []
margen_utilidad = []

for suc in sucs:
    ventas = 0
    deuda = 0
    for i in range(len(df)):
        if df.loc[i, "suc"] == suc:
            ventas += df.loc[i, "ventas_tot"]
            deuda += df.loc[i, "adeudo_actual"]
    deuda_millones = deuda / 1_000_000
    deuda_suc.append(deuda_millones)

    if ventas > 0:
        margen = ((ventas - deuda) / ventas) * 100
    else:
        margen = 0
    margen_utilidad.append(margen * 0.035)

x = np.arange(len(sucs))
width = 0.4

plt.figure(figsize=(12, 6))
plt.bar(x - width/2, deuda_suc, width=width, color="red", label="Deuda Total (millones)", alpha=0.7)
plt.bar(x + width/2, margen_utilidad, width=width, color="green", label="Margen Utilidad (% x 0.035)", alpha=0.7)
plt.xticks(x, sucs, rotation=45)
plt.ylabel("Escala visual (millones)")
plt.title("Deuda Total vs Margen de Utilidad por Sucursal (barras comparadas)")
plt.legend()
plt.tight_layout()
plt.show()