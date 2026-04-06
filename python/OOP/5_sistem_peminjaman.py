"""
SISTEM PEMINJAMAN BUKU
Menggabungkan semua konsep OOP (Class, Encapsulation, Inheritance, Polymorphism)
"""

from datetime import datetime
from typing import List, Optional


class Buku:
    """Class Buku - Representasi buku di perpustakaan"""
    
    def __init__(self, judul: str, penulis: str, tahun: int, stok: int = 1):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun
        self.__stok = stok  # Private attribute
        self.__dipinjam = 0  # Jumlah yang sedang dipinjam
    
    def info(self) -> str:
        return f"'{self.judul}' oleh {self.penulis} ({self.tahun})"
    
    def info_lengkap(self) -> str:
        status = "Tersedia" if self.tersedia else "Habis"
        return f"{self.info()} - {status} (Stok: {self.__stok - self.__dipinjam}/{self.__stok})"
    
    @property
    def tersedia(self) -> bool:
        return (self.__stok - self.__dipinjam) > 0
    
    def pinjam(self) -> bool:
        """Meminjam buku (mengurangi stok)"""
        if self.tersedia:
            self.__dipinjam += 1
            return True
        return False
    
    def kembalikan(self) -> None:
        """Mengembalikan buku (menambah stok)"""
        if self.__dipinjam > 0:
            self.__dipinjam -= 1
    
    def __str__(self) -> str:
        return self.info()


class Anggota:
    """Class Anggota Perpustakaan (Base class)"""
    
    def __init__(self, nama: str, id_anggota: str):
        self.nama = nama
        self.id_anggota = id_anggota
        self.__buku_dipinjam: List[Buku] = []
    
    def info(self) -> str:
        return f"{self.nama} (ID: {self.id_anggota})"
    
    def dapat_meminjam(self) -> bool:
        """Cek apakah anggota masih bisa meminjam"""
        return len(self.__buku_dipinjam) < self.batas_peminjaman()
    
    def batas_peminjaman(self) -> int:
        """Batas peminjaman default - akan di-override"""
        return 3
    
    def pinjam_buku(self, buku: Buku) -> bool:
        """Meminjam buku"""
        if not self.dapat_meminjam():
            print(f"{self.nama} sudah mencapai batas peminjaman ({self.batas_peminjaman()} buku)")
            return False
        
        if buku.pinjam():
            self.__buku_dipinjam.append(buku)
            print(f"{self.nama} berhasil meminjam {buku.judul}")
            return True
        else:
            print(f"Buku '{buku.judul}' sedang tidak tersedia")
            return False
    
    def kembalikan_buku(self, buku: Buku) -> bool:
        """Mengembalikan buku"""
        if buku in self.__buku_dipinjam:
            buku.kembalikan()
            self.__buku_dipinjam.remove(buku)
            print(f"{self.nama} mengembalikan {buku.judul}")
            return True
        else:
            print(f"{self.nama} tidak meminjam buku '{buku.judul}'")
            return False
    
    def daftar_pinjaman(self) -> None:
        """Menampilkan daftar buku yang dipinjam"""
        if not self.__buku_dipinjam:
            print(f"{self.nama} tidak sedang meminjam buku apapun")
        else:
            print(f"\n📚 Buku yang dipinjam oleh {self.nama}:")
            for i, buku in enumerate(self.__buku_dipinjam, 1):
                print(f"  {i}. {buku.info()}")
    
    def __str__(self) -> str:
        return self.info()


class Mahasiswa(Anggota):
    """Subclass Mahasiswa - memiliki batas peminjaman 5 buku"""
    
    def info(self) -> str:
        return f"Mahasiswa - {super().info()}"
    
    def batas_peminjaman(self) -> int:
        return 5  # Mahasiswa bisa pinjam 5 buku


class Dosen(Anggota):
    """Subclass Dosen - memiliki batas peminjaman 10 buku"""
    
    def info(self) -> str:
        return f"Dosen - {super().info()}"
    
    def batas_peminjaman(self) -> int:
        return 10  # Dosen bisa pinjam 10 buku


class Peminjaman:
    """Class Peminjaman - Mencatat transaksi peminjaman"""
    
    def __init__(self, anggota: Anggota, buku: Buku):
        self.__anggota = anggota
        self.__buku = buku
        self.__tanggal_pinjam = datetime.now()
        self.__tanggal_kembali = None
    
    def kembalikan(self) -> None:
        self.__tanggal_kembali = datetime.now()
    
    def info(self) -> str:
        status = "Selesai" if self.__tanggal_kembali else "Aktif"
        tgl_pinjam = self.__tanggal_pinjam.strftime('%d-%m-%Y %H:%M')
        tgl_kembali = self.__tanggal_kembali.strftime('%d-%m-%Y %H:%M') if self.__tanggal_kembali else "-"
        return f"{status} | {self.__anggota.nama} → {self.__buku.judul} | Pinjam: {tgl_pinjam} | Kembali: {tgl_kembali}"


