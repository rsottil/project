import streamlit as st
import pandas as pd
import plotly.express as px



st.header("Datos de Vehiculos USA")
car_data = pd.read_csv("vehicles_us.csv")


hist_button = st.button('Construir histograma')
if hist_button:
    st.write("Creating histogram for car sales dataset")
    fig = px.histogram(car_data, x="odometer", title="Odometer Distribution")
    st.plotly_chart(fig, use_container_width=True)


scatter_button = st.button("Build Scatter Plot")
if scatter_button:
    st.write("Creating scatter plot for car sales dataset")
    fig = px.scatter(car_data, x="odometer", y="price", title="Odometer vs Price")
    st.plotly_chart(fig, use_container_width=True)