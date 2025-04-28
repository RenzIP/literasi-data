# Looping dengan for
for i in range(5, 15, 2):
    print(f"loop ke-{i}")

hari = ["senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu"]

for i in hari :
    print(i)
    if i == "jumat":
        break

# Looping dengan while
i = 0
hari_kerja = hari[i]
while (hari_kerja != "sabtu") and (hari_kerja != "minggu"):
    print(hari_kerja)
    i += 1 
    hari_kerja = hari[i]
    if hari_kerja == "kamis":
        break

# nested loop
a = ["buku", "pensil", "penggaris"]
b = ["merah", "biru", "hijau"]
for i in a:
    for j in b:
        print(f"{i} {j}")
