import pandas as pd
import scipy.stats
import streamlit as st
import plotly.express as px

car_data = pd.read_csv('E:\\Tripleten\\Sprint_5\\Mis_proyectos\\Proy_1\\vehicles_us.csv')

st.header("Análisis del conjunto de datos")

hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: 
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Construir gráfico de dispersión') # crear un botón
        
if disp_button: 
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="price", y="odometer")
    st.plotly_chart(fig, use_container_width=True)
