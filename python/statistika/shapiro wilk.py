import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns
from tabulate import tabulate

print("=" * 60)
print("UJI NORMALITAS SHAPIRO-WILK")
print("=" * 60)

# INPUT DATA DENGAN VALIDASI
while True:
    print("\nPILIHAN DATA:")
    print("1. Gunakan Contoh Data NORMAL [65, 70, 75, 80, 85, 78, 72, 82]")
    print("2. Gunakan Contoh Data TIDAK NORMAL [10, 12, 15, 18, 20, 22, 25, 100]")
    print("3. Input data manual")
    print("CATATAN: Jumlah data harus genap untuk input data manual")

    pilihan = input("Pilih opsi (1/2/3): ").strip()

    if pilihan == "1":
        data = np.array([65, 70, 75, 80, 85, 78, 72, 82])
        print("Menggunakan data contoh NORMAL")
        break
    elif pilihan == "2":
        data = np.array([10, 12, 15, 18, 20, 22, 25, 100])
        print("Menggunakan data contoh TIDAK NORMAL")
        break
    elif pilihan == "3":
        data_input = input('Masukkan data (pisahkan dengan koma): ').strip()
        try:
            data = np.array([float(x.strip()) for x in data_input.split(',')])
            if len(data) < 3:
                print("Error: Jumlah data minimal 3 untuk uji Shapiro-Wilk")
                continue
            if len(data) % 2 != 0:
                print("PERINGATAN: Jumlah data ganjil. Untuk perhitungan manual yang akurat, disarankan menggunakan jumlah data genap.")
                print("Program akan tetap berjalan, tetapi hasil mungkin tidak optimal.")
            print(f"Data yang dimasukkan: {data}")
            break
        except ValueError:
            print("Error: Data yang dimasukkan salah! Pastikan data berupa angka yang dipisahkan koma.")
            continue
    else:
        print("Pilihan tidak valid! Silakan pilih 1, 2, atau 3.")
        continue

print(f"Data yang digunakan: {data}")
print(f"n (jumlah data): {len(data)}")

# LANGKAH 1: PENGURUTAN DATA
print("\n" + "="*50)
print("LANGKAH 1: PENGURUTAN DATA")
print("="*50)

data_terurut = np.sort(data)
print(f"Data asli: {data}")
print(f"Data terurut (xᵢ): {data_terurut}")

tabel_langkah1 = []
for i, nilai in enumerate(data_terurut, 1):
    tabel_langkah1.append([f"x{i}", nilai, f"Data ke-{i} dari terkecil"])

print("\nTabel Data Terurut:")
print(tabulate(tabel_langkah1, headers=["Notasi", "Nilai", "Keterangan"], tablefmt="grid"))

# LANGKAH 2: MENGHITUNG MEAN (RATA-RATA)
print("\n" + "="*50)
print("LANGKAH 2: MENGHITUNG MEAN (RATA-RATA)")
print("="*50)

print("Rumus: Mean = Σxᵢ / n")
print("Dimana:")
print("Σxᵢ = jumlah semua nilai data")
print("n = jumlah sampel")

jumlah_data = sum(data_terurut)
n = len(data_terurut)
mean = jumlah_data / n

print(f"\nΣxᵢ = { ' + '.join(map(str, data_terurut)) } = {jumlah_data}")
print(f"n = {n}")
print(f"Mean = {jumlah_data} / {n} = {mean}")

print(f"\nHasil: Mean = {mean}")

# LANGKAH 3: MENGHITUNG Σ(xᵢ - mean)²
print("\n" + "="*50)
print("LANGKAH 3: MENGHITUNG Σ(xᵢ - mean)²")
print("="*50)

print("PENJELASAN:")
print("Σ(xᵢ - mean)² adalah jumlah kuadrat selisih setiap data dengan mean.")
print("Ini mengukur seberapa jauh data-data menyebar dari rata-ratanya.")
print("Dalam uji Shapiro-Wilk, nilai ini digunakan sebagai penyebut dalam")
print("perhitungan statistik W.")

