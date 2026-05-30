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

st.subheader("Visualizaciones")

fig_scatter = px.scatter(
    df_anio,
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="country",
    hover_name="country",
    log_x=usar_escala_log,
    title=f"PIB per cápita vs expectativa de vida - {anio_seleccionado}"
)

st.plotly_chart(fig_scatter, use_container_width=True)


fig_bar = px.bar(
    df_anio.sort_values("pop", ascending=False),
    x="country",
    y="pop",
    color="country",
    title=f"Población por país - {anio_seleccionado}"
)

st.plotly_chart(fig_bar, use_container_width=True)


fig_line = px.line(
    df_filtrado,
    x="year",
    y="lifeExp",
    color="country",
    markers=True,
    title="Evolución de la expectativa de vida"
)

st.plotly_chart(fig_line, use_container_width=True)

mostrar_tabla = st.sidebar.checkbox("Mostrar tabla de datos", value=True)

if mostrar_tabla:
    st.subheader("Datos filtrados")
    st.dataframe(df_anio)

if st.button("Mostrar conclusión"):
    st.write(
        "Los filtros permiten explorar cómo cambian los indicadores "
        "según continente, país y año."
    )