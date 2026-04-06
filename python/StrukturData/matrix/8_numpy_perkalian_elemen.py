# Perkalian Elemen-dalam-Elemen (Element-wise) dengan Numpy
import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

B = np.array([
    [7, 8, 9],
    [10, 11, 12]
])

print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)

# Perkalian elemen-bij-elemen (bukan perkalian matrix)
hasil = A * B
print("\nHasil perkalian elemen-dalam-elemen A * B:")
print(hasil)
print("\nCatatan: Ini BUKAN perkalian matrix, tapi perkalian posisi yang sama")