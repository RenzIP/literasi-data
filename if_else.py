# If And Else

# nilai = int(input("Berapa nilainya?"))

# if nilai >= 80:
#     print("kamu lulus dengan nilai A", nilai)
# elif nilai >= 70:
#     print("kamu lulus dengan nilai B", nilai)
# elif nilai >= 60:
#     print("kamu lulus dengan nilai C", nilai)
# elif nilai >= 50:
#     print("kamu lulus dengan nilai D", nilai)
# elif nilai < 40:
#     print("Kamu lulus dengan nilai E", nilai)
# else :
#     print("Kamu tidak lulus", nilai)

# =======================================================================================================================================================================

def format_rupiah(angka):
    angka = int(angka)
    return f"Rp. {angka:,},-".replace(",", ".")

# total_belanja = int(input("berapa total belanja kamu? "))

# if total_belanja >= 200000:
#     print("Selamat! Anda mendapatkan diskon 10%")
#     diskon = total_belanja * 0.10
# elif total_belanja >= 100000:
#     print("Selamat! Anda mendapatkan diskon 5%")
#     diskon = total_belanja * 0.05
# else:
#     print("Anda tidak mendapatkan diskon")
#     diskon = 0
# print (format_rupiah(diskon))
# print ("Total belanja setelah diskon:", format_rupiah(total_belanja - diskon))

# ========================================================================================================================================================================

# Belanja
nama = str(input("Masukan Nama kamu = "))
B = int(input("Kamu sudah berapa belanja berapa banyak? "))

if B >= 500000:
    cashback = 0.20 * B
    kategori = "Platinum"
elif B >= 400000:
    cashback = 0.15 * B
    kategori = "Gold"
elif B >= 300000:
    cashback = 0.10 * B
    kategori = "Silver"
elif B >= 200000:
    cashback = 0.05 * B
    kategori = "Bronze"
else:
    cashback = 0
    kategori = "Timah"

print("==============================================================================")
print("Berikut adalah data Belanja kamu")
print ("nama            :", nama)
print ("Kategori        :", kategori)
jumlah_belanja = B
print("Jumlah belanja   :", format_rupiah(jumlah_belanja))
print("Cashback         :", format_rupiah(cashback))
bayar = jumlah_belanja - cashback
print("Yang di bayar    :", format_rupiah(bayar))

# ========================================================================================================================================================================
