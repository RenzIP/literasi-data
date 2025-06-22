import streamlit as st
import os
import re
from pathlib import Path

# Folder penyimpanan lokal
SAVE_DIR = "save_pdfs"
Path(SAVE_DIR).mkdir(parents=True, exist_ok=True)

st.title("📄 Upload Surat Pernyataan (PDF)")
st.markdown("**Format nama file:** `[NamaLengkap]-[NPM]-surat_pernyataan.pdf`")

# Upload PDF
uploaded_file = st.file_uploader("Unggah file PDF", type=["pdf"])

if uploaded_file is not None:
    filename = uploaded_file.name

    # Cek apakah sesuai format
    pattern = r'^([A-Za-z]+(?:-[A-Za-z]+)*)-(\d+)-surat_pernyataan\.pdf$'
    if re.match(pattern, filename):
        save_path = os.path.join(SAVE_DIR, filename)

        # Simpan ke folder lokal
        with open(save_path, "wb") as f:
            f.write(uploaded_file.read())

        st.success(f"✅ File berhasil diunggah dan disimpan sebagai `{filename}`.")
        st.info(f"📁 Lokasi penyimpanan: `{save_path}`")
    else:
        st.error("❌ Nama file tidak sesuai format. Contoh yang benar: `Gilar-1214055-surat_pernyataan.pdf`")
