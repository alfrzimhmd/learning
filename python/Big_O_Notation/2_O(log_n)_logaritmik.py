"""
BIG O NOTATION: O(log n) - LOGARITMIK
Waktu eksekusi meningkat secara logaritmik.
Contoh: Binary Search (data harus sudah terurut).
"""

def binary_search(lst, target):
    """
    Mencari target dalam list terurut.
    Kompleksitas: O(log n) - setiap iterasi membagi data menjadi 2.
    """
    left, right = 0, len(lst) - 1
    iterasi = 0  # Untuk demonstrasi
    
    while left <= right:
        iterasi += 1
        mid = (left + right) // 2
        
        if lst[mid] == target:
            print(f"  (Ditemukan dalam {iterasi} iterasi)")
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    print(f"  (Tidak ditemukan, {iterasi} iterasi)")
    return -1

# Contoh penggunaan
my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]

print("="*50)
print("CONTOH O(log n) - BINARY SEARCH")
print("="*50)
print(f"List (terurut): {my_list}")
print(f"Panjang list: {len(my_list)} elemen")
print(f"\nMencari angka 9:")
result = binary_search(my_list, 9)
print(f"Elemen 9 ditemukan pada indeks {result}")

print(f"\nMencari angka 7:")
print(binary_search(my_list, 7))

print(f"\nMencari angka 2 (tidak ada):")
print(binary_search(my_list, 2))

# Demonstrasi efisiensi O(log n)
import math
print("\n" + "="*50)
print("EFISIENSI O(log n):")
print("="*50)
for n in [10, 100, 1000, 1000000]:
    iterasi_max = math.ceil(math.log2(n))
    print(f"n = {n:7d} -> maksimal iterasi = {iterasi_max} (log2({n}) ≈ {math.log2(n):.2f})")