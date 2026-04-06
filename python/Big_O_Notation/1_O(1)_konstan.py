"""
BIG O NOTATION: O(1) - KONSTAN
Waktu eksekusi tetap, tidak tergantung pada ukuran input.
Contoh: Akses elemen array berdasarkan index.
"""

def akses_elemen(lst, index):
    """
    Mengakses elemen pada index tertentu.
    Kompleksitas: O(1) - selalu 1 operasi berapapun ukuran list.
    """
    return lst[index]

# Contoh penggunaan
my_list = [10, 20, 30, 40, 50]

print("="*50)
print("CONTOH O(1) - AKSES ELEMEN ARRAY")
print("="*50)
print(f"List: {my_list}")
print(f"Akses index 2: {akses_elemen(my_list, 2)}")  # Output: 30
print(f"Akses index 4: {akses_elemen(my_list, 4)}")  # Output: 50

# Demonstrasi bahwa waktu eksekusi tetap konstan
import time

small_list = [1, 2, 3]
large_list = list(range(1000000))

start = time.time()
akses_elemen(small_list, 0)
end = time.time()
print(f"\nAkses list kecil (3 elemen): {(end-start)*1000:.6f} ms")

start = time.time()
akses_elemen(large_list, 999999)
end = time.time()
print(f"Akses list besar (1jt elemen): {(end-start)*1000:.6f} ms")
print("✓ Waktu hampir sama! Ini bukti O(1)")