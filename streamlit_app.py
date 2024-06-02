import streamlit as st
import pandas as pd

st.markdown(
    "<div style='text-align: center;'><h1>GYM</h1></div>", unsafe_allow_html=True
)

baneados = ["yulia", "david"]
with st.form("inscripcion"):
    nombre = st.text_input("Nombre(s)")
    apellidos = st.text_input("Apellido(s)")
    edad = st.number_input("Edad", min_value=1, step=1)
    municipio = st.text_input("Municipio de residencia")
    motivos = st.text_area("Motivos por los cuales quieres entrar al gimnasio")

    enviado = st.form_submit_button("Enviar")

    if enviado:
        if edad < 15:
            st.error(
                f"Lo sentimos {nombre}, debes tener al menos 15 años para inscribirte."
            )

        elif nombre.lower() in baneados:
            st.error(
                f"Lo sentimos {nombre}, no puedes inscribirte. Fuiste baneado del Gym el mes pasado"
            )
        elif 60 <= edad <= 70:
            st.warning("Tiene una edad avanzada segura que quiere inscribirse al GYM?")
            st.success(f"¡Gracias por inscribirte, {nombre} {apellidos}!")
            st.write(f"Edad: {edad}")
            st.write(f"Municipio: {municipio}")
            st.write(f"Motivos: {motivos}")
        else:
            st.success(f"¡Gracias por inscribirte, {nombre} {apellidos}!")
            st.write(f"Edad: {edad}")
            st.write(f"Municipio: {municipio}")
            st.write(f"Motivos: {motivos}")
