# Array Multidimensi (Matrix) Sederhana

# Array 2 dimensi (seperti matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("ARRAY 2 DIMENSI (MATRIX 3x3):")
for baris in matrix:
    print(baris)

# Mengakses elemen
print("\n" + "="*50)
print("MENGAKSES ELEMEN:")
print("="*50)
print(f"matrix[0][0] (baris 1, kolom 1): {matrix[0][0]}")
print(f"matrix[1][2] (baris 2, kolom 3): {matrix[1][2]}")
print(f"matrix[2][1] (baris 3, kolom 2): {matrix[2][1]}")

# Iterasi array 2D
print("\n" + "="*50)
print("ITERASI ARRAY 2D:")
print("="*50)
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"matrix[{i}][{j}] = {matrix[i][j]}")

# Array 3 dimensi (sederhana)
print("\n" + "="*50)
print("ARRAY 3 DIMENSI:")
print("="*50)
arr_3d = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
]
print("Array 3D (2x2x2):")
print(arr_3d)
print(f"arr_3d[0][1][1] = {arr_3d[0][1][1]}")  # Mengakses elemen