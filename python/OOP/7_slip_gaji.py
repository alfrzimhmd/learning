"""
SISTEM SLIP GAJI PEGAWAI
Inheritance, Method Overriding, Polimorfisme
"""

from typing import List


class Pegawai:
    """Base class untuk semua pegawai"""
    
    def __init__(self, nama: str, nip: str):
        self.nama = nama
        self.nip = nip
        self._gaji_pokok = 4000000
    
    def jabatan(self) -> str:
        return "Pegawai Umum"
    
    def tunjangan(self) -> int:
        return 0
    
    def bonus_tahunan(self) -> int:
        """Bonus tahunan default"""
        return int(self._gaji_pokok * 0.5)
    
    def total_gaji(self) -> int:
        return self._gaji_pokok + self.tunjangan()
    
    def slip_gaji(self) -> str:
        return (
            f"\n╔{'═'*48}╗\n"
            f"║                    SLIP GAJI                    ║\n"
            f"╠{'═'*48}╣\n"
            f"║ Nama        : {self.nama:<36}║\n"
            f"║ NIP         : {self.nip:<36}║\n"
            f"║ Jabatan     : {self.jabatan():<36}║\n"
            f"╠{'═'*48}╣\n"
            f"║ Gaji Pokok  : Rp{self._gaji_pokok:>33,} ║\n"
            f"║ Tunjangan   : Rp{self.tunjangan():>33,} ║\n"
            f"╠{'═'*48}╣\n"
            f"║ Total Gaji  : Rp{self.total_gaji():>33,} ║\n"
            f"╚{'═'*48}╝"
        )
    
    def info_singkat(self) -> str:
        return f"{self.nip} | {self.nama} | {self.jabatan()} | Rp{self.total_gaji():,}"


class Manajer(Pegawai):
    """Class Manajer - inherits dari Pegawai"""
    
    def __init__(self, nama: str, nip: str, departemen: str = ""):
        super().__init__(nama, nip)
        self._gaji_pokok = 10000000
        self.departemen = departemen
        self.__anak_buah: List[Pegawai] = []  # Tim yang dikelola
    
    def jabatan(self) -> str:
        return "Manajer"
    
    def tunjangan(self) -> int:
        return int(self._gaji_pokok * 0.5)  # Tunjangan 50% dari gaji pokok
    
    def bonus_tahunan(self) -> int:
        """Manajer dapat bonus lebih besar"""
        return int(self._gaji_pokok * 1.0)  # Bonus 100%
    
    def tambah_anak_buah(self, pegawai: Pegawai) -> None:
        """Menambah anggota tim"""
        self.__anak_buah.append(pegawai)
    
    def info_tim(self) -> str:
        if not self.__anak_buah:
            return "Tidak memiliki tim"
        tim = ", ".join([p.nama for p in self.__anak_buah])
        return f"Mengelola: {tim}"


class Staf(Pegawai):
    """Class Staf - inherits dari Pegawai"""
    
    def __init__(self, nama: str, nip: str, divisi: str = ""):
        super().__init__(nama, nip)
        self._gaji_pokok = 5000000
        self.divisi = divisi
    
    def jabatan(self) -> str:
        return "Staf"
    
    def tunjangan(self) -> int:
        return int(self._gaji_pokok * 0.2)  # Tunjangan 20% dari gaji pokok


class Supervisor(Pegawai):
    """Class Supervisor - inherits dari Pegawai"""
    
    def __init__(self, nama: str, nip: str):
        super().__init__(nama, nip)
        self._gaji_pokok = 7000000
    
    def jabatan(self) -> str:
        return "Supervisor"
    
    def tunjangan(self) -> int:
        return int(self._gaji_pokok * 0.35)  # Tunjangan 35%


class Direktur(Pegawai):
    """Class Direktur - inherits dari Pegawai"""
    
    def __init__(self, nama: str, nip: str):
        super().__init__(nama, nip)
        self._gaji_pokok = 20000000
    
    def jabatan(self) -> str:
        return "Direktur"
    
    def tunjangan(self) -> int:
        return int(self._gaji_pokok * 0.75)  # Tunjangan 75%
    
    def bonus_tahunan(self) -> int:
        return int(self._gaji_pokok * 2.0)  # Bonus 200%


