import streamlit as st

st.set_page_config(page_title="Preguntas con Selectbox")
st.header(' Preguntas con múltiples opciones')

# Pregunta 1: Color favorito
color = st.selectbox("🎨 ¿Cuál es tu color favorito?", ("Azul", "Rojo", "Verde", "Amarillo", "Negro"))
st.write("✅ Elegiste el color:", color)

# Pregunta 2: Animal favorito
animal = st.selectbox("🐾 ¿Cuál es tu animal favorito?", ("Perro", "Gato", "Delfín", "Águila", "Elefante"))
st.write("✅ Animal elegido:", animal)

# Pregunta 3: Comida preferida
comida = st.selectbox("🍕 ¿Qué comida prefieres?", ("Pizza", "Sushi", "Tacos", "Pasta", "Ensalada"))
st.write("✅ Comida favorita:", comida)

# Pregunta 4: Estación del año favorita
estacion = st.selectbox("🌤️ ¿Cuál es tu estación del año favorita?", ("Primavera", "Verano", "Otoño", "Invierno"))
st.write("✅ Estación seleccionada:", estacion)

# Pregunta 5: Medio de transporte ideal
transporte = st.selectbox("🚗 ¿Qué medio de transporte prefieres?", ("Automóvil", "Bicicleta", "Metro", "Avión", "A pie"))
st.write("✅ Transporte elegido:", transporte)