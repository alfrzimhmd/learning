"""
BIG O NOTATION: O(n) - LINEAR
Waktu eksekusi proporsional dengan ukuran input.
Contoh: Linear Search, iterasi sederhana.
"""

def cari_elemen(lst, target):
    """
    Mencari target dengan memeriksa satu per satu.
    Kompleksitas: O(n) - dalam kasus terburuk, harus cek semua elemen.
    """
    for index, item in enumerate(lst):
        if item == target:
            return index
    return -1

# Contoh penggunaan
my_list = [10, 20, 30, 40, 50]

print("="*50)
print("CONTOH O(n) - LINEAR SEARCH")
print("="*50)
print(f"List: {my_list}")
print(f"Mencari 30: index ke-{cari_elemen(my_list, 30)}")  # Output: 2
print(f"Mencari 60: {cari_elemen(my_list, 60)}")  # Output: -1

# Demonstrasi pertumbuhan waktu O(n)
import time

def linear_search_demo(n):
    """Mencari elemen terakhir (kasus terburuk)"""
    lst = list(range(n))
    start = time.time()
    cari_elemen(lst, n-1)  # Cari elemen terakhir
    end = time.time()
    return (end - start) * 1000  # dalam milidetik

print("\n" + "="*50)
print("PERTUMBUHAN WAKTU O(n):")
print("="*50)
for n in [1000, 10000, 100000, 1000000]:
    waktu = linear_search_demo(n)
    print(f"n = {n:7d} -> waktu: {waktu:.4f} ms")