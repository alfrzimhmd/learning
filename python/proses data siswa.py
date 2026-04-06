import pandas as pd

def proses_data_siswa():
    """Memproses data siswa menggunakan pandas DataFrame."""

    # Membuat dictionary yang berisi data siswa
    data_siswa = {
        'Nama': ["Ali", "Budi", "Cindy", "Doni", "Eka"],  # Nama siswa
        'Umur': [15, 16, 15, 16, 17],                     # Umur siswa
        'Nilai Ujian': [70, 85, 90, 75, 80]              # Nilai ujian siswa
    }

    # Membuat DataFrame dari dictionary data_siswa
    df = pd.DataFrame(data_siswa)

    # Menampilkan semua data siswa
    print("Data Seluruh Siswa:")
    print(df)

    # Menghitung rata-rata nilai ujian dari kolom 'Nilai Ujian'
    rata_rata = df['Nilai Ujian'].mean()
    print(f"\nRata-rata nilai ujian: {rata_rata:.2f}")  # Menampilkan rata-rata dengan 2 desimal

    # Memfilter siswa yang memiliki nilai ujian di atas rata-rata
    siswa_di_atas_rata_rata = df[df['Nilai Ujian'] > rata_rata]

    # Menampilkan siswa dengan nilai di atas rata-rata
    print("\nSiswa dengan nilai di atas rata-rata:")
    print(siswa_di_atas_rata_rata)  # Menampilkan DataFrame siswa di atas rata-rata

    # Menampilkan jumlah siswa yang memiliki nilai di atas rata-rata
    print(f"\nJumlah siswa di atas rata-rata: {len(siswa_di_atas_rata_rata)} siswa")

# Memanggil fungsi proses_data_siswa() untuk menjalankan program
proses_data_siswa()