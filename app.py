import pandas as pd
import streamlit as st

# Leer base de datos
df = pd.read_csv("escuela_futbol.csv")

# Convertir fecha
df["FechaCompra"] = pd.to_datetime(df["FechaCompra"])

# Crear columna Mes
df["Mes"] = df["FechaCompra"].dt.month_name()

# Título
st.title("⚽ ChatBot Escuela de Fútbol")

st.write("Haz preguntas sobre la base de datos")

# Entrada usuario
pregunta = st.text_input("Escribe tu pregunta")

# Procesar preguntas
if pregunta:

    pregunta = pregunta.lower()

    # OBJETIVO DEL PROYECTO
    if (
        "objetivo del proyecto" in pregunta
        or "cual es el objetivo" in pregunta
        or "cuál es el objetivo" in pregunta
    ):

        st.success(
            "El objetivo del proyecto es analizar la información "
            "de los estudiantes de la escuela de fútbol para obtener estadísticas."
        )

    # CUÁNTOS REGISTROS
    elif (
        "cuantos registros" in pregunta
        or "cuántos registros" in pregunta
        or "cuantos alumnos" in pregunta
        or "cuántos alumnos" in pregunta
    ):

        st.success(f"Hay {len(df)} registros en la base de datos")

    # EDAD PROMEDIO
    elif (
        "edad promedio" in pregunta
        or "promedio de edad" in pregunta
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

    # GRUPO CON MÁS ESTUDIANTES
    elif (
        "grupo con mas estudiantes" in pregunta
        or "grupo con más estudiantes" in pregunta
        or "grupo con mayor cantidad" in pregunta
    ):

        grupo = df["Grupo"].value_counts().idxmax()
        cantidad = df["Grupo"].value_counts().max()

        st.success(
            f"El grupo con más estudiantes es {grupo} con {cantidad} estudiantes"
        )

    # 3 MESES CON MÁS ESTUDIANTES
    elif (
        "3 meses con mas estudiantes" in pregunta
        or "3 meses con más estudiantes" in pregunta
        or "meses con mayor volumen" in pregunta
    ):

        top_meses = df["Mes"].value_counts().head(3)

        st.write("📈 Los 3 meses con más estudiantes son:")

        st.write(top_meses)

    # 3 MESES CON MENOS ESTUDIANTES
    elif (
        "3 meses con menos estudiantes" in pregunta
        or "3 meses con menos volumen" in pregunta
        or "meses con menor volumen" in pregunta
    ):

        bottom_meses = df["Mes"].value_counts().tail(3)

        st.write("📉 Los 3 meses con menos estudiantes son:")

        st.write(bottom_meses)

    # MOSTRAR DATOS
    elif (
        "mostrar datos" in pregunta
        or "ver datos" in pregunta
        or "mostrar tabla" in pregunta
    ):

        st.dataframe(df)

    # SI NO ENTIENDE
    else:

        st.error("No entendí la pregunta")
