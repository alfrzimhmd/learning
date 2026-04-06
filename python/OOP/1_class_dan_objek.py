"""
CLASS DAN OBJEK DASAR
Membuat class dan menginstansiasi objek
"""


class Mahasiswa:
    """
    Class Mahasiswa - Blueprint untuk data mahasiswa
    
    Attributes:
        nama (str): Nama lengkap mahasiswa
        nim (str): Nomor Induk Mahasiswa
        prodi (str): Program studi mahasiswa
    """
    
    def __init__(self, nama: str, nim: str, prodi: str):
        """
        Constructor - Dipanggil saat objek dibuat
        
        Args:
            nama: Nama mahasiswa
            nim: NIM mahasiswa
            prodi: Program studi mahasiswa
        """
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
    
    def perkenalan(self) -> None:
        """Method untuk memperkenalkan diri"""
        print(f"Halo, Perkenalkan Nama Saya {self.nama}")
        print(f"Dengan NIM {self.nim}")
        print(f"Program Studi {self.prodi}")
        print("-" * 40)
    
    def belajar(self, mata_kuliah: str) -> None:
        """Method untuk aktivitas belajar"""
        print(f"{self.nama} sedang belajar {mata_kuliah}")
    
    def __str__(self) -> str:
        """String representation untuk print(objek)"""
        return f"{self.nama} ({self.nim}) - {self.prodi}"


# CONTOH PENGGUNAAN
def main():
    print("=" * 50)
    print("CONTOH CLASS DAN OBJEK")
    print("=" * 50)
    
    # Membuat objek (instansiasi)
    mhs1 = Mahasiswa("Budiyono", "43050240050", "Teknologi Informasi")
    mhs2 = Mahasiswa("Siti Aisyah", "43050240051", "Sistem Informasi")
    mhs3 = Mahasiswa("Budi Santoso", "43050240052", "Informatika")
    
    # Memanggil method
    print("\n--- PERKENALAN ---")
    mhs1.perkenalan()
    mhs2.perkenalan()
    mhs3.perkenalan()
    
    # Memanggil method lain
    print("\n--- AKTIVITAS ---")
    mhs1.belajar("Pemrograman Python")
    mhs2.belajar("Basis Data")
    mhs3.belajar("Jaringan Komputer")
    
    # Mengakses atribut langsung
    print("\n--- AKSES ATRIBUT ---")
    print(f"mhs1.nama = {mhs1.nama}")
    print(f"mhs2.nim = {mhs2.nim}")
    print(f"mhs3.prodi = {mhs3.prodi}")
    
    # Menggunakan __str__ method
    print("\n--- STRING REPRESENTATION ---")
    print(mhs1)
    print(mhs2)
    print(mhs3)


if __name__ == "__main__":
    main()