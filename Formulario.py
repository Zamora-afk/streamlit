import streamlit as st

st.set_page_config(page_title="Encuesta de Opinión", page_icon="🗳️")
st.title("🗳️ Encuesta de Opinión General")

st.header("1. Responde la encuesta")
with st.form("encuesta_general"):
    st.subheader("🔍 ¡Queremos conocer tu opinión!")

    # Pregunta 1: Edad
    edad = st.slider("¿Cuál es tu edad?", 10, 100, 25)

    # Pregunta 2: Género
    genero = st.radio("¿Con qué género te identificas?", ("Femenino", "Masculino", "No binario", "Prefiero no decirlo"))

    # Pregunta 3: ¿Con qué frecuencia usas internet?
    uso_internet = st.selectbox("¿Con qué frecuencia usas internet al día?", ["Menos de 1 hora", "1-3 horas", "3-6 horas", "Más de 6 horas"])

    # Pregunta 4: Medio de transporte principal
    transporte = st.selectbox("¿Cuál es tu medio de transporte principal?", ["Automóvil", "Transporte público", "Bicicleta", "A pie", "Otro"])

    # Pregunta 5: Actividad favorita en tu tiempo libre
    pasatiempo = st.selectbox("¿Qué actividad prefieres en tu tiempo libre?", ["Leer", "Ver series/películas", "Hacer ejercicio", "Jugar videojuegos", "Salir con amigos"])

    # Pregunta 6: Nivel de satisfacción con tu rutina diaria
    satisfaccion = st.slider("¿Qué tan satisfecho estás con tu rutina diaria?", 0, 10, 5)

    # Pregunta 7: ¿Tienes mascota?
    tiene_mascota = st.radio("¿Tienes mascota?", ["Sí", "No"])

    # Pregunta 8: ¿Te gusta trabajar en equipo?
    trabajo_equipo = st.radio("¿Te gusta trabajar en equipo?", ["Sí", "No", "Depende del equipo"])

    # Pregunta 9: ¿Qué sistema operativo prefieres?
    sistema = st.selectbox("¿Qué sistema operativo usas más?", ["Windows", "macOS", "Linux", "Android", "iOS"])

    # Pregunta 10: Comentario adicional
    comentario = st.text_input("¿Hay algo más que quieras compartir?")

    # Botón de enviar
    enviado = st.form_submit_button("Enviar respuestas")

if enviado:
    st.success("✅ ¡Gracias por completar la encuesta!")
    st.markdown(f"""
    ### 📝 Tus respuestas:
    - Edad: `{edad}`
    - Género: `{genero}`
    - Uso de internet: `{uso_internet}`
    - Transporte: `{transporte}`
    - Pasatiempo: `{pasatiempo}`
    - Satisfacción: `{satisfaccion}/10`
    - ¿Tienes mascota?: `{tiene_mascota}`
    - ¿Trabajas bien en equipo?: `{trabajo_equipo}`
    - Sistema operativo: `{sistema}`
    - Comentario: `{comentario if comentario else 'Sin comentarios'}`
    """)
else:
    st.info("☝️ Completa la encuesta y presiona *Enviar respuestas*.")




