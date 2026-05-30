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
    "Explora cómo han cambiado la expectativa de vida, la población "
    "y el PIB per cápita en diferentes países."
)

df = px.data.gapminder()

st.sidebar.header("Filtros")

continentes = sorted(df["continent"].unique())

continente_seleccionado = st.sidebar.selectbox(
    "Selecciona un continente",
    continentes
)

df_continente = df[df["continent"] == continente_seleccionado]

paises_disponibles = sorted(df_continente["country"].unique())

paises_seleccionados = st.sidebar.multiselect(
    "Selecciona países",
    paises_disponibles,
    default=paises_disponibles[:5]
)

anio_seleccionado = st.sidebar.slider(
    "Selecciona un año",
    int(df["year"].min()),
    int(df["year"].max()),
    int(df["year"].max()),
    step=5
)

usar_escala_log = st.sidebar.checkbox(
    "Usar escala logarítmica para PIB per cápita",
    value=True
)

df_filtrado = df_continente[
    (df_continente["country"].isin(paises_seleccionados))
]

df_anio = df_filtrado[df_filtrado["year"] == anio_seleccionado]

st.subheader("Datos filtrados")
st.dataframe(df_anio)

col1, col2, col3 = st.columns(3)

promedio_vida = df_anio["lifeExp"].mean()
poblacion_total = df_anio["pop"].sum()
pib_promedio = df_anio["gdpPercap"].mean()

col1.metric("Expectativa de vida promedio", f"{promedio_vida:,.1f} años")
col2.metric("Población total", f"{poblacion_total:,.0f}")
col3.metric("PIB per cápita promedio", f"${pib_promedio:,.0f}")