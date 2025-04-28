# Fungsi untuk menentukan ruangan berdasarkan usia
def check_room(age):
    # Jika usia lebih dari 20, masuk ke ruangan A
    if age > 20:
        return "Masuk ke ruangan A"
    # Jika usia lebih dari 12 tetapi kurang dari atau sama dengan 20, masuk ke ruangan B
    elif age > 12:
        return "Masuk ke ruangan B"
    # Jika usia 12 atau kurang, masuk ke ruangan C
    else:
        return "Masuk ke ruangan C"

# Contoh penggunaan fungsi check_room
print(check_room(25))  # Output: Masuk ke ruangan A
print(check_room(15))  # Output: Masuk ke ruangan B
print(check_room(10))  # Output: Masuk ke ruangan C


# Fungsi kalkulator sederhana untuk melakukan operasi aritmatika
def calc(a, b, operasi):
    # Jika operasi adalah penjumlahan
    if operasi == '+':
        return a + b
    # Jika operasi adalah pengurangan
    elif operasi == '-':
        return a - b
    # Jika operasi adalah perkalian
    elif operasi == '*':
        return a * b
    # Jika operasi adalah pembagian
    elif operasi == '/':
        return a / b
    # Jika operasi tidak valid
    else:
        return "Operasi tidak valid"

# Program utama untuk menggunakan fungsi kalkulator
print("=============== Calculator ===============")
# Meminta input angka pertama dari pengguna
a = int(input("Masukkan angka pertama: "))
# Meminta input angka kedua dari pengguna
b = int(input("Masukkan angka kedua: "))
# Meminta input operasi yang diinginkan dari pengguna
operasi = input("Masukkan operasi (+, -, *, /): ")
# Menghitung hasil menggunakan fungsi calc
result = calc(a, b, operasi)
# Menampilkan hasil perhitungan
print("Hasil:", result)