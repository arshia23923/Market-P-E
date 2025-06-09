
import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("C:/Users/Arshia/Desktop/realistic_market_pe.csv", parse_dates=["date"])

st.title("📊 Tehran Stock Exchange - Market P/E Ratio")
fig = px.line(df, x="date", y="pe_ratio", title="Market P/E Trend (2015–2023)")
st.plotly_chart(fig)


