# Pengenalan Numpy untuk Matrix
import numpy as np

# Membuat matrix dari list bersarang
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("Matrix A:")
print(A)
print(f"\nTipe data: {type(A)}")
print(f"Shape matrix: {A.shape}")
print(f"Dimensi matrix: {A.ndim}D")
print(f"Jumlah elemen: {A.size}")