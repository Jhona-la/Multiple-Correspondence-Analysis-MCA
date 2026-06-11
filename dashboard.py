import streamlit as st
import pandas as pd
import plotly.express as px
from src.utils import load_and_preprocess_data
from src.styling import display_kpi_dashboard

st.set_page_config(page_title="Absentismo Docente - Dashboard", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f4f7f6; }
    h1 { color: #2c3e50; font-family: 'Montserrat', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏛️ Control de Mando: Absentismo Docente")
st.write("Análisis estratégico de novedades administrativas en el sector educativo.")

@st.cache_data
def get_data():
    return load_and_preprocess_data()

try:
    df = get_data()

    # Sidebar Filters
    st.sidebar.header("Filtros de Análisis")
    selected_sede = st.sidebar.multiselect("Seleccionar Sede", options=df["NOMBRE_SEDE"].unique())
    selected_tipo = st.sidebar.multiselect("Tipo de Vinculación", options=df["TIPO"].unique(), default=df["TIPO"].unique())

    filtered_df = df[df["TIPO"].isin(selected_tipo)]
    if selected_sede:
        filtered_df = filtered_df[filtered_df["NOMBRE_SEDE"].isin(selected_sede)]

    # Main KPIs
    total_dias = filtered_df["DIAS HABILES"].sum()
    promedio = filtered_df["DIAS HABILES"].mean()
    total_casos = len(filtered_df)

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Días", f"{total_dias:,.0f}")
    col2.metric("Promedio Días", f"{promedio:.2f}")
    col3.metric("Total Registros", f"{total_casos:,.0f}")

    # Visualizations
    st.subheader("📊 Distribución de Impacto")
    fig_hist = px.histogram(filtered_df, x="DIAS HABILES", color="TIPO", barmode="overlay",
                            title="Distribución de Días de Ausencia", color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig_hist, use_container_width=True)

    c1, c2 = st.columns(2)
    with c1:
        st.subheader("🏫 Top Sedes Críticas")
        top_s = filtered_df.groupby("NOMBRE_SEDE")["DIAS HABILES"].sum().nlargest(10).reset_index()
        fig_s = px.bar(top_s, y="NOMBRE_SEDE", x="DIAS HABILES", orientation='h', color="DIAS HABILES")
        st.plotly_chart(fig_s, use_container_width=True)

    with c2:
        st.subheader("👤 Perfil por Género")
        fig_p = px.pie(filtered_df, names="SEXO", values="DIAS HABILES", hole=.4)
        st.plotly_chart(fig_p, use_container_width=True)

except Exception as e:
    st.error(f"Error cargando el dashboard: {e}")
