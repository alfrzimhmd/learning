# Daftar angka
arr = [9, 1, 3, 89, 20, 21, 30, 45, 55, 47, 102, 99, 33, 111]

# Inisialisasi jumlah bilangan genap dan ganjil
sum_genap = 0
sum_ganjil = 0

# Iterasi melalui setiap elemen dalam daftar
for i in range(len(arr)):
    nilai = arr[i]  # Mendapatkan nilai elemen pada indeks i
    if nilai % 2 == 0:
        sum_genap += nilai
        print(nilai, "adalah bilangan genap")
    else:
        sum_ganjil += nilai
        print(nilai, "adalah bilangan ganjil")

# Mencetak jumlah total bilangan genap dan ganjil setelah loop selesai
print("\nJumlah bilangan genap adalah:", sum_genap)
print("Jumlah bilangan ganjil adalah:", sum_ganjil)