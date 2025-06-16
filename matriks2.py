# Fungsi untuk menampilkan matriks
def tampil_matriks(matriks):
    for i in range(3):
        for j in range(3):
            print(matriks[i][j], end=" ")
        print()

# Fungsi untuk menghitung determinan dengan metode Sarus
def determinan_sarus(matriks):
    # Menghitung determinan menggunakan metode Sarus
    positif = (matriks[0][0] * matriks[1][1] * matriks[2][2] +
               matriks[0][1] * matriks[1][2] * matriks[2][0] +
               matriks[0][2] * matriks[1][0] * matriks[2][1])
    negatif = (matriks[0][2] * matriks[1][1] * matriks[2][0] +
               matriks[0][0] * matriks[1][2] * matriks[2][1] +
               matriks[0][1] * matriks[1][0] * matriks[2][2])
    determinan = positif - negatif
    return determinan

# Fungsi untuk menghitung determinan dengan metode Kofaktor
def determinan_kofaktor(matriks):
    # Menghitung kofaktor untuk setiap elemen baris pertama
    kofaktor_00 = matriks[1][1] * matriks[2][2] - matriks[1][2] * matriks[2][1]
    kofaktor_01 = -(matriks[1][0] * matriks[2][2] - matriks[1][2] * matriks[2][0])
    kofaktor_02 = matriks[1][0] * matriks[2][1] - matriks[1][1] * matriks[2][0]
    
    # Determinan = a11 * C11 + a12 * C12 + a13 * C13
    determinan = matriks[0][0] * kofaktor_00 + matriks[0][1] * kofaktor_01 + matriks[0][2] * kofaktor_02
    return determinan, kofaktor_00, kofaktor_01, kofaktor_02

# Membuat matriks kosong 3x3
matriks = [[0 for _ in range(3)] for _ in range(3)]

# Input elemen matriks dari pengguna
print("Masukkan elemen matriks 3x3:")
for i in range(3):
    for j in range(3):
        matriks[i][j] = float(input(f"Elemen [{i+1}][{j+1}]: "))

# Menampilkan matriks yang diinput
print("\nMatriks yang Anda masukkan:")
tampil_matriks(matriks)

# Menghitung determinan dengan metode Sarus
det_sarus = determinan_sarus(matriks)
print("\n=== Metode Sarus ===")
print(f"Determinan: {det_sarus}")
print("Langkah Sarus:")
print(f"Positif: ({matriks[0][0]} * {matriks[1][1]} * {matriks[2][2]}) + "
      f"({matriks[0][1]} * {matriks[1][2]} * {matriks[2][0]}) + "
      f"({matriks[0][2]} * {matriks[1][0]} * {matriks[2][1]})")
print(f"Negatif: ({matriks[0][2]} * {matriks[1][1]} * {matriks[2][0]}) + "
      f"({matriks[0][0]} * {matriks[1][2]} * {matriks[2][1]}) + "
      f"({matriks[0][1]} * {matriks[1][0]} * {matriks[2][2]})")

# Menghitung determinan dengan metode Kofaktor
det_kofaktor, kof_00, kof_01, kof_02 = determinan_kofaktor(matriks)
print("\n=== Metode Kofaktor ===")
print(f"Determinan: {det_kofaktor}")
print("Langkah Kofaktor:")
print(f"Kofaktor [1][1]: {kof_00}")
print(f"Kofaktor [1][2]: {kof_01}")
print(f"Kofaktor [1][3]: {kof_02}")
print(f"Determinan = {matriks[0][0]} * {kof_00} + {matriks[0][1]} * {kof_01} + {matriks[0][2]} * {kof_02}")