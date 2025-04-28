import math

def kalkulator_2d():
    print("Pilih bangun datar:")
    print("1. Persegi")
    print("2. Segitiga")
    print("3. Trapesium")
    print("4. Lingkaran")
    print("5. Persegi Panjang")
    pilihan = input("Masukkan pilihan (1-5): ")

    if pilihan == "1":
        sisi = float(input("Masukkan panjang sisi: "))
        print(f"Luas Persegi: {sisi ** 2}")
    elif pilihan == "2":
        alas = float(input("Masukkan panjang alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        print(f"Luas Segitiga: {0.5 * alas * tinggi}")
    elif pilihan == "3":
        sisi_atas = float(input("Masukkan panjang sisi atas: "))
        sisi_bawah = float(input("Masukkan panjang sisi bawah: "))
        tinggi = float(input("Masukkan tinggi: "))
        print(f"Luas Trapesium: {0.5 * (sisi_atas + sisi_bawah) * tinggi}")
    elif pilihan == "4":
        jari_jari = float(input("Masukkan jari-jari: "))
        print(f"Luas Lingkaran: {math.pi * jari_jari ** 2}")
    elif pilihan == "5":
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))
        print(f"Luas Persegi Panjang: {panjang * lebar}")
    else:
        print("Pilihan tidak valid.")

def kalkulator_3d():
    print("Pilih bangun ruang:")
    print("1. Bola")
    print("2. Kubus")
    print("3. Balok")
    print("4. Tabung")
    print("5. Kerucut")
    pilihan = input("Masukkan pilihan (1-5): ")

    if pilihan == "1":
        jari_jari = float(input("Masukkan jari-jari: "))
        print(f"Volume Bola: {(4/3) * math.pi * jari_jari ** 3}")
    elif pilihan == "2":
        sisi = float(input("Masukkan panjang sisi: "))
        print(f"Volume Kubus: {sisi ** 3}")
    elif pilihan == "3":
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))
        tinggi = float(input("Masukkan tinggi: "))
        print(f"Volume Balok: {panjang * lebar * tinggi}")
    elif pilihan == "4":
        jari_jari = float(input("Masukkan jari-jari: "))
        tinggi = float(input("Masukkan tinggi: "))
        print(f"Volume Tabung: {math.pi * jari_jari ** 2 * tinggi}")
    elif pilihan == "5":
        jari_jari = float(input("Masukkan jari-jari: "))
        tinggi = float(input("Masukkan tinggi: "))
        print(f"Volume Kerucut: {(1/3) * math.pi * jari_jari ** 2 * tinggi}")
    else:
        print("Pilihan tidak valid.")


print("Kalkulator Bangun 2D dan 3D")
print("1. Bangun Datar (2D)")
print("2. Bangun Ruang (3D)")
pilihan = input("Masukkan pilihan (1-2): ")

if pilihan == "1":
    kalkulator_2d()
elif pilihan == "2":
    kalkulator_3d()
else:
    print("Pilihan tidak valid.")