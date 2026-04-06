"""
BIG O NOTATION: O(2ⁿ) - EKSPONENSIAL
Waktu eksekusi berlipat ganda setiap penambahan input.
Contoh: Fibonacci rekursif (tanpa memoization).
"""

import time

def fibonacci(n):
    """
    Menghitung bilangan Fibonacci ke-n secara rekursif.
    Kompleksitas: O(2ⁿ) - sangat lambat untuk n besar.
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_dengan_counter(n, counter):
    """Versi dengan counter untuk demonstrasi"""
    counter[0] += 1
    if n <= 1:
        return n
    else:
        return fibonacci_dengan_counter(n-1, counter) + fibonacci_dengan_counter(n-2, counter)

# Contoh penggunaan
print("="*50)
print("CONTOH O(2ⁿ) - FIBONACCI REKURSIF")
print("="*50)

for n in [5, 10, 15, 20, 30]:
    counter = [0]
    start = time.time()
    hasil = fibonacci_dengan_counter(n, counter)
    end = time.time()
    print(f"fib({n:2d}) = {hasil:8d} | Panggilan fungsi: {counter[0]:8d} | Waktu: {(end-start)*1000:.2f} ms")

print("\n" + "="*50)
print("EFISIENSI O(2ⁿ):")
print("="*50)
print("n=40  -> bisa memakan waktu MENITAN!")
print("n=100 -> tidak akan selesai dalam ribuan tahun!")

# Versi efisien (menggunakan memoization/dinamis)
def fibonacci_efisien(n, memo={}):
    """Versi O(n) dengan memoization"""
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_efisien(n-1, memo) + fibonacci_efisien(n-2, memo)
    return memo[n]

print("\n" + "="*50)
print("PERBANDINGAN DENGAN VERSI EFISIEN (O(n)):")
print("="*50)
start = time.time()
hasil = fibonacci_efisien(100)
end = time.time()
print(f"fib(100) dengan O(n) = {hasil} (waktu: {(end-start)*1000:.2f} ms)")
print("✓ Perbedaan sangat drastis!")