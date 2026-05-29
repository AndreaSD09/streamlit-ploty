import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Gapminder Dashboard",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 Gapminder Dashboard")
st.write(
    "Aplicación interactiva para explorar expectativa de vida, población "
    "y PIB per cápita por país y continente."
)

df = px.data.gapminder()

st.write("Vista previa de los datos:")
st.dataframe(df.head())