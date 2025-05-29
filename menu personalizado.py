import streamlit as st

st.set_page_config(page_title="Menú de Comida Rápida", page_icon="🍔")
st.title("🍔 Menú de Comida Rápida")
st.write("Selecciona lo que te gustaría ordenar:")

# --- Lado izquierdo: barra lateral con instrucciones
st.sidebar.title("📋 Instrucciones")
st.sidebar.markdown("Marca los alimentos que quieres incluir en tu orden. Tu resumen aparecerá al final.")

# Opciones del menú (checkboxes)
hamburguesa = st.checkbox("Hamburguesa 🍔")
papas = st.checkbox("Papas fritas 🍟")
nuggets = st.checkbox("Nuggets de pollo 🍗")
refresco = st.checkbox("Refresco 🥤")
helado = st.checkbox("Helado 🍦")

# Mensajes individuales si se elige cada uno
if hamburguesa:
    st.success("Añadido: Hamburguesa 🍔")
if papas:
    st.success("Añadido: Papas fritas 🍟")
if nuggets:
    st.success("Añadido: Nuggets de pollo 🍗")
if refresco:
    st.success("Añadido: Refresco 🥤")
if helado:
    st.success("Añadido: Helado 🍦")

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
    st.write("✅ Has ordenado:", ", ".join(pedido))
else:
    st.warning("No has seleccionado nada aún.")

[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#7F8C8D"
textColor="#FFFFFF"
font="monospace"
