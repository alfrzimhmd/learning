# Transpose Matrix (Manual)
# Matrix A (2x3)
A = [
    [1, 2, 3],
    [4, 5, 6]
]

print("Matrix A (2x3):")
for baris in A:
    print(baris)

# Membuat matrix transpose (3x2) dengan nilai 0
transpose_A = [
    [0, 0],
    [0, 0],
    [0, 0]
]

# Melakukan transpose: baris menjadi kolom, kolom menjadi baris
for i in range(len(A)):          # Baris matrix asli
    for j in range(len(A[0])):   # Kolom matrix asli
        transpose_A[j][i] = A[i][j]

print("\nTranspose Matrix A (3x2):")
for baris in transpose_A:
    print(baris)