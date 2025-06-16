# If Else Conditionalsx

cantarella = "Istri"

inputan = input("Siapa cantarella?: ")
if inputan == cantarella:
    print("Cantarella adalah istri saya")
elif inputan == "Pacar":
    print("Cantarella adalah pacar saya")
else:
    print("Cantarella bukan istri atau pacar saya")


def cek_cantarella():
    if inputan == cantarella:
        return "Cantarella adalah istri saya"
    elif inputan == "Pacar":
        return "Cantarella adalah pacar saya"
    else:
        return "Cantarella bukan istri atau pacar saya"

print(cek_cantarella())
    
