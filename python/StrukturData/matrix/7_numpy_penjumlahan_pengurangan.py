# Penjumlahan dan Pengurangan Matrix dengan Numpy
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

# Penjumlahan
C = A + B
print("\nPenjumlahan A + B:")
print(C)

# Pengurangan
D = A - B
print("\nPengurangan A - B:")
print(D)