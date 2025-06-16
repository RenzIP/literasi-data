import numpy as np

def welcome_message():
    print("==============================================")
    print("Selamat datang di Program Aljabar Linear Python!")
    print("Program ini dapat melakukan operasi matriks:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Invers Matriks")
    print("5. Determinan Matriks")
    print("6. Perkalian Matriks 3x3 dengan Metode Sarrus dan Kofaktor")
    print("==============================================")

def input_matrix(n=None, m=None, name="matriks"):
    if n is None or m is None:
        n = int(input(f"Masukkan jumlah baris {name}: "))
        m = int(input(f"Masukkan jumlah kolom {name}: "))
    print(f"Masukkan elemen-elemen {name} satu per satu:")
    mat = []
    for i in range(n):
        row = []
        for j in range(m):
            while True:
                try:
                    val = float(input(f"Elemen [{i+1},{j+1}]: "))
                    row.append(val)
                    break
                except:
                    print("Input tidak valid, masukkan angka.")
        mat.append(row)
    return np.array(mat)

def tanya_pakai_hasil(hasil, nama="hasil sebelumnya"):
    while True:
        tanya = input(f"Apakah Anda ingin menggunakan {nama} sebagai input matriks? (y/n): ").lower()
        if tanya == 'y':
            return hasil
        elif tanya == 'n':
            return None
        else:
            print("Input tidak valid, jawab 'y' atau 'n'.")

def penjumlahan(A, B):
    return A + B

def pengurangan(A, B):
    return A - B

def perkalian(A, B):
    return A @ B

def invers_numpy(A):
    try:
        inv = np.linalg.inv(A)
        return inv
    except np.linalg.LinAlgError:
        return None

def determinan_numpy(A):
    return np.linalg.det(A)

def determinan_sarrus_3x3(A):
    if A.shape != (3,3):
        print("Metode Sarrus hanya berlaku untuk matriks 3x3")
        return None
    a = A
    det = (a[0,0]*a[1,1]*a[2,2] +
           a[0,1]*a[1,2]*a[2,0] +
           a[0,2]*a[1,0]*a[2,1]) - \
          (a[0,2]*a[1,1]*a[2,0] +
           a[0,0]*a[1,2]*a[2,1] +
           a[0,1]*a[1,0]*a[2,2])
    return det

def kofaktor(A):
    if A.shape != (3,3):
        print("Metode kofaktor ini hanya untuk matriks 3x3")
        return None
    cof = np.zeros((3,3))
    for i in range(3):
        for j in range(3):
            minor = np.delete(np.delete(A, i, axis=0), j, axis=1)
            cof[i,j] = ((-1)**(i+j)) * np.linalg.det(minor)
    return cof

def invers_kofaktor_3x3(A):
    det = determinan_sarrus_3x3(A)
    if det == 0:
        print("Matriks singular, tidak bisa dihitung inversnya")
        return None
    cof = kofaktor(A)
    adj = cof.T
    inv = adj / det
    return inv

def main():
    welcome_message()
    last_result = None
    
    while True:
        print("\nPilih operasi matriks yang ingin dilakukan:")
        print("1. Penjumlahan matriks")
        print("2. Pengurangan matriks")
        print("3. Perkalian matriks")
        print("4. Invers matriks")
        print("5. Determinan matriks")
        print("6. Perkalian matriks 3x3 dengan metode Sarrus dan Kofaktor")
        print("0. Keluar")
        
        pilihan = input("Masukkan pilihan (0-6): ")
        if pilihan == '0':
            print("Terima kasih sudah menggunakan program ini. Sampai jumpa!")
            break
        
        if pilihan in ['1','2','3']:
            A = None
            if last_result is not None:
                A = tanya_pakai_hasil(last_result, "hasil sebelumnya sebagai matriks pertama")
            if A is None:
                A = input_matrix()
            
            if pilihan == '3':
                # Perkalian matriks: kolom A harus sama dengan baris B
                while True:
                    B = input_matrix()
                    if A.shape[1] != B.shape[0]:
                        print(f"Jumlah kolom matriks pertama ({A.shape[1]}) harus sama dengan jumlah baris matriks kedua ({B.shape[0]}). Coba lagi.")
                    else:
                        break
            else:
                B = input_matrix(A.shape[0], A.shape[1], "matriks kedua")
            
            if pilihan == '1':
                hasil = penjumlahan(A, B)
                print("Hasil penjumlahan matriks:")
            elif pilihan == '2':
                hasil = pengurangan(A, B)
                print("Hasil pengurangan matriks:")
            else:
                hasil = perkalian(A, B)
                print("Hasil perkalian matriks:")
            print(hasil)
            last_result = hasil
        
        elif pilihan == '4':
            A = None
            if last_result is not None:
                A = tanya_pakai_hasil(last_result, "hasil sebelumnya")
            if A is None:
                A = input_matrix()
            
            print("Pilih metode invers:")
            print("1. Menggunakan numpy.linalg.inv()")
            print("2. Metode kofaktor (hanya matriks 3x3)")
            m = input("Masukkan pilihan metode (1/2): ")
            if m == '1':
                inv = invers_numpy(A)
                if inv is None:
                    print("Matriks tidak memiliki invers (singular).")
                    last_result = None
                else:
                    print("Invers matriks (numpy):")
                    print(inv)
                    last_result = inv
            elif m == '2':
                if A.shape != (3,3):
                    print("Metode kofaktor hanya untuk matriks 3x3")
                    last_result = None
                    continue
                inv = invers_kofaktor_3x3(A)
                if inv is not None:
                    print("Invers matriks (metode kofaktor):")
                    print(inv)
                    last_result = inv
                else:
                    last_result = None
            else:
                print("Pilihan metode tidak valid.")
                last_result = None
        
        elif pilihan == '5':
            A = None
            if last_result is not None:
                A = tanya_pakai_hasil(last_result, "hasil sebelumnya")
            if A is None:
                A = input_matrix()
            
            print("Pilih metode determinan:")
            print("1. Menggunakan numpy.linalg.det()")
            print("2. Metode Sarrus (hanya matriks 3x3)")
            m = input("Masukkan pilihan metode (1/2): ")
            if m == '1':
                det = determinan_numpy(A)
                print(f"Determinan matriks (numpy): {det:.4f}")
            elif m == '2':
                if A.shape != (3,3):
                    print("Metode Sarrus hanya untuk matriks 3x3")
                    continue
                det = determinan_sarrus_3x3(A)
                print(f"Determinan matriks (Sarrus): {det:.4f}")
            else:
                print("Pilihan metode tidak valid.")
            # Determinan bukan matriks, jadi tidak simpan last_result
        
        elif pilihan == '6':
            print("Input matriks pertama (3x3):")
            A = input_matrix(3,3, "matriks pertama")
            print("Input matriks kedua (3x3):")
            B = input_matrix(3,3, "matriks kedua")
            
            print("Menghitung perkalian matriks 3x3 dengan metode Sarrus dan kofaktor:")
            
            hasil_np = perkalian(A, B)
            print("Hasil perkalian matriks (numpy):")
            print(hasil_np)
            
            print("\nDeterminan matriks pertama (Sarrus):", determinan_sarrus_3x3(A))
            print("Determinan matriks kedua (Sarrus):", determinan_sarrus_3x3(B))
            
            print("\nCatatan: Metode Sarrus dan Kofaktor hanya berlaku untuk determinan dan invers 3x3,")
            print("perkalian matriks biasa menggunakan operator '@' numpy.")
            last_result = hasil_np
        
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
