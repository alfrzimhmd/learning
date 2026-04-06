# Mengakses dan Memodifikasi Elemen Matrix
# Matrix awal
matriks = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix awal:")
for baris in matriks:
    print(baris)

# Mengakses elemen di baris 1, kolom 2 (indeks 0,1)
elemen = matriks[0][1]
print(f"\nElemen di baris 1, kolom 2: {elemen}")

# Memodifikasi beberapa elemen
matriks[1][2] = 60   # baris 2, kolom 3 (indeks 1,2)
matriks[0][1] = 45   # baris 1, kolom 2 (indeks 0,1)
matriks[2][1] = 23   # baris 3, kolom 2 (indeks 2,1)

print("\nMatrix setelah modifikasi:")
for baris in matriks:
    print(baris)