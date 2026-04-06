# Mendeteksi Bilangan Genap dan Ganjil dalam Array

arr = [9, 1, 3, 89, 20, 21, 30, 45, 55, 47, 102, 99, 33, 111]

print("DAFTAR BILANGAN:")
print(arr)
print("\n" + "="*50)
print("HASIL DETEKSI:")
print("="*50)

# Menampilkan setiap bilangan dengan status genap/ganjil
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        print(f"{arr[i]} -> bilangan GENAP")
    else:
        print(f"{arr[i]} -> bilangan GANJIL")

# Versi lebih ringkas dengan enumerate()
print("\n" + "="*50)
print("VERSI RINGKAS dengan enumerate():")
print("="*50)
for idx, nilai in enumerate(arr):
    status = "GENAP" if nilai % 2 == 0 else "GANJIL"
    print(f"Index {idx}: {nilai} adalah {status}")