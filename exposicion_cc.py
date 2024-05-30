import streamlit as st
import streamlit.components.v1 as components

def main():
    # Configuración de la página
    st.set_page_config(
        page_title="Exposición de Competencias Comunicativas",
        page_icon=":rocket:",
        layout="wide"
    )

    # Estilo personalizado
    st.markdown(
        """
        <style>
            .main {
                background-color: #f8f9fa;
            }
            .sidebar .sidebar-content {
                background-color: #343a40;
                color: #ffffff;
            }
            .Widget.stButton {
                background-color: #007bff;
                color: #ffffff;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Título
    st.title("Exposición de Competencias Comunicativas")

    # Menú de navegación
    navigation = st.sidebar.radio("Navegación", ["Introducción", "Tema 1", "Tema 2", "Tema 3", "Tema 4"])

    if navigation == "Introducción":
        show_title()
    elif navigation == "Tema 1":
        show_topic1()
    elif navigation == "Tema 2":
        show_topic2()
    elif navigation == "Tema 3":
        show_topic3()
    elif navigation == "Tema 4":
        show_topic4()

def show_title():
    st.header("Análisis del Capítulo 3 del libro 'Saber Hablar': `La Producción del Discurso Oral: La Claridad en las Ideas.`")
    st.image("markmap/portada.png", use_column_width=True)

def show_topic1():
    st.header("`Tema 1`: La Preparación del Discurso: Las Circunstancias del Público, la Intención del Discurso, la Elección del Tema o Título, la Recogida de Ideas")
    
    # Leer y mostrar el contenido del archivo HTML de Markmap
    with open("markmap/sosa.html", "r", encoding='utf-8') as f:
        markmap_html = f.read()
    components.html(markmap_html, height=500)

def show_topic2():
    st.header("`Tema 2`: Selección y Ordenación de las Ideas")
    
    with open("markmap/candia.html", "r", encoding='utf-8') as f:
        markmap_html = f.read()
    components.html(markmap_html, height=500)

def show_topic3():
    st.header("`Tema 3`: Ordenar lo que se va a decir. Jerarquización de las Ideas: El Guión")
    
    with open("markmap/caceres.html", "r", encoding='utf-8') as f:
        markmap_html = f.read()
    components.html(markmap_html, height=500)


def show_topic4():
    st.header("`Tema 4`: Modelos de estructuración de un discurso")
    
    with open("markmap/vera.html", "r", encoding='utf-8') as f:
        markmap_html = f.read()
    components.html(markmap_html, height=500)


if __name__ == "__main__":
    main()
