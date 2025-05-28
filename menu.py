import streamlit as st

st.set_page_config(page_title="Menú de Comida Rápida")
st.header(" Menú de Comida Rápida")
st.write("Selecciona lo que te gustaría ordenar:")

# Opciones del menú (checkboxes)
hamburguesa = st.checkbox("Hamburguesa 🍔")
papas = st.checkbox("Papas fritas 🍟")
nuggets = st.checkbox("Nuggets de pollo 🍗")
refresco = st.checkbox("Refresco 🥤")
helado = st.checkbox("Helado 🍦")

# Mensajes individuales si se elige cada uno
if hamburguesa:
    st.write("Añadido: Hamburguesa 🍔")
if papas:
    st.write("Añadido: Papas fritas 🍟")
if nuggets:
    st.write("Añadido: Nuggets de pollo 🍗")
if refresco:
    st.write("Añadido: Refresco 🥤")
if helado:
    st.write("Añadido: Helado 🍦")

# Mostrar resumen final
st.markdown("---")
st.subheader("🧾 Resumen de tu orden:")
pedido = []
if hamburguesa:
    pedido.append("Hamburguesa")
if papas:
    pedido.append("Papas fritas")
if nuggets:
    pedido.append("Nuggets")
if refresco:
    pedido.append("Refresco")
if helado:
    pedido.append("Helado")

if pedido:
    st.write("Has ordenado:", ", ".join(pedido))
else:
    st.write("No has seleccionado nada aún.")
