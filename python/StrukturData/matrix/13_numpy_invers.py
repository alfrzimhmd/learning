# Menghitung Invers Matrix dengan Numpy
import numpy as np

# Matrix harus persegi dan determinan != 0
A = np.array([
    [1, 2],
    [3, 4]
])

print("Matrix A:")
print(A)
print(f"Determinan A: {np.linalg.det(A):.2f}")

# Menghitung invers
try:
    invers = np.linalg.inv(A)
    print("\nInvers Matrix A:")
    print(invers)
    
    # Verifikasi: A * invers = identitas
    identitas = A @ invers
    print("\nVerifikasi A x invers (seharusnya matrix identitas):")
    print(identitas.round(2))
    
except np.linalg.LinAlgError:
    print("Matrix tidak memiliki invers (singular)")

# Contoh matrix yang tidak memiliki invers
B = np.array([
    [1, 2],
    [2, 4]
])
print("\nMatrix B (singular):")
print(B)
print(f"Determinan B: {np.linalg.det(B):.2f}")