
import streamlit as st

st.set_page_config(page_title="App con Botones", page_icon="🖱️", layout="centered")
st.title(" App Interactiva con 3 Botones")

st.markdown("prueba los botones")

# --- Botón 1 ---
st.subheader("🔘 Botón 1")
if st.button("Presióname"):
    st.write("Velociraptor")
else:
    st.write("ADIOS")

# --- Botón 2 ---
st.subheader("🔘 Botón 2")
if st.button("Presióname 2"):
    st.write("Spiderman")
else:
    st.write("ADIOS")

# --- Botón 3 ---
st.subheader("🔘 Botón 3")
if st.button("Presióname 3 "):
    st.write("me caen mal los otros botones")
else:
    st.write("ADIOS")