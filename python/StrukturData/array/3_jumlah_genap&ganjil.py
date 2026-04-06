# Menjumlahkan Seluruh Bilangan Genap dan Ganjil dalam Array

# Daftar angka
arr = [9, 1, 3, 89, 20, 21, 30, 45, 55, 47, 102, 99, 33, 111]

# Inisialisasi jumlah
sum_genap = 0
sum_ganjil = 0

print("DAFTAR ANGKA:")
print(arr)
print("\n" + "="*50)
print("PROSES PENJUMLAHAN:")
print("="*50)

# Iterasi dan menjumlah
for i in range(len(arr)):
    nilai = arr[i]
    if nilai % 2 == 0:
        sum_genap += nilai
        print(f"{nilai} (GENAP) -> ditambahkan ke sum_genap (total sementara: {sum_genap})")
    else:
        sum_ganjil += nilai
        print(f"{nilai} (GANJIL) -> ditambahkan ke sum_ganjil (total sementara: {sum_ganjil})")

# Mencetak hasil akhir
print("\n" + "="*50)
print("HASIL AKHIR:")
print("="*50)
print(f"Jumlah seluruh bilangan GENAP : {sum_genap}")
print(f"Jumlah seluruh bilangan GANJIL: {sum_ganjil}")
print(f"Jumlah keseluruhan             : {sum_genap + sum_ganjil}")

# Verifikasi dengan fungsi sum() bawaan Python
print("\n" + "="*50)
print("VERIFIKASI:")
print("="*50)
print(f"Sum semua elemen dengan sum(arr): {sum(arr)}")
print(f"Jumlah genap + ganjil            : {sum_genap + sum_ganjil}")
print(f"✓ Hasil sesuai!" if sum(arr) == sum_genap + sum_ganjil else "⚠️ Ada ketidaksesuaian!")

# Menampilkan statistik tambahan
print("\n" + "="*50)
print("STATISTIK TAMBAHAN:")
print("="*50)
print(f"Total elemen array: {len(arr)}")
print(f"Jumlah bilangan genap: {len([x for x in arr if x % 2 == 0])} buah")
print(f"Jumlah bilangan ganjil: {len([x for x in arr if x % 2 == 1])} buah")
print(f"Rata-rata genap: {sum_genap / len([x for x in arr if x % 2 == 0]):.2f}" if sum_genap > 0 else "Tidak ada genap")
print(f"Rata-rata ganjil: {sum_ganjil / len([x for x in arr if x % 2 == 1]):.2f}" if sum_ganjil > 0 else "Tidak ada ganjil")