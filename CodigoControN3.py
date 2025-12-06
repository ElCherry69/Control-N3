import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("datos.csv")
df["Fecha"] = pd.to_datetime(df["Fecha"])
st.title("Análisis Interactivo de Horas de Luz en Cuatro Ciudades del Mundo")

st.write(
    """
    Este aplicativo permite analizar los datos de salida del sol, puesta del sol y duración del día
    registrados semanalmente para Santiago (Chile), Singapur, Tokio y Oslo.
    El objetivo es visualizar cómo varían estas horas a lo largo del año y compararlas entre países.
    """
)

st.subheader("Comparación entre ciudades para una variable")

opcion_var = st.selectbox(
    "Seleccione la variable a graficar:",
    ["Salida", "Puesta", "Duración"]
)

fig1, ax1 = plt.subplots(figsize=(10, 5))

colores_ciudades = {
    "Chile": "blue",
    "Singapur": "magenta",
    "Tokio": "yellow",
    "Oslo": "red"
}

for ciudad in ["Chile", "Singapur", "Tokio", "Oslo"]:
    df_c = df[df["Ciudad"] == ciudad]
    if not df_c.empty:
        ax1.plot(df_c["Fecha"], df_c[opcion_var], label=ciudad, color=colores_ciudades[ciudad])

ax1.set_title(f"Curva de {opcion_var} para todas las ciudades")
ax1.set_xlabel("Fecha")
ax1.set_ylabel(f"{opcion_var} (h)")
ax1.legend()
plt.xticks(rotation=45)

st.pyplot(fig1)
st.subheader("Curvas completas para una ciudad")

opcion_ciudad = st.selectbox(
    "Seleccione la ciudad a graficar:",
    ["Chile", "Singapur", "Tokio", "Oslo"]
)

fig2, ax2 = plt.subplots(figsize=(10, 5))

colores_vars = {"Salida": "blue", "Puesta": "red", "Duración": "green"}

df_sel = df[df["Ciudad"] == opcion_ciudad]

for var in ["Salida", "Puesta", "Duración"]:
    ax2.plot(df_sel["Fecha"], df_sel[var], label=var, color=colores_vars[var])

ax2.set_title(f"Curvas de Salida, Puesta y Duración para {opcion_ciudad}")
ax2.set_xlabel("Fecha")
ax2.set_ylabel("Horas (h)")
ax2.legend()
plt.xticks(rotation=45)

st.pyplot(fig2)

