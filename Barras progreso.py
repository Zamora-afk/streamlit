import streamlit as st
import time

st.set_page_config(page_title="Barras de Progreso")
st.title(" Barras de Progreso con Diferentes Velocidades")

with st.expander("ℹ️ Sobre esta app"):
    st.write("Esta app muestra cómo se pueden usar múltiples barras de progreso con diferentes velocidades usando `st.progress`.")

# Barra 1 - Rápida
st.subheader(" Progreso rápido")
bar1 = st.progress(0)
for i in range(101):
    time.sleep(0.01)  # Muy rápido
    bar1.progress(i)
st.success("✅ Barra rápida completada")

# Barra 2 - Velocidad media
st.subheader(" Progreso medio")
bar2 = st.progress(0)
for i in range(101):
    time.sleep(0.03)  # Velocidad intermedia
    bar2.progress(i)
st.success("✅ Barra media completada")

# Barra 3 - Lenta
st.subheader(" Progreso lento")
bar3 = st.progress(0)
for i in range(101):
    time.sleep(0.06)  # Más lento
    bar3.progress(i)
st.success("✅ Barra lenta completada")

# Celebración al final
st.balloons()
