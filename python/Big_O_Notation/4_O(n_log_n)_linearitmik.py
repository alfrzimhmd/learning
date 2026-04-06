"""
BIG O NOTATION: O(n log n) - LINEARITMIK
Waktu eksekusi n dikali log n.
Contoh: Merge Sort, Quick Sort (rata-rata).
"""

def merge_sort(lst):
    """
    Mengurutkan list dengan algoritma Merge Sort.
    Kompleksitas: O(n log n) - lebih efisien dari O(n²).
    """
    if len(lst) > 1:
        mid = len(lst) // 2
        L = lst[:mid]
        R = lst[mid:]

        merge_sort(L)  # Rekursif kiri
        merge_sort(R)  # Rekursif kanan

        i = j = k = 0

        # Merge dua sublist yang sudah terurut
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                lst[k] = L[i]
                i += 1
            else:
                lst[k] = R[j]
                j += 1
            k += 1

        # Sisa elemen dari L
        while i < len(L):
            lst[k] = L[i]
            i += 1
            k += 1

        # Sisa elemen dari R
        while j < len(R):
            lst[k] = R[j]
            j += 1
            k += 1

# Contoh penggunaan
my_list = [38, 27, 43, 3, 15, 82, 10, 8, 67]

print("="*50)
print("CONTOH O(n log n) - MERGE SORT")
print("="*50)
print(f"Sebelum sorting: {my_list}")
merge_sort(my_list)
print(f"Setelah sorting: {my_list}")

# Perbandingan dengan sorting bawaan Python (Timsort, juga O(n log n))
import time
import random

print("\n" + "="*50)
print("PERBANDINGAN EFISIENSI:")
print("="*50)

for n in [1000, 10000, 50000]:
    data = [random.randint(1, 10000) for _ in range(n)]
    
    # Copy untuk masing-masing sorting
    data_merge = data.copy()
    data_builtin = data.copy()
    
    start = time.time()
    merge_sort(data_merge)
    end = time.time()
    waktu_merge = end - start
    
    start = time.time()
    data_builtin.sort()
    end = time.time()
    waktu_builtin = end - start
    
    print(f"n = {n:5d} -> Merge Sort: {waktu_merge*1000:.2f} ms, Built-in: {waktu_builtin*1000:.2f} ms")