# ========================
# Análisis del PIB Mundial (Filtrado: Colombia)
# ========================

# Importamos las librerías necesarias
import pandas as pd              # Para manipulación y análisis de datos
import seaborn as sns            # Para realizar gráficos estadísticos atractivos
import matplotlib.pyplot as plt  # Para crear y mostrar gráficos

# ========================
# 1. Cargar el dataset
# ========================

# URL oficial del dataset del PIB mundial (fuente: Banco Mundial)
url = "https://raw.githubusercontent.com/datasets/gdp/master/data/gdp.csv"

# Cargar los datos del archivo CSV directamente desde la URL
df = pd.read_csv(url)

# Mostrar las primeras filas del dataset original para inspección inicial
print("===== PRIMERAS FILAS DEL DATASET GLOBAL =====")
print(df.head(), "\n")  # head() muestra las primeras 5 filas del DataFrame

# ========================
# 2. Filtrar los datos solo de Colombia
# ========================

# Filtrar las filas del DataFrame donde el país sea "Colombia"
colombia = df[df["Country Name"] == "Colombia"].copy()  # .copy() evita advertencias de asignación

# Mostrar el registro de los datos filtrados de Colombia
print("===== DATOS DE COLOMBIA =====")
print(colombia.head(), "\n")

# ========================
# 3. Limpieza y conversión de datos
# ========================

# Convertimos las columnas de texto a formato numérico
colombia["Año"] = pd.to_numeric(colombia["Year"], errors="coerce")       # Convierte el año a número
colombia["PIB (USD)"] = pd.to_numeric(colombia["Value"], errors="coerce")  # Convierte el PIB a número

# ========================
# 4. Medidas de tendencia central y dispersión
# ========================

# Cálculo de medidas estadísticas descriptivas
media = colombia["PIB (USD)"].mean()      # Promedio de los valores del PIB
mediana = colombia["PIB (USD)"].median()  # Valor central del PIB
moda = colombia["PIB (USD)"].mode()[0]    # Valor más frecuente del PIB
rango = colombia["PIB (USD)"].max() - colombia["PIB (USD)"].min()  # Diferencia entre el PIB máximo y mínimo
varianza = colombia["PIB (USD)"].var()    # Varianza (dispersión cuadrática)
desviacion = colombia["PIB (USD)"].std()  # Desviación estándar (dispersión promedio)
coef_variacion = (desviacion / media) * 100  # Medida de variabilidad relativa (porcentaje)

# Mostrar los resultados estadísticos en consola
print("===== MEDIDAS DE TENDENCIA CENTRAL Y DISPERSIÓN =====")
print(f"Media: {media:,.2f} USD")
print(f"Mediana: {mediana:,.2f} USD")
print(f"Moda: {moda:,.2f} USD")
print(f"Rango: {rango:,.2f} USD")
print(f"Varianza: {varianza:,.2f}")
print(f"Desviación estándar: {desviacion:,.2f}")
print(f"Coeficiente de variación: {coef_variacion:.2f}%\n")

# ========================
# 5. Calcular tasa de crecimiento porcentual
# ========================

# Calcular el porcentaje de variación del PIB respecto al año anterior
colombia["Crecimiento (%)"] = colombia["PIB (USD)"].pct_change() * 100  # pct_change calcula el cambio relativo

# ========================
# 6. Visualizaciones con Seaborn
# ========================

# Configurar el estilo visual de los gráficos
sns.set_theme(style="whitegrid", palette="crest")

# --- Gráfico 1: Evolución del PIB ---
plt.figure(figsize=(10, 5))  # Tamaño del gráfico
sns.lineplot(data=colombia, x="Año", y="PIB (USD)", marker="o")  # Línea con puntos
plt.title("Evolución del PIB de Colombia (1960–2023)", fontsize=14)  # Título
plt.xlabel("Año")  # Etiqueta del eje X
plt.ylabel("PIB Nominal (en dólares estadounidenses)")  # Etiqueta del eje Y
plt.tight_layout()  # Ajustar el espacio para que no se sobrepongan los textos
plt.show()  # Mostrar gráfico

# --- Gráfico 2: Crecimiento porcentual anual ---
plt.figure(figsize=(10, 5))
sns.barplot(data=colombia, x="Año", y="Crecimiento (%)", color="teal")  # Barras en color verde azulado
plt.title("Tasa de Crecimiento Anual del PIB (%)", fontsize=14)
plt.xlabel("Año")
plt.ylabel("Crecimiento anual (%)")
plt.xticks(rotation=90)  # Rotar etiquetas para que no se encimen
plt.tight_layout()
plt.show()

# --- Gráfico 3: Distribución del PIB ---
plt.figure(figsize=(8, 5))
sns.histplot(data=colombia, x="PIB (USD)", bins=15, kde=True, color="purple")  # Histograma + curva de densidad
plt.title("Distribución del PIB de Colombia (1960–2023)", fontsize=14)
plt.xlabel("PIB (USD)")
plt.ylabel("Frecuencia")  # Número de veces que se repite un rango de PIB
plt.tight_layout()
plt.show()

# --- Gráfico 4: Boxplot del PIB ---
plt.figure(figsize=(6, 5))
sns.boxplot(data=colombia, y="PIB (USD)", color="orange")  # Caja de distribución del PIB
plt.title("Distribución y valores atípicos del PIB", fontsize=14)
plt.ylabel("PIB (USD)")
plt.tight_layout()
plt.show()

# --- Gráfico 5: Dispersión del crecimiento ---
plt.figure(figsize=(10, 5))
sns.scatterplot(
    data=colombia,
    x="Año",
    y="Crecimiento (%)",
    hue="Crecimiento (%)",      # Color según la magnitud del crecimiento
    size="Crecimiento (%)",     # Tamaño del punto según el valor
    palette="coolwarm",         # Paleta azul (bajo crecimiento) - roja (alto crecimiento)
    sizes=(50, 250)             # Rango de tamaños de los puntos
)
plt.title("Relación entre el año y el crecimiento del PIB (%)", fontsize=14)
plt.xlabel("Año")
plt.ylabel("Crecimiento anual (%)")
plt.tight_layout()
plt.show()

# ========================
# 7. Conclusiones automáticas
# ========================

# Identificar el mayor y menor crecimiento, y los años en que ocurrieron
crec_max = colombia["Crecimiento (%)"].max()   # Valor máximo del crecimiento
crec_min = colombia["Crecimiento (%)"].min()   # Valor mínimo (caída)
anio_max = int(colombia.loc[colombia["Crecimiento (%)"].idxmax(), "Año"])  # Año del crecimiento máximo
anio_min = int(colombia.loc[colombia["Crecimiento (%)"].idxmin(), "Año"])  # Año del crecimiento mínimo

# Mostrar conclusiones automáticas basadas en los cálculos
print("===== CONCLUSIONES =====")
print(f"El mayor crecimiento se presentó en el año {anio_max} con una tasa de {crec_max:.2f}%.")
print(f"La mayor caída del PIB ocurrió en el año {anio_min} con una variación de {crec_min:.2f}%.")
print(f"El PIB promedio entre 1960 y 2023 fue de {media:,.2f} USD.")
print(f"La dispersión (desviación estándar) indica una variabilidad de {desviacion:,.2f} USD entre los años analizados.")
