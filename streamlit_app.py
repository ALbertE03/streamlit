import streamlit as st
import pandas as pd

st.markdown(
    "<div style='text-align: center;'><h1>GYM</h1></div>", unsafe_allow_html=True
)

with st.form("inscripcion_form"):
    nombre = st.text_input("Nombre(s)")
    apellidos = st.text_input("Apellido(s)")
    edad = st.number_input("Edad", min_value=1, step=1)
    municipio = st.text_input("Municipio de residencia")
    motivos = st.text_area("Motivos por los cuales quieres entrar al gimnasio")

    enviado = st.form_submit_button("Enviar")

    if enviado:
        if edad < 15:
            st.error("Lo sentimos, debes tener al menos 15 años para inscribirte.")
        else:
            st.success(f"¡Gracias por inscribirte, {nombre} {apellidos}!")
            st.write(f"Edad: {edad}")
            st.write(f"Municipio: {municipio}")
            st.write(f"Motivos: {motivos}")