print("\nLangkah perhitungan:")
print("1. Hitung selisih setiap data dengan mean: (xᵢ - mean)")
print("2. Kuadratkan selisihnya: (xᵢ - mean)²")
print("3. Jumlahkan semua kuadrat selisih: Σ(xᵢ - mean)²")

selisih_kuadrat = [(x - mean)**2 for x in data_terurut]
sum_squares = sum(selisih_kuadrat)

print("\nCONTOH PERHITUNGAN UNTUK DATA PERTAMA (x₁):")
x1 = data_terurut[0]
selisih_x1 = x1 - mean
kuadrat_x1 = selisih_x1 ** 2
print(f"x₁ = {x1}")
print(f"x₁ - mean = {x1} - {mean} = {selisih_x1}")
print(f"(x₁ - mean)² = ({selisih_x1})² = {kuadrat_x1}")

print("\nPERHITUNGAN DETAIL UNTUK SEMUA DATA:")
tabel_langkah3 = []
for i, (x, sq) in enumerate(zip(data_terurut, selisih_kuadrat), 1):
    selisih = x - mean
    tabel_langkah3.append([f"x{i}", x, selisih, sq])

print(tabulate(tabel_langkah3,
               headers=["Data", "xᵢ", "xᵢ - mean", "(xᵢ - mean)²"],
               tablefmt="grid"))

print(f"\nPENJUMLAHAN SEMUA NILAI (xᵢ - mean)²:")
nilai_kuadrat_list = [f"{sq}" for sq in selisih_kuadrat]
penjumlahan_str = " + ".join(nilai_kuadrat_list)
print(f"{penjumlahan_str} = {sum_squares}")

print(f"\nHASIL: Σ(xᵢ - mean)² = {sum_squares}")

print(f"\nMAKNA HASIL:")
print(f"Nilai {sum_squares} menunjukkan total penyebaran data dari rata-rata.")
print(f"Semakin besar nilai ini, semakin tersebar data-data.")

# LANGKAH 4: POLA PEMASANGAN DATA & KOEFISIEN aᵢ
print("\n" + "="*50)
print("LANGKAH 4: POLA PEMASANGAN DATA & KOEFISIEN aᵢ")
print("="*50)

print("PENJELASAN:")
print("Dalam uji Shapiro-Wilk, data dipasangkan untuk memeriksa simetri distribusi.")
print("Prinsip pemasangan data berdasarkan urutan sebagai berikut:")
print("- Data terkecil dipasangkan dengan data terbesar (x₁ dengan x₈)")
print("- Data kedua terkecil dengan data kedua terbesar (x₂ dengan x₇)")
print("- Dan seterusnya hingga semua data berpasangan")
print("")
print("Pemilihan pola ini didasarkan pada fakta bahwa dalam distribusi normal,")
print("data seharusnya simetris terhadap mean. Jika data normal, selisih antara")
print("pasangan data ekstrem seharusnya konsisten dengan pola yang diharapkan.")
print("")
print("Notasi:")
print("- xᵢ = data ke-i dari yang terkecil")
print("- x₍ₙ₊₁₋ᵢ₎ = data ke-i dari yang terbesar") 
print("- aᵢ = koefisien dari tabel Shapiro-Wilk")
print("")
print("Koefisien aᵢ sudah ditentukan oleh penelitian statistik dan berbeda")
print("untuk setiap ukuran sampel. Koefisien ini memberikan bobot yang lebih")
print("besar pada pasangan data ekstrem karena pasangan inilah yang paling")
print("sensitif dalam mendeteksi penyimpangan dari normalitas.")

n = len(data_terurut)

