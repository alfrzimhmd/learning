# Menghitung Determinan Matrix dengan Numpy
import numpy as np

# Determinan hanya untuk matrix persegi (n x n)
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [4, 6, 2],
    [3, 1, 5],
    [7, 8, 9]
])

print("Matrix A (2x2):")
print(A)
determinan_A = np.linalg.det(A)
print(f"Determinan A: {determinan_A:.2f}")

print("\nMatrix B (3x3):")
print(B)
determinan_B = np.linalg.det(B)
print(f"Determinan B: {determinan_B:.2f}")

# Contoh matrix singular (determinan = 0)
C = np.array([
    [1, 2],
    [2, 4]
])
print("\nMatrix C (2x2 - singular):")
print(C)
print(f"Determinan C: {np.linalg.det(C):.2f}")