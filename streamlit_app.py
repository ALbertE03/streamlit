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
        if nombre != "" and apellidos != "" and edad > 15 and municipio != "":
            st.success(f"¡Gracias por inscribirte, {nombre} {apellidos}!")
            st.write(f"Edad: {edad}")
            st.write(f"Municipio: {municipio}")
            st.write(f"Motivos: {motivos}")

        if nombre == "":
            st.error("Por favor, ingresa tu nombre")
        if apellidos == "":
            st.error("Por favor ingresa tus apellidos")
        if edad < 15 and edad != 1:
            st.error(
                f"lo sentimos {nombre} debes tener al menos 15 años para inscribirte."
            )
        if edad == 1:
            st.error("Por favor modifique el campo edad con su edad real")
        if municipio == "":
            st.error("Por favor ingresa tu municipio de residencia")
        elif nombre.lower() in baneados:
            st.error(
                f"Lo sentimos {nombre}, no puedes inscribirte. Fuiste baneado del Gym el mes pasado"
            )
        if (
            motivos == ""
            and nombre != ""
            and apellidos != ""
            and edad > 15
            and municipio != ""
        ):
            st.warning(
                "no quiere poner ningún motivo 🙂? o es el que todos sabemos 😉?"
            )
