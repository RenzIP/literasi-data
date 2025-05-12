import random
import time

# Konfigurasi
awalan = "+62821"           # Awalan yang ditentukan
jumlah_digit = 8        # Jumlah digit angka acak setelah awalan

def generate_random_number(awalan, jumlah_digit):
    angka = ''.join(random.choices("0123456789", k=jumlah_digit))
    return f"{awalan}{angka}"

try:
    while True:
        hasil = generate_random_number(awalan, jumlah_digit)
        print(hasil)
        time.sleep(0.1)  # jeda 0.5 detik (bisa disesuaikan)
except KeyboardInterrupt:
    print("\nProgram dihentikan oleh pengguna.")
