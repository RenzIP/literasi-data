import streamlit as st

st.title("Kalkulator BMI (Body Mass Index)")

st.write("Aplikasi ini akan menghitung BMI berdasarkan berat dan tinggi badan kamu.")

# Input dari user
berat = st.number_input("Masukkan berat badan (kg):", min_value=1.0)
tinggi_cm = st.number_input("Masukkan tinggi badan (cm):", min_value=1.0)

if st.button("Hitung BMI"):
    tinggi_m = tinggi_cm / 100
    bmi = berat / (tinggi_m ** 2)
    st.success(f"BMI kamu adalah {bmi:.2f}")

    # Kategori BMI
    if bmi < 18.5:
        st.warning("Kamu tergolong kekurangan berat badan.")
    elif 18.5 <= bmi < 25:
        st.info("Berat badan kamu normal.")
    elif 25 <= bmi < 30:
        st.warning("Kamu tergolong kelebihan berat badan.")
    else:
        st.error("Kamu tergolong obesitas.")
