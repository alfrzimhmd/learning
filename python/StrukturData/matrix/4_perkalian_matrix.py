# Perkalian Dua Matrix (Manual)
# Syarat: jumlah kolom A = jumlah baris B
# Hasil: (baris A) x (kolom B)

# Matrix A (2x3)
A = [
    [1, 2, 3],
    [4, 5, 6]
]

# Matrix B (3x2)
B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

print("Matrix A (2x3):")
for baris in A:
    print(baris)

print("\nMatrix B (3x2):")
for baris in B:
    print(baris)

# Inisialisasi matrix hasil (2x2) dengan nilai 0
hasil_perkalian = [
    [0, 0],
    [0, 0]
]

# Perkalian matrix
for i in range(len(A)):          # Baris matrix A
    for j in range(len(B[0])):   # Kolom matrix B
        for k in range(len(B)):   # Elemen yang dikalikan
            hasil_perkalian[i][j] += A[i][k] * B[k][j]

print("\nHasil Perkalian Matrix A x B:")
for baris in hasil_perkalian:
    print(baris)