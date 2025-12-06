import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------------------------------
# Cargar datos
# -----------------------------------------------------------
df = pd.read_csv("datos.csv")

# -----------------------------------------------------------
# Configuración general del sitio
# -----------------------------------------------------------
st.title("Análisis Interactivo de Horas de Luz en Cuatro Ciudades del Mundo")

st.write(
    """
    Este aplicativo permite analizar los datos de salida del sol, puesta del sol y duración del día
    registrados semanalmente para Santiago (Chile), Singapur, Tokio y Oslo.
    El objetivo es visualizar cómo varían estas horas a lo largo del año y compararlas entre países.
    """
)

st.write(
    """
    **Guía de uso:**
    - Use el primer selector para graficar *una* de las tres curvas (Salida, Puesta o Duración) para **todas** las ciudades.
    - Use el segundo selector para graficar **todas** las curvas simultáneamente (Salida, Puesta y Duración), pero solo para **una** ciudad seleccionada.
    """
)

# -----------------------------------------------------------
# Gráfico 1: Selección de curva para todas las ciudades
# -----------------------------------------------------------
st.subheader("Comparación entre ciudades para una variable")

opcion_var = st.selectbox(
    "Seleccione la variable a graficar:",
    ["Salida", "Puesta", "Duración"]
)

fig1, ax1 = plt.subplots(figsize=(10, 5))

for ciudad, color in zip(["Chile", "Singapur", "Tokio", "Oslo"], ["blue", "magenta", "gold", "red"]):
    df_ciudad = df[df["Ciudad"] == ciudad]
    ax1.plot(df_ciudad["Fecha"], df_ciudad[opcion_var], label=ciudad, color=color)

ax1.set_title(f"Curva de {opcion_var} para todas las ciudades")
az1 = ax1
ax1.set_xlabel("Fecha")
ax1.set_ylabel(f"{opcion_var} (h)")
ax1.legend()
plt.xticks(rotation=45)
st.pyplot(fig1)

# -----------------------------------------------------------
# Gráfico 2: Todas las curvas para una ciudad
# -----------------------------------------------------------
st.subheader("Curvas completas para una ciudad")

opcion_ciudad = st.selectbox(
    "Seleccione la ciudad a graficar:",
    ["Chile", "Singapur", "Tokio", "Oslo"]
)

fig2, ax2 = plt.subplots(figsize=(10, 5))

colores = {"Salida": "blue", "Puesta": "red", "Duración": "green"}

df_sel = df[df["Ciudad"] == opcion_ciudad]

for var in ["Salida", "Puesta", "Duración"]:
    ax2.plot(df_sel["Fecha"], df_sel[var], label=var, color=colores[var])

ax2.set_title(f"Curvas de Salida, Puesta y Duración para {opcion_ciudad}")
ax2.set_xlabel("Fecha")
ax2.set_ylabel("Horas (h)")
ax2.legend()
plt.xticks(rotation=45)

st.pyplot(fig2)
