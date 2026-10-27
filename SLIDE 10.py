# Definisi fungsi dengan parameter default (usia = 17)
def print_info(nama, usia=17):
  """Fungsi ini menampilkan7info yang dimasukkan"""
  print("Nama: ", nama)
  print("Usia ", usia)

# Memanggil fungsi dengan menentukan nilai usia secara spesifik
print_info(usia=19, nama="TALITA")

# Memanggil fungsi tanpa menyediakan argumen usia (otomatis menggunakan 17)
print_info(nama="TALITA")