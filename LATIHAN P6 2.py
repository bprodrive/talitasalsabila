x = int(input("Masukan Nilai 1= "))
y = int(input("Masukan Nilai 2= "))
print("")

def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Pemanggilan fungsi dan cetak hasil
print("Penjumlahan:", tambah(x, y))
print("Pengurangan:", kurang(x, y))
print("Perkalian:", kali(x, y))
print("Pembagian:", bagi(x, y))