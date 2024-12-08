import qrcode
import streamlit as st
import os

# Directorio para guardar el QR generado
output_dir = "qr_codes"
os.makedirs(output_dir, exist_ok=True)  # Crear el directorio si no existe
filename = os.path.join(output_dir, "qr_code.png")

def generate_qr_code(url, filename):
    """
    Genera un código QR a partir de una URL y lo guarda como imagen.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

# Configuración de la página
st.set_page_config(page_title="QR Code Generator", page_icon="🌐", layout="centered")
st.title("QR Code Generator")

# Mostrar imagen de encabezado (asegúrate de ajustar la ruta a tu imagen)
image_path = "images/supports.JPG"  # Cambia según la ubicación real
if os.path.exists(image_path):
    st.image(image_path, use_column_width=True)
else:
    st.warning("Imagen no encontrada. Asegúrate de colocar 'supports.JPG' en el directorio 'images'.")

# Entrada de URL
url = st.text_input("Enter the URL")

# Botón para generar código QR
if st.button("Generate QR Code"):
    if url:
        generate_qr_code(url, filename)
        st.image(filename, caption="Generated QR Code", use_column_width=True)
        
        # Descargar QR
        with open(filename, "rb") as f:
            image_data = f.read()
        st.download_button(
            label="Download QR",
            data=image_data,
            file_name="qr_generated.png",
            mime="image/png"
        )
    else:
        st.error("Please enter a valid URL!")
