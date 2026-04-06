"""
BIG O NOTATION: O(n!) - FAKTORIAL
Waktu eksekusi sangat cepat memburuk.
Contoh: Menghasilkan semua permutasi.
"""

def permutasi(s):
    """
    Menghasilkan semua permutasi dari string s.
    Kompleksitas: O(n!) - jumlah permutasi = n!
    """
    if len(s) == 1:
        return [s]
    else:
        hasil = []
        for i in range(len(s)):
            for p in permutasi(s[:i] + s[i+1:]):
                hasil.append(s[i] + p)
        return hasil

# Contoh penggunaan
print("="*50)
print("CONTOH O(n!) - PERMUTASI")
print("="*50)

for char in ['A', 'AB', 'ABC', 'ABCD']:
    import time
    start = time.time()
    hasil = permutasi(char)
    end = time.time()
    print(f"String '{char:<4}' -> {len(hasil)} permutasi | Waktu: {(end-start)*1000:.2f} ms")

print("\n" + "="*50)
print("PERTUMBUHAN JUMLAH PERMUTASI:")
print("="*50)
for n in range(1, 11):
    import math
    print(f"n = {n:2d} -> {n}! = {math.factorial(n):10,d} permutasi")
    
print("\n n=10 sudah 3.6 juta permutasi!")
print("n=20 akan menghasilkan 2.4 QUINTILLION permutasi (tidak mungkin)")