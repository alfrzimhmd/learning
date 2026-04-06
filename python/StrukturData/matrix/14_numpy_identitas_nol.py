# Membuat Matrix Identitas dan Matrix Nol dengan Numpy
import numpy as np

# Matrix Identitas (hanya matrix persegi)
I_3 = np.identity(3)
print("Matrix Identitas 3x3:")
print(I_3)

I_4 = np.eye(4)  # Cara lain membuat identitas
print("\nMatrix Identitas 4x4:")
print(I_4)

# Matrix Nol (bisa berbagai ukuran)
Z_2x4 = np.zeros((2, 4))
print("\nMatrix Nol 2x4:")
print(Z_2x4)

Z_3x3 = np.zeros((3, 3))
print("\nMatrix Nol 3x3:")
print(Z_3x3)

# Matrix dengan nilai 1 (ones)
O_2x3 = np.ones((2, 3))
print("\nMatrix Ones 2x3:")
print(O_2x3)

# Matrix dengan nilai konstanta
K_2x2 = np.full((2, 2), 7)
print("\nMatrix 2x2 dengan nilai 7:")
print(K_2x2)