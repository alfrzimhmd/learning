# Operasi Dasar pada Array Python

arr = [9, 1, 3, 89, 20, 21, 30, 45, 55, 47, 102, 99, 33, 111]

print("ARRAY ORIGINAL:")
print(arr)

# 1. Mencari nilai maksimum dan minimum
print("\n" + "="*50)
print("1. NILAI EKSTREM:")
print("="*50)
print(f"Nilai maksimum: {max(arr)}")
print(f"Nilai minimum: {min(arr)}")

# 2. Mengurutkan array
print("\n" + "="*50)
print("2. PENGURUTAN:")
print("="*50)
print(f"Array ascending : {sorted(arr)}")
print(f"Array descending: {sorted(arr, reverse=True)}")

# 3. Operasi statistik
print("\n" + "="*50)
print("3. STATISTIK:")
print("="*50)
print(f"Total elemen    : {len(arr)}")
print(f"Jumlah semua     : {sum(arr)}")
print(f"Nilai rata-rata : {sum(arr)/len(arr):.2f}")

# 4. Filter data
print("\n" + "="*50)
print("4. FILTER DATA:")
print("="*50)
print(f"Angka > 50 : {[x for x in arr if x > 50]}")
print(f"Angka < 20 : {[x for x in arr if x < 20]}")
print(f"Angka antara 20-50: {[x for x in arr if 20 <= x <= 50]}")

# 5. Manipulasi array
print("\n" + "="*50)
print("5. MANIPULASI:")
print("="*50)
# Menambahkan elemen
arr_copy = arr.copy()
arr_copy.append(999)
print(f"Tambah 999 di akhir: {arr_copy}")
# Menyisipkan elemen
arr_copy.insert(0, 888)
print(f"Sisip 888 di awal : {arr_copy}")
# Menghapus elemen
arr_copy.remove(999)
print(f"Hapus 999         : {arr_copy}")