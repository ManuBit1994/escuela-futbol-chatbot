import pandas as pd
import streamlit as st

df = pd.read_csv("escuela_futbol.csv")

st.title("⚽ ChatBot Escuela de Fútbol")

pregunta = st.text_input("Haz una pregunta")

if pregunta:

    pregunta = pregunta.lower()

    if "cuantos registros" in pregunta:
        st.write(f"Hay {len(df)} registros")

    elif "edad promedio" in pregunta:
        st.write(df["EdadTomador"].mean())

    else:
        st.write("No entendí la pregunta")