import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Gráficos con Streamlit")
st.header(' Visualización de datos con 3 gráficos diferentes')


st.subheader(" Temperatura diaria (°C)")
dias = pd.date_range("2025-05-01", periods=7)
df_temp = pd.DataFrame({
    'Día': dias,
    'Temperatura': [24, 25, 26, 27, 28, 29, 30]
})
df_temp.set_index('Día', inplace=True)
st.line_chart(df_temp)


st.subheader(" Ventas semanales por producto")
df_ventas = pd.DataFrame({
    'Producto': ['A', 'B', 'C', 'D'],
    'Ventas': [120, 90, 150, 60]
})
st.bar_chart(df_ventas.set_index('Producto'))


st.subheader(" Crecimiento de usuarios mensuales")
df_usuarios = pd.DataFrame({
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
    'Usuarios': [100, 180, 250, 320, 400]
})
df_usuarios.set_index('Mes', inplace=True)
st.area_chart(df_usuarios)