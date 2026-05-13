import pandas as pd
import streamlit as st

# Leer base de datos
df = pd.read_csv("escuela_futbol.csv")

# Título
st.title("⚽ ChatBot Escuela de Fútbol")

# Caja de texto
pregunta = st.text_input("Haz una pregunta")

# Procesar pregunta
if pregunta:

    pregunta = pregunta.lower()

    # CUÁNTOS REGISTROS
    if (
        "cuantos registros" in pregunta
        or "cuántos registros" in pregunta
        or "cuantos alumnos" in pregunta
        or "cuántos alumnos" in pregunta
        or "cuantas personas" in pregunta
    ):

        st.success(f"Hay {len(df)} registros en la base de datos")

    # EDAD PROMEDIO
    elif (
        "edad promedio" in pregunta
        or "promedio de edad" in pregunta
        or "edad media" in pregunta
    ):

        promedio = round(df["EdadTomador"].mean(), 2)

        st.success(f"La edad promedio es {promedio} años")

    # EDAD MÁXIMA
    elif (
        "edad maxima" in pregunta
        or "edad máxima" in pregunta
        or "mayor edad" in pregunta
    ):

        maxima = df["EdadTomador"].max()

        st.success(f"La edad máxima es {maxima}")

    # EDAD MÍNIMA
    elif (
        "edad minima" in pregunta
        or "edad mínima" in pregunta
        or "menor edad" in pregunta
    ):

        minima = df["EdadTomador"].min()

        st.success(f"La edad mínima es {minima}")

    # MOSTRAR DATOS
    elif (
        "mostrar datos" in pregunta
        or "ver datos" in pregunta
        or "mostrar tabla" in pregunta
    ):

        st.dataframe(df)

    # RESPUESTA POR DEFECTO
    else:

        st.error("No entendí la pregunta")
