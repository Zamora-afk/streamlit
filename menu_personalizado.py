import streamlit as st

# Mostrar el tema personalizado como código dentro de la app
st.title("🍔 Menú de Comida Rápida")


# Sidebar
st.sidebar.title("📋 Instrucciones")
st.sidebar.markdown("Marca los alimentos que quieres incluir en tu orden. Tu resumen aparecerá al final.")

st.markdown("---")
st.header("🧾 ¿Qué deseas ordenar?")

# Checkboxes del menú
hamburguesa = st.checkbox("Hamburguesa 🍔")
papas = st.checkbox("Papas fritas 🍟")
nuggets = st.checkbox("Nuggets de pollo 🍗")
refresco = st.checkbox("Refresco 🥤")
helado = st.checkbox("Helado 🍦")

# Mensajes individuales
if hamburguesa:
    st.success("✓ Añadido: Hamburguesa 🍔")
if papas:
    st.success("✓ Añadido: Papas fritas 🍟")
if nuggets:
    st.success("✓ Añadido: Nuggets de pollo 🍗")
if refresco:
    st.success("✓ Añadido: Refresco 🥤")
if helado:
    st.success("✓ Añadido: Helado 🍦")

# Resumen
st.markdown("---")
st.subheader("📦 Tu orden:")
pedido = []
if hamburguesa: pedido.append("Hamburguesa")
if papas: pedido.append("Papas fritas")
if nuggets: pedido.append("Nuggets")
if refresco: pedido.append("Refresco")
if helado: pedido.append("Helado")

if pedido:
    st.write("Has ordenado:", ", ".join(pedido))
else:
    st.warning("No has seleccionado nada aún.")
