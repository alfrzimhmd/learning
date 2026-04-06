# Perkalian Matrix (Dot Product) dengan Numpy
import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print("Matrix A (2x2):")
print(A)
print("\nMatrix B (2x2):")
print(B)

# Cara 1: Menggunakan np.dot()
hasil = np.dot(A, B)
print("\nHasil perkalian matrix A x B (dengan np.dot()):")
print(hasil)

# Cara 2: Menggunakan operator @ (Python 3.5+)
hasil2 = A @ B
print("\nHasil perkalian matrix A x B (dengan operator @):")
print(hasil2)

# Contoh dengan ukuran berbeda
C = np.array([[1, 2, 3], [4, 5, 6]])  # 2x3
D = np.array([[7, 8], [9, 10], [11, 12]])  # 3x2
print("\nMatrix C (2x3):")
print(C)
print("\nMatrix D (3x2):")
print(D)
print("\nHasil C x D (2x2):")
print(C @ D)