import streamlit as st
from datetime import time, datetime

st.set_page_config(page_title="Sliders Simples", page_icon="🎚️")
st.header("🎚️ Sliders Simples")

# Slider 1: Edad
edad = st.slider("¿Cuál es tu edad?", 0, 100, 25)
st.write("Edad:", edad)

# Slider 2: Porcentaje
porcentaje = st.slider("Selecciona un porcentaje", 0, 100, 50)
st.write("Porcentaje:", porcentaje, "%")

# Slider 3: Hora del día
hora = st.slider("Elige una hora", value=time(14, 0))
st.write("Hora seleccionada:", hora)

# Slider 4: Fecha de nacimiento (aproximada)
fecha = st.slider("Elige una fecha", value=datetime(2000, 1, 1))
st.write("Fecha:", fecha.date())