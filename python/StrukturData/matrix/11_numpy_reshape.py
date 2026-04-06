# Mengubah Bentuk Matrix (Reshape) dengan Numpy
import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("Matrix A (2x3):")
print(A)
print(f"Shape: {A.shape}")

# Transpose
hasil = A.T
print("\nTranspose A (3x2):")
print(hasil)
print(f"Shape setelah transpose: {hasil.shape}")

# Reshape ke bentuk lain
B = A.reshape(3, 2)  # Ubah dari 2x3 menjadi 3x2
print("\nReshape A menjadi 3x2:")
print(B)

# Flatten (ubah menjadi 1 dimensi)
C = A.flatten()
print("\nFlatten A (1 dimensi):")
print(C)