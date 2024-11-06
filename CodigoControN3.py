import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
         
data = pd.read_csv('data.csv')

# Configuración de la página
st.title("Explorador de Películas")
st.sidebar.header("Opciones de Filtro")

# Filtro de búsqueda de película
search_title = st.sidebar.text_input("Buscar película por título")
filtered_data = data[data['title'].str.contains(search_title, case=False, na=False)]

# Filtro por tipo de contenido
content_types = filtered_data['type'].unique()
selected_type = st.sidebar.multiselect("Seleccionar tipo de contenido", options=content_types, default=content_types)
filtered_data = filtered_data[filtered_data['type'].isin(selected_type)]

# Filtro por género
all_genres = set(g for sublist in filtered_data['genres'].str.split(', ') for g in sublist)
selected_genres = st.sidebar.multiselect("Seleccionar géneros", options=list(all_genres), default=list(all_genres))
filtered_data = filtered_data[filtered_data['genres'].apply(lambda x: any(g in x for g in selected_genres))]

# Selección de columna para el histograma
hist_column = st.sidebar.selectbox("Seleccionar columna para histograma", ['imdbAverageRating', 'releaseYear'])

# Ajuste de bins
bins = st.sidebar.slider("Número de bins", min_value=5, max_value=50, value=20)

# Mostrar resultados
st.write(f"### Resultados de búsqueda ({len(filtered_data)} películas encontradas)")
st.dataframe(filtered_data[['title', 'type', 'genres', 'releaseYear', 'imdbAverageRating']])

# Generar histograma
st.write(f"### Histograma de {hist_column}")
fig, ax = plt.subplots()
ax.hist(filtered_data[hist_column].dropna(), bins=bins, color='skyblue', edgecolor='black')
ax.set_xlabel(hist_column)
ax.set_ylabel("Frecuencia")
st.pyplot(fig)

