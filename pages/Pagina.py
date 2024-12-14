import streamlit as st
import datetime

st.title('Datos del usuario')

edad = st.number_input("Ingrese su edad:", 0, 100)
nombre = st.text_input("Nombres y apellidos:", max_chars=30, placeholder="Ingrese su nombre completo")

genero = st.radio("Género:", [":blue[Hombre]",":red[Mujer]",":rainbow[Otro]"],index=None)
pais = st.selectbox("Seleccione su país:", ("Ecuador", "Colombia", "Brasil", "Perú", "Chile"))

hora = st.time_input("Seleccione la hora para contactarlo:", datetime.time(9, 00))
st.write("Ha solicitado contactarlo desde:", hora, "horas")

fec_nac = st.date_input("Ingrese su fecha de nacimiento", value=None)
st.write("Nació el:", fec_nac)

st.write("Subir archivos")
uploaded_files = st.file_uploader("", type="pdf", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)

mes = st.slider("Seleccione el mes de su nacimiento:", 1,12)
    
agree = st.checkbox("Aceptar términos y condiciones")
if agree:
    st.write("Ha aceptado")

if st.button("Enviar"):
    col2.markdown("Su información se ha enviado")