def get_a_coefficients(n):
    """Mengembalikan koefisien aᵢ untuk Shapiro-Wilk berdasarkan n"""
    coefficients = {
        3: [0.7071],
        4: [0.6872, 0.1677],
        5: [0.6646, 0.2413, 0.0000],
        6: [0.6431, 0.2806, 0.0875],
        7: [0.6233, 0.3031, 0.1401, 0.0000],
        8: [0.6052, 0.3164, 0.1743, 0.0561],
        9: [0.5888, 0.3244, 0.1976, 0.0947, 0.0000],
        10: [0.5739, 0.3291, 0.2141, 0.1224, 0.0399]
    }
    return coefficients.get(n, [0.5] * ((n + 1) // 2))

a_coeff = get_a_coefficients(n)

print("\nTABEL KOEFISIEN aᵢ UNTUK BERBAGAI n:")
print("Nilai koefisien ini ditentukan oleh Shapiro dan Wilk melalui penelitian:")
tabel_koefisien = [
    [3, "[0.7071]"],
    [4, "[0.6872, 0.1677]"],
    [5, "[0.6646, 0.2413, 0.0000]"],
    [6, "[0.6431, 0.2806, 0.0875]"],
    [7, "[0.6233, 0.3031, 0.1401, 0.0000]"],
    [8, "[0.6052, 0.3164, 0.1743, 0.0561]"],
    [9, "[0.5888, 0.3244, 0.1976, 0.0947, 0.0000]"],
    [10, "[0.5739, 0.3291, 0.2141, 0.1224, 0.0399]"]
]
print(tabulate(tabel_koefisien, headers=["n", "Koefisien aᵢ"], tablefmt="grid"))

print(f"\nKOEFISIEN UNTUK n = {n}: {a_coeff}")

print("\nCONTOH PERHITUNGAN UNTUK PASANGAN PERTAMA:")
print(f"x₁ = {data_terurut[0]} (data terkecil)")
print(f"x₈ = {data_terurut[7]} (data terbesar)")
print(f"x₈ - x₁ = {data_terurut[7]} - {data_terurut[0]} = {data_terurut[7] - data_terurut[0]}")
print(f"a₁ = {a_coeff[0]} (dari tabel koefisien untuk n={n})")

print("\nTABEL POLA PEMASANGAN DATA:")
tabel_pasangan = []
for i in range(n//2):
    x_kecil = data_terurut[i]
    x_besar = data_terurut[n-1-i]
    selisih = x_besar - x_kecil
    a_i = a_coeff[i]

    tabel_pasangan.append([
        i+1, f"x{i+1}", x_kecil, f"x{n-i}", x_besar,
        selisih, f"{a_i:.4f}"
    ])

print(tabulate(tabel_pasangan,
               headers=["i", "Notasi Kecil", "Nilai", "Notasi Besar", "Nilai", "Selisih", "aᵢ"],
               tablefmt="grid"))

print(f"\nPENJELASAN:")
print(f"Kolom 'aᵢ' berisi koefisien dari tabel Shapiro-Wilk untuk n={n}")
print(f"Koefisien a₁ paling besar ({a_coeff[0]}) karena pasangan terluar (data terkecil")
print(f"dan terbesar) paling penting untuk mendeteksi normalitas. Pasangan ini")
print(f"paling sensitif terhadap keberadaan outlier dan ketidaksimetrian distribusi.")

# LANGKAH 5: MENGHITUNG b = Σ[aᵢ × (x₍ₙ₊₁₋ᵢ₎ - xᵢ)]
print("\n" + "="*50)
print("LANGKAH 5: MENGHITUNG b = Σ[aᵢ × (x₍ₙ₊₁₋ᵢ₎ - xᵢ)]")
print("="*50)

print("PENJELASAN:")
print("Menghitung komponen b dengan rumus:")
print("b = Σ[aᵢ × (x₍ₙ₊₁₋ᵢ₎ - xᵢ)]")
print("")
print("Langkah perhitungan:")
print("1. Untuk setiap pasangan, kalikan koefisien aᵢ dengan selisih pasangan")
print("2. Jumlahkan semua hasil perkalian tersebut")
print("")
print("Nilai b mengukur keselarasan data dengan pola distribusi normal.")
print("Nilai b yang besar menunjukkan bahwa data memiliki pola yang mendekati")
print("distribusi normal, sedangkan nilai b yang kecil menunjukkan penyimpangan.")

print("\nCONTOH PERHITUNGAN UNTUK PASANGAN PERTAMA:")
contoh_hasil = a_coeff[0] * (data_terurut[7] - data_terurut[0])
contoh_hasil_bulat = round(contoh_hasil, 4)
print(f"a₁ × (x₈ - x₁) = {a_coeff[0]} × ({data_terurut[7]} - {data_terurut[0]})")
print(f"= {a_coeff[0]} × {data_terurut[7] - data_terurut[0]} = {contoh_hasil_bulat}")

total_b = 0
print("\nPERHITUNGAN LENGKAP UNTUK SEMUA PASANGAN:")

tabel_langkah5 = []
for i in range(n//2):
    x_kecil = data_terurut[i]
    x_besar = data_terurut[n-1-i]
    selisih = x_besar - x_kecil
    a_i = a_coeff[i]
    b_i = a_i * selisih
    b_i_bulat = round(b_i, 4)
    total_b += b_i_bulat  

    tabel_langkah5.append([
        i+1, f"{a_i:.4f}", selisih, f"{b_i_bulat:.4f}"
    ])

print(tabulate(tabel_langkah5,
               headers=["i", "aᵢ", "Selisih", "aᵢ × Selisih"],
               tablefmt="grid"))

print(f"\nPENJUMLAHAN SEMUA NILAI aᵢ × Selisih:")
b_values = [a_coeff[i] * (data_terurut[n-1-i] - data_terurut[i]) for i in range(n//2)]
b_values_str = " + ".join([f"{bv:.4f}" for bv in b_values])
print(f"{b_values_str} = {total_b:.4f}")

print(f"\nHASIL: b = Σ[aᵢ × selisih] = {total_b:.4f}")

print(f"\nMAKNA HASIL:")
print(f"Nilai b = {total_b:.4f} menunjukkan tingkat keselarasan data dengan pola normal.")
print(f"Semakin besar nilai b, semakin normal data karena menunjukkan bahwa")
print(f"pola pemasangan data sesuai dengan yang diharapkan dalam distribusi normal.")
print(f"Pada distribusi normal yang sempurna, nilai b akan maksimal karena")
print(f"selisih pasangan data proporsional dengan koefisien aᵢ.")

# LANGKAH 6: MENGHITUNG STATISTIK W
print("\n" + "="*50)
print("LANGKAH 6: MENGHITUNG STATISTIK W")
print("="*50)

print("PENJELASAN:")
print("Menghitung statistik W dengan rumus:")
print("W = b² / Σ(xᵢ - mean)²")
print("")
print("Dimana:")
print("- b² = kuadrat dari komponen b (Langkah 5)")
print("- Σ(xᵢ - mean)² = penyebaran data (Langkah 3)")
print("")
print("Statistik W selalu bernilai antara 0 dan 1.")
print("Semakin mendekati 1, semakin normal distribusi data.")

W = (total_b ** 2) / sum_squares

print("\nPERHITUNGAN:")
print(f"b² = ({total_b:.4f})² = {total_b**2:.4f}")
print(f"Σ(xᵢ - mean)² = {sum_squares}")
print(f"W = {total_b**2:.4f} / {sum_squares} = {W:.4f}")

print(f"\nHASIL: Statistik W = {W:.4f}")

# LANGKAH 7: MEMBANDINGKAN DENGAN NILAI KRITIS
print("\n" + "="*50)
print("LANGKAH 7: MEMBANDINGKAN DENGAN NILAI KRITIS")
print("="*50)

print("PENJELASAN:")
print("Nilai kritis Shapiro-Wilk diperoleh dari tabel statistik yang telah")
print("ditetapkan melalui penelitian ekstensif. Nilai-nilai ini berbeda untuk")
print("setiap ukuran sampel (n) dan tingkat signifikansi (α).")
print("")
print("Untuk α = 0.05 (tingkat kepercayaan 95%), nilai kritis menunjukkan")
print("batas minimum statistik W untuk menyimpulkan data berdistribusi normal.")
print("Jika W hitung lebih besar atau sama dengan W kritis, maka data dianggap")
print("berdistribusi normal. Sebaliknya, jika W hitung lebih kecil dari W kritis,")
print("maka data tidak berdistribusi normal.")

def get_critical_value(n):
    critical_values = {
        3: 0.767, 4: 0.748, 5: 0.762, 6: 0.788, 7: 0.803, 8: 0.818,
        9: 0.829, 10: 0.842, 11: 0.850, 12: 0.859, 13: 0.866, 14: 0.874,
        15: 0.881, 16: 0.887, 17: 0.892, 18: 0.897, 19: 0.901, 20: 0.905,
        25: 0.918, 30: 0.927, 35: 0.934, 40: 0.940, 45: 0.945, 50: 0.947
    }
    return critical_values.get(n, 0.950)

W_kritis = get_critical_value(n)

print("\nTABEL NILAI KRITIS SHAPIRO-WILK (α = 0.05):")
tabel_kritis = [
    [3, 0.767], [4, 0.748], [5, 0.762], [6, 0.788], [7, 0.803], [8, 0.818],
    [9, 0.829], [10, 0.842], [15, 0.881], [20, 0.905], [25, 0.918], [30, 0.927],
    [35, 0.934], [40, 0.940], [45, 0.945], [50, 0.947]
]
print(tabulate(tabel_kritis, headers=["n", "W kritis"], tablefmt="grid", floatfmt=".3f"))

print(f"\nPERBANDINGAN UNTUK n = {n}:")
print(f"W hitung  = {W:.4f}")
print(f"W kritis = {W_kritis:.4f}")

# LANGKAH 8: PENGAMBILAN KEPUTUSAN
print("\n" + "="*50)
print("LANGKAH 8: PENGAMBILAN KEPUTUSAN")
print("="*50)

print("Hipotesis:")
print("H₀: Data berdistribusi normal")
print("H₁: Data tidak berdistribusi normal")
print("α = 0.05")

print("\nKriteria Pengambilan Keputusan:")
print("Jika W hitung ≥ W kritis → Gagal tolak H₀ (Data normal)")
print("Jika W hitung < W kritis → Tolak H₀ (Data tidak normal)")

if W >= W_kritis:
    keputusan = "GAGAL TOLAK H₀"
    kesimpulan = "Data berdistribusi normal"
    
    print(f"\nKEPUTUSAN STATISTIK:")
    print(f"Berdasarkan perbandingan antara statistik W hitung ({W:.4f}) dengan nilai kritis ({W_kritis:.4f}),")
    print(f"dan mengingat W hitung ≥ W kritis, maka hipotesis nol (H₀) gagal ditolak.")
    
    print(f"\nINTERPRETASI:")
    print(f"Data menunjukkan pola yang konsisten dengan distribusi normal. Karakteristik data")
    print(f"seperti simetri, kemiringan, dan keruncingan sesuai dengan yang diharapkan dari")
    print(f"distribusi normal.")
    
    print(f"\nIMPLIKASI:")
    print(f"Karena data berdistribusi normal, metode statistik parametrik seperti uji-t, ANOVA,")
    print(f"atau analisis regresi dapat digunakan dengan valid.")
    
else:
    keputusan = "TOLAK H₀"
    kesimpulan = "Data tidak berdistribusi normal"
    
    print(f"\nKEPUTUSAN STATISTIK:")
    print(f"Berdasarkan perbandingan antara statistik W hitung ({W:.4f}) dengan nilai kritis ({W_kritis:.4f}),")
    print(f"dan mengingat W hitung < W kritis, maka hipotesis nol (H₀) ditolak.")
    
    print(f"\nINTERPRETASI:")
    print(f"Data tidak mengikuti pola distribusi normal. Kemungkinan terdapat outlier,")
    print(f"data miring (skewed), atau pola tidak simetris yang menyebabkan ketidaknormalan.")
    
    print(f"\nIMPLIKASI:")
    print(f"Karena data tidak berdistribusi normal, disarankan menggunakan metode statistik")
    print(f"non-parametrik atau melakukan transformasi data sebelum analisis lebih lanjut.")

print(f"\nKESIMPULAN: {kesimpulan}")

# LANGKAH 9: VISUALISASI DATA
print("\n" + "="*50)
print("LANGKAH 9: VISUALISASI DATA")
print("="*50)

fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Plot 1: Histogram dengan kurva normal
axes[0, 0].hist(data, bins=min(8, len(data)//2), density=True, alpha=0.7, 
                color='skyblue', edgecolor='black')
xmin, xmax = axes[0, 0].get_xlim()
x = np.linspace(xmin, xmax, 100)
p = stats.norm.pdf(x, mean, np.std(data, ddof=1))
axes[0, 0].plot(x, p, 'r-', linewidth=2, label='Kurva Normal Teoritis')
axes[0, 0].axvline(mean, color='green', linestyle='--', label=f'Mean = {mean:.2f}')
axes[0, 0].set_title('Histogram dan Kurva Normal')
axes[0, 0].set_xlabel('Nilai')
axes[0, 0].set_ylabel('Density')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)

# Plot 2: Q-Q Plot
stats.probplot(data, dist="norm", plot=axes[0, 1])
axes[0, 1].set_title('Q-Q Plot\n(Pengecekan Normalitas Visual)')
axes[0, 1].grid(True, alpha=0.3)

# Plot 3: Box Plot
axes[1, 0].boxplot(data, vert=True, patch_artist=True)
axes[1, 0].set_title('Box Plot\n(Deteksi Outlier)')
axes[1, 0].set_ylabel('Nilai')
axes[1, 0].grid(True, alpha=0.3)

# Plot 4: Summary Hasil
axes[1, 1].axis('off')
summary_text = f"""
HASIL UJI NORMALITAS SHAPIRO-WILK

Data: {data}
n = {n}

STATISTIK:
• Mean     = {mean:.2f}
• Std Dev  = {np.std(data, ddof=1):.2f}
• W hitung = {W:.4f}
• W kritis = {W_kritis:.4f}

KEPUTUSAN:
• {keputusan}
• {kesimpulan}
"""
axes[1, 1].text(0.1, 0.9, summary_text, transform=axes[1, 1].transAxes,
                fontsize=12, verticalalignment='top', fontfamily='monospace',
                bbox=dict(boxstyle="round,pad=0.5", facecolor="lightyellow" if W >= W_kritis else "lightcoral"))

plt.tight_layout()
plt.savefig('shapiro_wilk_analysis.png', dpi=300, bbox_inches='tight')
plt.show()


print("PENJELASAN VISUALISASI:")
print("Visualisasi data membantu memahami pola distribusi secara grafis")
print("dan melengkapi hasil uji statistik formal. Terdapat tiga jenis grafik:")
print("")
print("1. HISTOGRAM DENGAN KURVA NORMAL:")
print("   - Menampilkan distribusi frekuensi data")
print("   - Garis merah menunjukkan kurva normal teoritis")
print("   - Garis hijau putus-putus menunjukkan posisi mean")
print("   - Jika histogram mengikuti kurva normal, indikasi data normal")
print("")
print("2. Q-Q PLOT (Quantile-Quantile Plot):")
print("   - Membandingkan quantile data dengan quantile distribusi normal")
print("   - Titik-titik yang mendekati garis lurus menunjukkan data normal")
print("   - Penyimpangan dari garis lurus menunjukkan ketidaknormalan")
print("")
print("3. BOX PLOT:")
print("   - Menampilkan ringkasan distribusi data")
print("   - Kotak menunjukkan interquartile range (IQR)")
print("   - Garis dalam kotak menunjukkan median")
print("   - Whisker menunjukkan range data normal")
print("   - Titik di luar whisker menunjukkan outlier")

# LAPORAN AKHIR
print("\n" + "="*60)
print("LAPORAN ANALISIS NORMALITAS SELESAI")
print("="*60)

print(f"""
SUMMARY HASIL ANALISIS:

DATA PENELITIAN    : {data}
JUMLAH SAMPEL      : {n}
STATISTIK W        : {W:.4f}
NILAI KRITIS       : {W_kritis:.4f}
HASIL UJI         : {kesimpulan}
TINGKAT SIGNIFIKANSI : α = 0.05

REKOMENDASI:
{'Data berdistribusi normal. Dapat menggunakan statistik parametrik.' 
 if W >= W_kritis else 
 'Data tidak berdistribusi normal. Disarankan menggunakan statistik non-parametrik atau transformasi data.'}
""")

print("Analisis selesai. Hasil dapat digunakan untuk laporan penelitian.")