class Perpustakaan:
    """Class Perpustakaan - Mengelola koleksi buku dan anggota"""
    
    def __init__(self, nama: str):
        self.nama = nama
        self.__daftar_buku: List[Buku] = []
        self.__daftar_anggota: List[Anggota] = []
        self.__daftar_peminjaman: List[Peminjaman] = []
    
    def tambah_buku(self, buku: Buku) -> None:
        self.__daftar_buku.append(buku)
        print(f"📖 Buku '{buku.judul}' ditambahkan ke perpustakaan")
    
    def daftar_anggota(self, anggota: Anggota) -> None:
        self.__daftar_anggota.append(anggota)
        print(f"👤 Anggota {anggota.nama} terdaftar")
    
    def cari_buku(self, keyword: str) -> List[Buku]:
        """Mencari buku berdasarkan judul atau penulis"""
        hasil = []
        keyword_lower = keyword.lower()
        for buku in self.__daftar_buku:
            if keyword_lower in buku.judul.lower() or keyword_lower in buku.penulis.lower():
                hasil.append(buku)
        return hasil
    
    def tampilkan_buku(self) -> None:
        """Menampilkan semua buku di perpustakaan"""
        print(f"\n📚 DAFTAR BUKU DI {self.nama.upper()}:")
        print("=" * 50)
        if not self.__daftar_buku:
            print("Belum ada buku")
        else:
            for i, buku in enumerate(self.__daftar_buku, 1):
                print(f"{i:2d}. {buku.info_lengkap()}")
        print("=" * 50)
    
    def pinjam_buku(self, anggota: Anggota, buku: Buku) -> bool:
        """Proses peminjaman buku"""
        if anggota.pinjam_buku(buku):
            peminjaman = Peminjaman(anggota, buku)
            self.__daftar_peminjaman.append(peminjaman)
            return True
        return False
    
    def kembalikan_buku(self, anggota: Anggota, buku: Buku) -> bool:
        """Proses pengembalian buku"""
        if anggota.kembalikan_buku(buku):
            # Update status peminjaman
            for p in self.__daftar_peminjaman:
                if p._Peminjaman__anggota == anggota and p._Peminjaman__buku == buku and not p._Peminjaman__tanggal_kembali:
                    p.kembalikan()
                    break
            return True
        return False
    
    def laporan_peminjaman(self) -> None:
        """Menampilkan laporan semua peminjaman"""
        print(f"\n📋 LAPORAN PEMINJAMAN {self.nama.upper()}:")
        print("=" * 60)
        if not self.__daftar_peminjaman:
            print("Belum ada transaksi peminjaman")
        else:
            for p in self.__daftar_peminjaman:
                print(p.info())
        print("=" * 60)


# PROGRAM UTAMA
def main():
    print("=" * 60)
    print("SISTEM PERPUSTAKAAN - DEMONSTRASI OOP")
    print("=" * 60)
    
    # Membuat perpustakaan
    perpus = Perpustakaan("Perpustakaan Universitas Teknologi")
    
    # Menambahkan buku
    print("\n--- TAMBAH BUKU ---")
    buku_list = [
        Buku("Python Dasar", "Guido van Rossum", 2020, 3),
        Buku("Machine Learning", "Andrew Ng", 2021, 2),
        Buku("Kecerdasan Buatan", "John McCarthy", 2019, 2),
        Buku("Dasar Pembuatan Website", "Vans Smith", 2022, 4),
        Buku("Algoritma dan Struktur Data", "Donald Knuth", 2018, 2),
    ]
    
    for buku in buku_list:
        perpus.tambah_buku(buku)
    
    # Mendaftarkan anggota
    print("\n--- DAFTAR ANGGOTA ---")
    mahasiswa1 = Mahasiswa("Budiyono", "43050240050")
    mahasiswa2 = Mahasiswa("Siti Aisyah", "43050240051")
    dosen1 = Dosen("Dr. Budi Santoso", "DS2024001")
    
    perpus.daftar_anggota(mahasiswa1)
    perpus.daftar_anggota(mahasiswa2)
    perpus.daftar_anggota(dosen1)
    
    # Menampilkan daftar buku
    perpus.tampilkan_buku()
    
    # Proses peminjaman
    print("\n--- PROSES PEMINJAMAN ---")
    
    # Cari buku
    buku_python = perpus.cari_buku("Python")[0]
    buku_ml = perpus.cari_buku("Machine")[0]
    buku_web = perpus.cari_buku("Website")[0]
    
    # Peminjaman oleh mahasiswa
    perpus.pinjam_buku(mahasiswa1, buku_python)
    perpus.pinjam_buku(mahasiswa1, buku_ml)
    perpus.pinjam_buku(mahasiswa2, buku_web)
    
    # Peminjaman oleh dosen (batas lebih besar)
    perpus.pinjam_buku(dosen1, buku_python)
    perpus.pinjam_buku(dosen1, buku_ml)
    perpus.pinjam_buku(dosen1, buku_web)
    
    # Coba pinjam buku yang sudah habis
    print("\n--- COBA PINJAM BUKU HABIS ---")
    perpus.pinjam_buku(mahasiswa2, buku_python)  # Stok Python habis
    
    # Melihat daftar pinjaman anggota
    print("\n--- DAFTAR PINJAMAN ANGGOTA ---")
    mahasiswa1.daftar_pinjaman()
    mahasiswa2.daftar_pinjaman()
    dosen1.daftar_pinjaman()
    
    # Proses pengembalian
    print("\n--- PROSES PENGEMBALIAN ---")
    perpus.kembalikan_buku(mahasiswa1, buku_python)
    perpus.kembalikan_buku(dosen1, buku_ml)
    
    # Laporan peminjaman
    perpus.laporan_peminjaman()
    
    # Tampilkan stok buku setelah peminjaman/pengembalian
    print("\n--- STOK BUKU SETELAH TRANSAKSI ---")
    perpus.tampilkan_buku()


if __name__ == "__main__":
    main()