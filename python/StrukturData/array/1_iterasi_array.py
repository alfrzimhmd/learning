# Cara Iterasi/Mengakses Elemen Array dalam Python

arr = [9, 1, 3, 89, 20, 21, 30, 45, 55, 47, 102, 99, 33, 111]

print("="*50)
print("CARA PERTAMA: Menggunakan enumerate()")
print("="*50)
# enumerate() memberikan index dan value secara bersamaan
for i, v in enumerate(arr):
    print(f"index ke : {i} -> value: {v}")

print("\n" + "="*50)
print("CARA KEDUA: Menggunakan range(len(arr))")
print("="*50)
# Cara klasik dengan index
for i in range(len(arr)):
    print(f"index ke : {i} -> value: {arr[i]}")

print("\n" + "="*50)
print("CARA KETIGA: Menggunakan counter manual")
print("="*50)
# Manual counter (jarang digunakan tapi valid)
index = 0
for v in arr:
    print(f"index ke : {index} -> value: {v}")
    index += 1

print("\n" + "="*50)
print("Rekomendasi: Gunakan enumerate() karena paling Pythonic!")
print("="*50)