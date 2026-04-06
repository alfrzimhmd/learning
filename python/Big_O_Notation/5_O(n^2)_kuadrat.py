"""
BIG O NOTATION: O(n²) - KUADRAT
Waktu eksekusi proporsional dengan n².
Contoh: Bubble Sort, Selection Sort, nested loop.
"""

def bubble_sort(lst):
    """
    Mengurutkan dengan Bubble Sort (tidak efisien untuk data besar).
    Kompleksitas: O(n²) - ada nested loop.
    """
    n = len(lst)
    iterasi = 0  # Untuk demonstrasi
    
    for i in range(n):
        for j in range(0, n-i-1):
            iterasi += 1
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    
    print(f"  (Total iterasi: {iterasi} untuk n={n})")
    return lst

# Contoh penggunaan
my_list = [64, 34, 25, 12, 22, 11, 90]

print("="*50)
print("CONTOH O(n²) - BUBBLE SORT")
print("="*50)
print(f"Sebelum sorting: {my_list}")
bubble_sort(my_list)
print(f"Setelah sorting: {my_list}")

# Demonstrasi pertumbuhan O(n²)
import time

print("\n" + "="*50)
print("PERTUMBUHAN WAKTU O(n²):")
print("="*50)
for n in [100, 500, 1000, 2000]:
    data = list(range(n, 0, -1))  # Data terbalik (kasus terburuk)
    start = time.time()
    bubble_sort(data.copy())
    end = time.time()
    print(f"n = {n:4d} -> waktu: {(end-start)*1000:.2f} ms")

print("\nPerhatikan: Ketika n digandakan, waktu menjadi ~4x lipat!")