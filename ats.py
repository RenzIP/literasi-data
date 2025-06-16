# SOAL NO 1
# Buat program Python untuk menghitung pajak penghasilan (PPh) seseorang berdasarkan penghasilan bulanan.

nama_pegawai = input("Masukkan nama pegawai: ")
gaji_bulanan = int(input("Masukkan gaji bulanan (Rp): "))

if gaji_bulanan <= 3000000:
    tarif_pajak = 0
elif 3000000 < gaji_bulanan <= 6000000:
    tarif_pajak = 0.05
elif 6000000 < gaji_bulanan <= 10000000:
    tarif_pajak = 0.10
else:
    tarif_pajak = 0.15

# Hitung jumlah pajak
pajak = gaji_bulanan * tarif_pajak

# Hitung gaji bersih
gaji_bersih = gaji_bulanan - pajak

print("Nama Pegawai:", nama_pegawai)
print("Gaji Bersih setelah pajak: Rp", int(gaji_bersih))


# SOAL NO 2
# Mebuat program untuk menghitung total biaya kirim berdasarka berat barang, dan membuat diskon jika total biaya lebih dari Rp.150.000, sebesar 10%

# Fungsi untuk menghitung biaya kirim
def hitung_biaya_kirim(berat):
    if 0 <= berat <= 5:
        biaya_per_kg = 20000
    elif 5 < berat <= 10:
        biaya_per_kg = 18000
    else:
        biaya_per_kg = 15000
    
    # Hitung total biaya sebelum diskon
    total_biaya = berat * biaya_per_kg
    
    # Cek apakah total biaya lebih dari Rp.150.000 untuk diskon
    if total_biaya > 150000:
        diskon = total_biaya * 0.10
        total_biaya -= diskon
    
    return total_biaya

# Input berat barang
berat = float(input("Masukkan berat barang (kg): "))

# Validasi input berat jika beratnya negatif
if berat < 0:
    print("Berat barang tidak boleh negatif!")
else:
    # Hitung total biaya menggunakan fungsi
    total_biaya = hitung_biaya_kirim(berat)
    print("Total biaya kirim: Rp", int(total_biaya))
