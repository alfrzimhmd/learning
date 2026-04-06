"""
BIG O NOTATION: O(√n) - AKAR KUADRAT
Waktu eksekusi proporsional dengan akar kuadrat dari n.
Contoh: Pengecekan bilangan prima (optimized).
"""

import math

def is_prime(n):
    """
    Mengecek apakah n adalah bilangan prima.
    Kompleksitas: O(√n) - hanya perlu cek sampai √n.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # PERBAIKAN: Hanya cek sampai √n, dan return True setelah loop selesai
    for i in range(3, int(math.sqrt(n)) + 1, 2):  # Hanya angka ganjil
        if n % i == 0:
            return False
    return True  # ← Perbaikan: indentasi ini penting!

# Contoh penggunaan
print("="*50)
print("CONTOH O(√n) - PENGECEKAN BILANGAN PRIMA")
print("="*50)

angka = [29, 100, 2, 17, 97, 1, 101, 49]
for num in angka:
    status = "PRIMA" if is_prime(num) else "BUKAN PRIMA"
    print(f"{num:3d} -> {status}")

print("\n" + "="*50)
print("EFISIENSI O(√n):")
print("="*50)

def cek_prima_dengan_counter(n):
    """Versi dengan counter untuk demonstrasi"""
    if n <= 1:
        return False, 0
    if n == 2:
        return True, 0
    if n % 2 == 0:
        return False, 1
    
    counter = 0
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        counter += 1
        if n % i == 0:
            return False, counter
    return True, counter

for n in [101, 10007, 100003, 1000003]:
    prima, iterasi = cek_prima_dengan_counter(n)
    print(f"n = {n:8d} -> √n ≈ {math.sqrt(n):.0f} -> iterasi = {iterasi:4d} -> {prima}")