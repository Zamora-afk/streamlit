import streamlit as st

st.set_page_config(page_title="Selección Múltiple")
st.header(" Encuesta con Selección Múltiple (máximo 3 opciones por pregunta)")

# Función para verificar límite de selección
def validar_seleccion(opciones, nombre):
    if len(opciones) > 3:
        st.warning(f" Has seleccionado más de 3 opciones en '{nombre}'. Intenta reducir tu selección.")
    else:
        st.success(f"✅ Selección válida en '{nombre}'")

# Pregunta 1
p1 = st.multiselect(
    " ¿Qué géneros musicales prefieres?",
    ['Pop', 'Rock', 'Reggaetón', 'Jazz', 'Clásica'],
    default=[]
)
validar_seleccion(p1, "Géneros musicales")

# Pregunta 2
p2 = st.multiselect(
    " ¿Qué comidas disfrutas más?",
    ['Pizza', 'Tacos', 'Sushi', 'Hamburguesas', 'Ensalada'],
    default=[]
)
validar_seleccion(p2, "Comidas favoritas")

# Pregunta 3
p3 = st.multiselect(
    " ¿A qué continentes te gustaría viajar?",
    ['Europa', 'Asia', 'América', 'África', 'Oceanía'],
    default=[]
)
validar_seleccion(p3, "Destinos")

# Pregunta 4
p4 = st.multiselect(
    " ¿Qué géneros de películas te gustan?",
    ['Acción', 'Comedia', 'Drama', 'Ciencia ficción', 'Terror'],
    default=[]
)
validar_seleccion(p4, "Películas favoritas")

# Pregunta 5
p5 = st.multiselect(
    " ¿Qué tipos de libros te interesan más?",
    ['Novela', 'Historia', 'Ciencia', 'Autoayuda', 'Fantasía'],
    default=[]
)
validar_seleccion(p5, "Libros preferidos")

# Mostrar respuestas
st.markdown("---")
st.subheader("📋 Resumen de tus respuestas")
st.write("🎶 Música:", p1)
st.write("🍽️ Comida:", p2)
st.write("🌍 Viajes:", p3)
st.write("🎬 Películas:", p4)
st.write("📚 Libros:", p5)
