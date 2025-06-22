import streamlit as st
from PIL import Image

st.title("🖼️ Aplikasi Upload & Preview Gambar")

# Upload file gambar
uploaded_file = st.file_uploader("Pilih gambar untuk diunggah", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Buka dan tampilkan gambar
    image = Image.open(uploaded_file)
    st.image(image, caption="Gambar yang diunggah", use_column_width=True)
    st.success("Gambar berhasil diunggah!")
else:
    st.info("Silakan unggah file gambar (jpg, jpeg, png)")
