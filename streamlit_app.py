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
    precio = st.selectbox("Plan de Precios", ["Precios", "100$", "150$", "200$"])

    enviado = st.form_submit_button("Enviar")

    if enviado:
        if (
            nombre != ""
            and len(nombre) > 3
            and (nombre not in baneados)
            and apellidos != ""
            and len(apellidos) > 3
            and edad > 15
            and municipio != ""
            and precio != "Precios"
            and precio != "200$"
        ):
            st.success(f"¡Gracias por inscribirte, {nombre} {apellidos}!")
            st.write(f"Edad: {edad}")
            st.write(f"Municipio: {municipio}")
            st.write(f"Motivos: {motivos}")
            st.write(f"Precio del plan seleccionado: {precio}")

        if (
            nombre != ""
            and (nombre not in baneados)
            and len(nombre) > 3
            and apellidos != ""
            and len(apellidos) > 3
            and edad > 15
            and municipio != ""
            and precio != "Precios"
            and precio == "200$"
        ):
            st.success(f"¡Gracias por inscribirte, {nombre} {apellidos}!")
            st.write(f"Edad: {edad}")
            st.write(f"Municipio: {municipio}")
            st.write(f"Motivos: {motivos}")
            st.write(f"Precio del plan seleccionado: {precio}")
            st.info(f"{nombre} este plan solo lo seleccionan los verdaderos reales😎")

        if nombre == "" and nombre.lower() != "yulia":
            st.error("Por favor, ingresa tu nombre")
        if len(nombre) <= 3 and nombre != "" and nombre.lower() != "yulia":
            st.warning(
                f"nadie se llama {nombre}, creo. Si es su nombre correcto contactar con el staff. se encuetra a su lado 🫡"
            )
            st.error("Por favor, ingresa un nombre válido")
        if len(apellidos) <= 3 and nombre.lower() != "yulia":
            st.error("Por favor, ingresa un apellido válido")
        if apellidos == "" and nombre.lower() != "yulia":
            st.error("Por favor ingresa tus apellidos")
        if edad < 15 and edad != 1 and nombre.lower() != "yulia":
            st.error(
                f"Lo sentimos {nombre}, debes tener al menos 15 años para inscribirte."
            )
        if edad == 1 and nombre.lower() != "yulia":
            st.error("Por favor modifique el campo edad con su edad real")
        if municipio == "" and nombre.lower() != "yulia":
            st.error("Por favor ingresa tu municipio de residencia")
        if nombre.lower() in baneados and nombre.lower() != "yulia":
            st.error(
                f"Lo sentimos {nombre}, no puedes inscribirte. Fuiste baneado del Gym el mes pasado"
            )
        if nombre.lower() == "yulia":
            st.error(
                f"{nombre} no necesitas el GYM, ya estas buena, vaya a estudiar bb."
            )
        if (precio == "Precios" or precio == "") and nombre.lower() != "yulia":
            st.error("no puede inscribirse sin pagar, seleccione un precio")
        if (
            motivos == ""
            and nombre != ""
            and apellidos != ""
            and edad > 15
            and municipio != ""
            and nombre.lower() != "yulia"
        ):
            st.warning(
                "no quiere poner ningún motivo 🙂? o es el que todos sabemos 😉?"
            )
