import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

st.set_page_config(layout="wide")
st.title("🅿️ Roma Mobility: Analisi Infrastrutturale Parcheggi")

# Connessione al DB
engine = create_engine('sqlite:///mobility.db')

@st.cache_data
def load_data():
    return pd.read_sql("SELECT * FROM parking_stats", engine)

df = load_data()

# KPI
col1, col2 = st.columns(2)
col1.metric("Totale Parcheggi a DB", len(df))
col2.metric("Posti Auto Totali", int(df['posti_totali'].sum()))

# Grafico
st.subheader("Distribuzione Posti per Parcheggio")
fig = px.bar(df, x='nome_parcheggio', y='posti_totali', title="Capacità Totale")
fig.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig, use_container_width=True)