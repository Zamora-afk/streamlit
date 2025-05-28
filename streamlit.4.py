import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Encabezado
st.set_page_config(page_title="App con DataFrames")
st.header(' Explorando datos con `st.write()`')




st.subheader("🎓 Calificaciones de estudiantes")
df_notas = pd.DataFrame({
    'Alumno': ['Ana', 'Luis', 'Marta', 'Carlos'],
    'Matemáticas': [85, 90, 78, 92],
    'Historia': [88, 75, 84, 79],
    'Ciencia': [91, 89, 76, 85]
})
st.write("Estas son las calificaciones de 4 alumnos:")
st.write(df_notas)


# --- Ejemplo 5: Población mundial por continente ---
st.subheader("🌍 Población mundial por continente")
df_poblacion = pd.DataFrame({
    'Continente': ['Asia', 'África', 'Europa', 'América', 'Oceanía'],
    'Población (millones)': [4600, 1340, 750, 1000, 43]
})
st.write("Comparación de población en millones:")
st.write(df_poblacion)

# Gráfico de barras
bar_chart = alt.Chart(df_poblacion).mark_bar().encode(
    x='Continente',
    y='Población (millones)',
    color='Continente'
)
st.altair_chart(bar_chart, use_container_width=True)