# Mengakses Elemen dalam Matrix
matrix = [
    [1, 2, 3],  # baris 0
    [4, 5, 6],  # baris 1
    [7, 8, 9],  # baris 2
]

print(matrix[0], "-> matrix index ke 0 (seluruh baris 0)")
print(matrix[0][1], "-> matrix index ke (0,1)")
print(matrix[2][2], "-> matrix index ke (2,2)")

# Menampilkan seluruh matrix
print("\nSeluruh matrix:")
print(matrix)

# Mengetahui ukuran matrix
rows = len(matrix)
cols = len(matrix[0])
print(f"\nUkuran matrix: {rows} baris x {cols} kolom")

# MEMBUAT MATRIX KOSONG DENGAN UKURAN TERTENTU (YANG BENAR)
matrix_kosong = [[0] * cols for _ in range(rows)]  # Perbaikan dari bug sebelumnya
print("\nMatrix kosong 3x3:")
for row in matrix_kosong:
    print(row)