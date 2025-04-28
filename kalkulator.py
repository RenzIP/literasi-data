pi = 3.14 # nilai pi

def bangun_2d(): # function untuk mempermudah dalam memilih kalkulator 2d
    print("Pilih bangun datar:")
    print("1. Persegi")
    print("2. Segitiga")
    print("3. Trapesium")
    print("4. Lingkaran")
    print("5. Persegi Panjang")
    pilihan = input("Silahkan di pilih: ")

    if pilihan == "1": # Menghitung luas persegi
        sisi = int(input("Masukkan panjang sisi: "))
        print("Luas Persegi: ", sisi ** 2)
        
    elif pilihan == "2": # Menghitung luas segitiga
        alas = int(input("Masukkan panjang alas: "))
        tinggi = int(input("Masukkan tinggi: "))
        print("Luas Segitiga: ",0.5 * alas * tinggi)
        
    elif pilihan == "3": # Menghitung luas trapesium
        sisi_atas = int(input("Masukkan panjang sisi atas: "))
        sisi_bawah = int(input("Masukkan panjang sisi bawah: "))
        tinggi = int(input("Masukkan tinggi: "))
        print("Luas Trapesium: ", 0.5 * (sisi_atas + sisi_bawah) * tinggi)
        
    elif pilihan == "4": # Menghitung luas jari- jari linkaran
        jari_jari = float(input("Masukkan jari-jari: "))
        print("Luas Lingkaran: ", pi * jari_jari ** 2)
        
    elif pilihan == "5": # Menghitung luas persegi panjang
        panjang = int(input("Masukkan panjang: "))
        lebar = int(input("Masukkan lebar: "))
        print("Luas Persegi Panjang: ", panjang * lebar)
        
    else: # tidak valid
        print("Pilihan tidak valid.")

def bangun_3d(): # function untuk mempermudah dalam memilih kalkulator 3d
    print("Pilih bangun ruang:")
    print("1. Bola")
    print("2. Kubus")
    print("3. Balok")
    print("4. Tabung")
    print("5. Kerucut")
    pilihan = input("Silahkan di Pilih: ")

    if pilihan == "1": # Menghitung volume bola
        jari_jari = int(input("Masukkan jari-jari: "))
        print("Volume Bola: ", (4/3) * pi * jari_jari ** 3)
        
    elif pilihan == "2": # Menghitung volume kubus
        sisi = int(input("Masukkan panjang sisi: "))
        print("Volume Kubus: ", sisi ** 3)
        
    elif pilihan == "3": # Menghitung volume balok
        panjang = int(input("Masukkan panjang: "))
        lebar = int(input("Masukkan lebar: "))
        tinggi = int(input("Masukkan tinggi: "))
        print("Volume Balok: ", panjang * lebar * tinggi)
        
    elif pilihan == "4": # Menghitung volume tabung
        jari_jari = int(input("Masukkan jari-jari: "))
        tinggi = int(input("Masukkan tinggi: "))
        print("Volume Tabung: ", pi * jari_jari ** 2 * tinggi)
        
    elif pilihan == "5": # Menghitung volume kerucut
        jari_jari = int(input("Masukkan jari-jari: "))
        tinggi = int(input("Masukkan tinggi: "))
        print("Volume Kerucut: ", (1/3) * pi * jari_jari ** 2 * tinggi)
        
    else: # tidak valid
        print("Pilihan tidak valid.")


print ("=============== Kalkulator Bangun Datar dan Ruang ===============")
print ("Silahan pilih jenis kalkulator:")
print ("1. Kalkulator Bangun Datar")
print ("2. Kalkulator Bangun Ruang")
pilihan = input("Silahkan Pilih: ")

if pilihan == "1": # Memanggil fungsi kalkulator 2D
    bangun_2d()
elif pilihan == "2": # Memanggil fungsi kalkulator 3D
    bangun_3d()
else: # tidak valid
    print("Pilihan tidak valid.")