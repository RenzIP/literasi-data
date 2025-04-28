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
    
    if operasi == '+': # Jika operasi adalah penjumlahan
        print("Ini adalah penjumlahan")
        return a + b
    
    elif operasi == '-': # Jika operasi adalah pengurangan
        print("Ini adalah pengurangan")
        return a - b
    
    elif operasi == '*': # Jika operasi adalah perkalian
        print("Ini adalah perkalian")
        return a * b
    
    elif operasi == '/': # Jika operasi adalah pembagian
        print("Ini adalah pembagian")
        if b != 0:
                return a / b
        else :
            return "Pembagian dengan nol tidak diperbolehkan"
    
    elif operasi == '%': # Jika operasi adalah modulus
        print("Ini adalah modulus")
        return a % b
    
    else: # Jika operasi tidak valid
        return "Operasi tidak valid"


print("=============== Calculator ===============") # Program utama untuk menggunakan fungsi kalkulator

a = int(input("Masukkan angka pertama: ")) # Meminta input angka pertama dari pengguna

b = int(input("Masukkan angka kedua: ")) # Meminta input angka kedua dari pengguna

operasi = input("Masukkan operasi (+, -, *, /, %): ") # Meminta input operasi yang diinginkan dari pengguna

result = calc(a, b, operasi) # Menghitung hasil menggunakan fungsi calc

print("Hasil:", result) # Menampilkan hasil perhitungan