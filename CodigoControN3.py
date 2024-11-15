import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('data.csv')


st.title("MAX")
st.sidebar.header("Opciones de Filtro")


search_title = st.sidebar.text_input("Buscar película o serie")
filtered_data = data[data['title'].str.contains(search_title, case=False, na=False)]


content_types = filtered_data['type'].unique()
selected_type = st.sidebar.multiselect("Seleccionar tipo de contenido", options=content_types, default=content_types)
filtered_data = filtered_data[filtered_data['type'].isin(selected_type)]



filtered_data = filtered_data.dropna(subset=['genres'])
all_genres = set(g for sublist in filtered_data['genres'].str.split(', ') for g in sublist)
selected_genres = st.sidebar.multiselect("Seleccionar géneros", options=list(all_genres), default=list(all_genres))
filtered_data = filtered_data[filtered_data['genres'].apply(lambda x: any(g in x for g in selected_genres))]


hist_column = st.sidebar.selectbox("Seleccionar columna para histograma", ['imdbAverageRating', 'releaseYear'])


bins = st.sidebar.slider("Número de bins", min_value=5, max_value=50, value=20)


st.write(f"### Resultados de búsqueda ({len(filtered_data)} películas encontradas)")
st.dataframe(filtered_data[['title', 'type', 'genres', 'releaseYear', 'imdbAverageRating']])


st.write(f"### Histograma de {hist_column}")
fig, ax = plt.subplots()
ax.hist(filtered_data[hist_column].dropna(), bins=bins, color='skyblue', edgecolor='black')
ax.set_xlabel(hist_column)
ax.set_ylabel("Frecuencia")
st.pyplot(fig)
