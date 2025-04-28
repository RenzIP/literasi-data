def check_room(age):
    if age > 20:
        return "Masuk ke ruangan A"
    elif age > 12:
        return "Masuk ke ruangan B"
    else:
        return "Masuk ke ruangan C"

# Contoh penggunaan
print(check_room(25))  # Output: Masuk ke ruangan A
print(check_room(15))  # Output: Masuk ke ruangan B
print(check_room(10))  # Output: Masuk ke ruangan C


def calc (a,b, operasi):
    if operasi == '+':
        return a + b
    elif operasi == '-':
        return a - b
    elif operasi == '*':
        return a * b
    elif operasi == '/':
        return a / b
    else:
        return "Operasi tidak valid"
    
print("=============== Calculator ===============")
a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
operasi = input("Masukkan operasi (+, -, *, /): ")
result = calc(a, b, operasi)
print("Hasil:", result)