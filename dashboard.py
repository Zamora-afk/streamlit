import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Cargar el archivo de datos
file_path = 'UPDINTEGRADO_sincodificar_3categorias.xlsx - Sheet1.csv'
df = pd.read_csv(file_path)

# 2. Título general
st.title("📦 Análisis Integral de Pedidos y Categorías de Productos")

# 3. Barra lateral con filtros
st.sidebar.header("Filtros Interactivos")

# Filtro de volumen
min_volumen = int(df['volumen'].min())
max_volumen = int(df['volumen'].max())
volumen_range = st.sidebar.slider("Selecciona el rango de volumen:", 
                                  min_value=min_volumen, 
                                  max_value=max_volumen, 
                                  value=(min_volumen, max_volumen))

# Filtro de región
regiones = df['region'].unique()
region_seleccionada = st.sidebar.selectbox("Selecciona la región:", opciones := ['Todas'] + list(regiones))

# 4. Aplicar filtros
df_filtrado = df[(df['volumen'] >= volumen_range[0]) & (df['volumen'] <= volumen_range[1])]
if region_seleccionada != 'Todas':
    df_filtrado_region = df[df['region'] == region_seleccionada]
else:
    df_filtrado_region = df.copy()

# 5. Pestañas para las visualizaciones
tab1, tab2 = st.tabs(["Visualizaciones 1-2", "Visualizaciones 3-4"])

# Colores
color_principal = '#5B2C6F'  # Morado oscuro
color_secundario = '#AF7AC5'  # Morado claro

# Pestaña 1: Visualizaciones 1 y 2
with tab1:
    st.subheader("🔹 Distribución de Pagos por Tipo de Entrega")
    pago_entrega = df_filtrado.groupby('tipo_entrega_clase')['pago'].sum()
    fig1, ax1 = plt.subplots()
    pago_entrega.plot(kind='bar', ax=ax1, color=color_principal)
    ax1.set_xlabel("Tipo de Entrega")
    ax1.set_ylabel("Pago Total")
    ax1.set_title("Distribución de Pagos por Tipo de Entrega")
    st.pyplot(fig1)

    st.subheader("🔹 Costo Promedio de Flete por Rangos de 3 Días de Entrega")
    # Agrupar el tiempo de entrega en bins de 3 días
    max_dias = int(df_filtrado_region['tiempo_total_entrega_dias'].max())
    bins = list(range(0, max_dias + 4, 3))  # +4 para incluir el último rango
    labels = [f'{bins[i]}-{bins[i+1]-1} días' for i in range(len(bins)-1)]
    
    df_filtrado_region['rango_entrega'] = pd.cut(df_filtrado_region['tiempo_total_entrega_dias'], 
                                                  bins=bins, labels=labels, include_lowest=True)
    costo_promedio = df_filtrado_region.groupby('rango_entrega')['costo_de_flete'].mean().dropna()

    fig2, ax2 = plt.subplots()
    costo_promedio.plot(kind='bar', ax=ax2, color=color_secundario)
    ax2.set_xlabel("Rango de Tiempo de Entrega (3 días)")
    ax2.set_ylabel("Costo Promedio de Flete")
    ax2.set_title("Costo Promedio de Flete por Rangos de 3 Días de Entrega")
    st.pyplot(fig2)

# Pestaña 2: Visualizaciones 3 y 4
with tab2:
    st.subheader("🔹 Categorías más Populares en Pedidos")
    categorias_count = df_filtrado['categoria_de_productos'].value_counts()
    fig3, ax3 = plt.subplots()
    categorias_count.plot(kind='bar', ax=ax3, color=color_secundario)
    ax3.set_xlabel("Categoría de Productos")
    ax3.set_ylabel("Frecuencia")
    ax3.set_title("Categorías más Populares en Pedidos")
    st.pyplot(fig3)

    st.subheader("🔹 Distribución Geográfica de Pedidos")
    region_count = df_filtrado_region['region'].value_counts()
    fig4, ax4 = plt.subplots()
    region_count.plot(kind='pie', ax=ax4, autopct='%1.1f%%', startangle=90, 
                       colors=[color_principal, color_secundario, '#BB8FCE'])
    ax4.set_ylabel('')
    ax4.set_title("Distribución Geográfica de Pedidos")
    st.pyplot(fig4)
