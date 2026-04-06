# Penjumlahan Dua Matrix (Manual)
A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8, 9],
    [10, 11, 12]
]

print("Matrix A:")
for baris in A:
    print(baris)

print("\nMatrix B:")
for baris in B:
    print(baris)

# Menjumlahkan matrix
hasil_penjumlahan = []

for i in range(len(A)):          # Iterasi setiap baris
    baris = []
    for j in range(len(A[0])):   # Iterasi setiap kolom
        baris.append(A[i][j] + B[i][j])
    hasil_penjumlahan.append(baris)

print("\nHasil Penjumlahan Matrix A + B:")
for baris in hasil_penjumlahan:
    print(baris)