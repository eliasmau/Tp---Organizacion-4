import pandas as pd
import matplotlib.pyplot as plt

# Leer datos
df = pd.read_csv("datos/ventas_empresa.csv")
df['total'] = df['cantidad'] * df['precio']

# Calcular totales
reporte = df.groupby('producto')['total'].sum()

# Guardar gráfico
reporte.plot(kind='bar', color='blue')
plt.title("Ventas por Producto")
plt.savefig("resultados/grafico_ventas.png")
print("Análisis completado: Gráfico guardado.")
