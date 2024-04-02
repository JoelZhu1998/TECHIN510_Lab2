# app.py
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Penguins Explorer",
    page_icon="🐧",
    layout="centered", # centered, wide 
    initial_sidebar_state="auto", 
    menu_items=None
)

st.title("🐧 Penguins Explorer")

df = pd.read_csv('https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv')

st.write(df)