class Perusahaan:
    """Class Perusahaan - Mengelola semua pegawai"""
    
    def __init__(self, nama: str):
        self.nama = nama
        self.__daftar_pegawai: List[Pegawai] = []
    
    def rekrut(self, pegawai: Pegawai) -> None:
        """Menambahkan pegawai baru"""
        self.__daftar_pegawai.append(pegawai)
        print(f"{pegawai.jabatan()} {pegawai.nama} (NIP: {pegawai.nip}) bergabung")
    
    def pecat(self, nip: str) -> bool:
        """Menghapus pegawai"""
        for i, pegawai in enumerate(self.__daftar_pegawai):
            if pegawai.nip == nip:
                del self.__daftar_pegawai[i]
                print(f"Pegawai dengan NIP {nip} telah keluar")
                return True
        print(f"Pegawai dengan NIP {nip} tidak ditemukan")
        return False
    
    def daftar_semua_pegawai(self) -> None:
        """Menampilkan semua pegawai"""
        print(f"\n{'='*60}")
        print(f"DAFTAR PEGAWAI {self.nama.upper()}")
        print(f"{'='*60}")
        
        if not self.__daftar_pegawai:
            print("Belum ada pegawai")
            return
        
        # Kelompokkan berdasarkan jabatan
        jabatan_dict = {}
        for p in self.__daftar_pegawai:
            jabat = p.jabatan()
            if jabat not in jabatan_dict:
                jabatan_dict[jabat] = []
            jabatan_dict[jabat].append(p)
        
        for jabatan, pegawai_list in jabatan_dict.items():
            print(f"\n{jabatan.upper()} ({len(pegawai_list)} orang):")
            for p in pegawai_list:
                print(f"   {p.info_singkat()}")
    
    def cetak_semua_slip(self) -> None:
        """Mencetak slip gaji semua pegawai"""
        print(f"\n{'='*60}")
        print(f"SLIP GAJI PEGAWAI {self.nama.upper()}")
        print(f"{'='*60}")
        
        for pegawai in self.__daftar_pegawai:
            print(pegawai.slip_gaji())
    
    def total_beban_gaji(self) -> int:
        """Menghitung total gaji semua pegawai"""
        return sum(p.total_gaji() for p in self.__daftar_pegawai)
    
    def laporan_keuangan(self) -> None:
        """Menampilkan laporan keuangan perusahaan"""
        print(f"\n{'='*60}")
        print(f"LAPORAN KEUANGAN {self.nama.upper()}")
        print(f"{'='*60}")
        print(f"Jumlah Pegawai : {len(self.__daftar_pegawai)} orang")
        print(f"Total Gaji     : Rp{self.total_beban_gaji():,}")
        print(f"Rata-rata Gaji : Rp{self.total_beban_gaji() // len(self.__daftar_pegawai) if self.__daftar_pegawai else 0:,}")


# PROGRAM UTAMA
def main():
    print("=" * 60)
    print("SISTEM SLIP GAJI - DEMONSTRASI OOP")
    print("=" * 60)
    
    # Membuat perusahaan
    perusahaan = Perusahaan("PT Teknologi Maju")
    
    print("\n--- PROSES REKRUTMEN ---")
    
    # Input data pegawai
    pegawai_list = [
        ("Budi Santoso", "P001", "manajer", "IT"),
        ("Siti Aminah", "P002", "staf", "HRD"),
        ("Joko Widodo", "P003", "staf", "IT"),
        ("Dewi Sartika", "P004", "supervisor", ""),
        ("Ahmad Dahlan", "P005", "direktur", ""),
        ("Rina Amelia", "P006", "staf", "Marketing"),
        ("Hendra Wijaya", "P007", "manajer", "Marketing"),
    ]
    
    for nama, nip, jabatan, divisi in pegawai_list:
        if jabatan == "manajer":
            pegawai = Manajer(nama, nip, divisi)
        elif jabatan == "supervisor":
            pegawai = Supervisor(nama, nip)
        elif jabatan == "direktur":
            pegawai = Direktur(nama, nip)
        else:  # staf
            pegawai = Staf(nama, nip, divisi)
        
        perusahaan.rekrut(pegawai)
    
    # Tambahkan hubungan manajer - anak buah
    # Cari manajer dan staf untuk dihubungkan
    manajer_it = None
    manajer_marketing = None
    staf_it = []
    staf_marketing = []
    
    # Simulasi sederhana: kita tidak perlu implementasi penuh
    print("\n--- STRUKTUR ORGANISASI ---")
    print("Manajer IT: Budi Santoso")
    print("  - Staf IT: Joko Widodo")
    print("Manajer Marketing: Hendra Wijaya")
    print("  - Staf Marketing: Rina Amelia")
    print("Supervisor: Dewi Sartika")
    print("Direktur: Ahmad Dahlan")
    print("HRD: Siti Aminah")
    
    # Tampilkan semua pegawai
    perusahaan.daftar_semua_pegawai()
    
    # Cetak slip gaji
    perusahaan.cetak_semua_slip()
    
    # Laporan keuangan
    perusahaan.laporan_keuangan()
    
    # Demonstrasi polimorfisme
    print("\n" + "=" * 60)
    print("DEMONSTRASI POLIMORFISME")
    print("=" * 60)
    print("Method yang sama (total_gaji()) menghasilkan nilai berbeda:")
    print("- Manajer: Gaji pokok + tunjangan 50%")
    print("- Staf: Gaji pokok + tunjangan 20%")
    print("- Supervisor: Gaji pokok + tunjangan 35%")
    print("- Direktur: Gaji pokok + tunjangan 75%")


if __name__ == "__main__":
    main()