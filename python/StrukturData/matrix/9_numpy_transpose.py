# Transpose Matrix dengan Numpy
import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("Matrix A (2x3):")
print(A)

# Cara 1: Menggunakan .T
transpose_A = A.T
print("\nTranspose Matrix A (3x2) dengan .T:")
print(transpose_A)

# Cara 2: Menggunakan fungsi np.transpose()
transpose_A_func = np.transpose(A)
print("\nTranspose Matrix A (3x2) dengan np.transpose():")
print(transpose_A_func)