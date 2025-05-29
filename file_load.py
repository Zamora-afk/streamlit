import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Comparador de CSV", page_icon="📁")
st.title("📁 Comparador de dos archivos CSV")
st.write("Sube dos archivos `.csv` para visualizar sus datos y comparar sus estadísticas.")

# Subida del primer archivo
st.subheader("📤 Archivo 1")
file1 = st.file_uploader("Elige el primer archivo CSV", type="csv", key="file1")

# Subida del segundo archivo
st.subheader("📤 Archivo 2")
file2 = st.file_uploader("Elige el segundo archivo CSV", type="csv", key="file2")

# Validación y procesamiento
if file1 is not None and file2 is not None:
    try:
        df1 = pd.read_csv(file1)
        df2 = pd.read_csv(file2)

        st.markdown("---")
        st.subheader("📄 Vista previa del **Archivo 1**")
        st.dataframe(df1)

        st.subheader("📄 Vista previa del **Archivo 2**")
        st.dataframe(df2)

        st.markdown("---")
        st.subheader("📊 Estadísticas descriptivas comparadas")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Archivo 1**")
            st.write(df1.describe())
        with col2:
            st.markdown("**Archivo 2**")
            st.write(df2.describe())

    except Exception as e:
        st.error(f"❌ Ocurrió un error al procesar los archivos: {e}")
else:
    st.info("☝️ Sube ambos archivos CSV para continuar.")
