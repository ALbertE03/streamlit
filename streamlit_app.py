import streamlit as st
import pandas as pd
import csv

st.set_page_config(
    page_title="Inscripción al Gimnasio de influencer",
    page_icon=":muscle:",
    layout="wide",
)
st.markdown(
    "<div style='text-align: center;'><h1>influencer GYM 🤩</h1></div>",
    unsafe_allow_html=True,
)


def otra_pagina():
    try:
        with open("datos.csv", "r") as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            nombre_buscar = st.text_input("Ingresa su nombre")
            primera_columna = [fila[0].lower() for fila in lector_csv]
            if nombre_buscar:
                if nombre_buscar.lower() in primera_columna:
                    st.success(f"El nombre '{nombre_buscar}' existe en el archivo CSV.")
                    foto = st.camera_input("comprobemos si eres tu")
                    if foto:
                        st.success(
                            "No se que hacer con la foto, asi que asumo que eres tú😉, no me engañes"
                        )
                else:
                    st.warning(
                        f"El nombre '{nombre_buscar}' no existe en el archivo CSV."
                    )
    except:
        st.error("Error al cargar el csv")


def pagina_form():
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
                and (nombre.lower() not in baneados)
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
                with open("datos.csv", "a", newline="") as archivo:
                    escritor = csv.writer(archivo)
                    escritor.writerow([nombre, apellidos, edad, municipio, precio, 1])
                    st.success("Datos guardados correctamente")

            if (
                nombre != ""
                and (nombre.lower() not in baneados)
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
                st.info(
                    f"{nombre} este plan solo lo seleccionan los verdaderos reales😎"
                )
                with open("datos.csv", "a", newline="") as archivo:
                    escritor = csv.writer(archivo)
                    escritor.writerow([nombre, apellidos, edad, municipio, precio, 1])
                    st.success("Datos guardados correctamente")

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


pages = {
    "Registro": pagina_form,
    "Inicio de sección(📸)": otra_pagina,
}


selection = st.sidebar.radio("Ir a", list(pages.keys()))
pages[selection]()
st.markdown(
    """
    <div>
        <p>© influencer GYM 2024</p>
        <p> Albert.com</p>
    </div>
""",
    unsafe_allow_html=True,
)
