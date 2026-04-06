"""
SISTEM RESERVASI HOTEL
Polymorphism, Inheritance, Encapsulation
"""

from datetime import datetime, timedelta
from typing import List, Optional


class Tamu:
    """Class Tamu - Representasi tamu hotel"""
    
    def __init__(self, nama: str, identitas: str, no_telp: str = ""):
        self.nama = nama
        self.identitas = identitas
        self.no_telp = no_telp
    
    def info(self) -> str:
        return f"{self.nama} (ID: {self.identitas})"
    
    def info_lengkap(self) -> str:
        telp = f" - Telp: {self.no_telp}" if self.no_telp else ""
        return self.info() + telp


class Kamar:
    """Base class untuk semua tipe kamar"""
    
    def __init__(self, nomor: int, lantai: int = 1):
        self.nomor = nomor
        self.lantai = lantai
        self._tersedia = True
    
    def harga_per_malam(self) -> int:
        """Method yang akan di-override oleh subclass"""
        return 0
    
    def tipe(self) -> str:
        return "Kamar Biasa"
    
    def fasilitas(self) -> List[str]:
        return ["Kasur", "AC", "TV", "Kamar Mandi Dalam"]
    
    def info(self) -> str:
        fasilitas_str = ", ".join(self.fasilitas()[:3]) + "..."
        status = "✓ Tersedia" if self._tersedia else "✗ Terisi"
        return f"{self.tipe()} - No.{self.nomor} (Lt.{self.lantai}) - Rp{self.harga_per_malam():,}/malam - {status}\n   Fasilitas: {fasilitas_str}"
    
    @property
    def tersedia(self) -> bool:
        return self._tersedia
    
    def pesan(self) -> bool:
        if self._tersedia:
            self._tersedia = False
            return True
        return False
    
    def kosongkan(self) -> None:
        self._tersedia = True


class StandardRoom(Kamar):
    """Kamar Standar - harga 300.000/malam"""
    
    def harga_per_malam(self) -> int:
        return 300000
    
    def tipe(self) -> str:
        return "Standar"
    
    def fasilitas(self) -> List[str]:
        return ["Kasur Queen", "AC", "TV 32 inch", "Kamar Mandi Dalam", "Shower"]


class DeluxeRoom(Kamar):
    """Kamar Deluxe - harga 500.000/malam"""
    
    def harga_per_malam(self) -> int:
        return 500000
    
    def tipe(self) -> str:
        return "Deluxe"
    
    def fasilitas(self) -> List[str]:
        return ["Kasur King", "AC", "TV 50 inch", "Kamar Mandi Dalam", "Bathtub", "Mini Bar", "Balkon"]


class SuiteRoom(Kamar):
    """Kamar Suite - harga 1.000.000/malam"""
    
    def harga_per_malam(self) -> int:
        return 1000000
    
    def tipe(self) -> str:
        return "Suite"
    
    def fasilitas(self) -> List[str]:
        return [
            "Kasur King Size (2)", "AC", "TV 65 inch", "Kamar Mandi Dalam (2)",
            "Jacuzzi", "Mini Bar", "Balkon", "Ruang Tamu", "Dapur Kecil"
        ]


class Reservasi:
    """Class Reservasi - Mencatat transaksi pemesanan kamar"""
    
    def __init__(self, tamu: Tamu, kamar: Kamar, check_in: datetime, check_out: datetime):
        self.__tamu = tamu
        self.__kamar = kamar
        self.__check_in = check_in
        self.__check_out = check_out
        self.__id_reservasi = self.__generate_id()
    
    def __generate_id(self) -> str:
        import random
        return f"RSV{random.randint(10000, 99999)}"
    
    def durasi_menginap(self) -> int:
        return (self.__check_out - self.__check_in).days
    
    def total_biaya(self) -> int:
        return self.__kamar.harga_per_malam() * self.durasi_menginap()
    
    @property
    def id_reservasi(self) -> str:
        return self.__id_reservasi
    
    def info(self) -> str:
        return (
            f"\n🏨 RESERVASI #{self.id_reservasi}\n"
            f"{'='*40}\n"
            f"Tamu      : {self.__tamu.info_lengkap()}\n"
            f"Kamar     : {self.__kamar.info()}\n"
            f"Check-in  : {self.__check_in.strftime('%d-%m-%Y')} (15:00 WIB)\n"
            f"Check-out : {self.__check_out.strftime('%d-%m-%Y')} (12:00 WIB)\n"
            f"Durasi    : {self.durasi_menginap()} malam\n"
            f"{'-'*40}\n"
            f"Total     : Rp{self.total_biaya():,}\n"
            f"{'='*40}"
        )
    
    def invoice(self) -> str:
        """Membuat invoice detail"""
        invoice_str = f"""
╔══════════════════════════════════════════════════════════════╗
║                    INVOICE HOTEL                             ║
╠══════════════════════════════════════════════════════════════╣
║ ID Reservasi : {self.id_reservasi}
║ Tamu         : {self.__tamu.nama}
║ Identitas    : {self.__tamu.identitas}
╠══════════════════════════════════════════════════════════════╣
║ Detail Kamar : {self.__kamar.tipe()} Room No.{self.__kamar.nomor}
║ Harga/malam  : Rp{self.__kamar.harga_per_malam():,}
║ Durasi       : {self.durasi_menginap()} malam
╠══════════════════════════════════════════════════════════════╣
║ SUBTOTAL     : Rp{self.__kamar.harga_per_malam() * self.durasi_menginap():,}
║ Pajak (10%)  : Rp{int(self.total_biaya() * 0.1):,}
║ Service (5%) : Rp{int(self.total_biaya() * 0.05):,}
╠══════════════════════════════════════════════════════════════╣
║ TOTAL        : Rp{int(self.total_biaya() * 1.15):,}
╚══════════════════════════════════════════════════════════════╝
"""
        return invoice_str


class Hotel:
    """Class Hotel - Mengelola kamar dan reservasi"""
    
    def __init__(self, nama: str, alamat: str):
        self.nama = nama
        self.alamat = alamat
        self.__daftar_kamar: List[Kamar] = []
        self.__daftar_reservasi: List[Reservasi] = []
    
    def tambah_kamar(self, kamar: Kamar) -> None:
        self.__daftar_kamar.append(kamar)
        print(f"Kamar {kamar.tipe()} No.{kamar.nomor} ditambahkan")
    
    def kamar_tersedia(self) -> List[Kamar]:
        return [k for k in self.__daftar_kamar if k.tersedia]
    
    def tampilkan_kamar(self) -> None:
        """Menampilkan semua kamar"""
        print(f"\n🏨 DAFTAR KAMAR {self.nama.upper()}")
        print("=" * 60)
        
        tersedia = self.kamar_tersedia()
        terisi = [k for k in self.__daftar_kamar if not k.tersedia]
        
        print(f"\n✓ Kamar Tersedia ({len(tersedia)}):")
        for kamar in tersedia:
            print(f"  {kamar.info()}")
        
        print(f"\n✗ Kamar Terisi ({len(terisi)}):")
        for kamar in terisi:
            print(f"  {kamar.tipe()} - No.{kamar.nomor} (Lt.{kamar.lantai})")
    
    def cari_kamar_tersedia(self, tipe: str = None) -> List[Kamar]:
        """Mencari kamar tersedia berdasarkan tipe"""
        tersedia = self.kamar_tersedia()
        if tipe:
            tipe_lower = tipe.lower()
            return [k for k in tersedia if k.tipe().lower() == tipe_lower]
        return tersedia
    
    def buat_reservasi(self, tamu: Tamu, nomor_kamar: int, check_in: datetime, check_out: datetime) -> Optional[Reservasi]:
        """Membuat reservasi baru"""
        # Cari kamar
        kamar = None
        for k in self.__daftar_kamar:
            if k.nomor == nomor_kamar and k.tersedia:
                kamar = k
                break
        
        if not kamar:
            print(f"Kamar nomor {nomor_kamar} tidak tersedia")
            return None
        
        if check_in >= check_out:
            print("Tanggal check-out harus setelah check-in")
            return None
        
        # Pesan kamar
        if kamar.pesan():
            reservasi = Reservasi(tamu, kamar, check_in, check_out)
            self.__daftar_reservasi.append(reservasi)
            print(f"\nReservasi berhasil dibuat!")
            return reservasi
        
        print(f"Gagal membuat reservasi")
        return None
    
    def cek_reservasi(self, id_reservasi: str) -> Optional[Reservasi]:
        """Mencari reservasi berdasarkan ID"""
        for reservasi in self.__daftar_reservasi:
            if reservasi.id_reservasi == id_reservasi:
                return reservasi
        return None


# PROGRAM UTAMA
def main():
    print("=" * 60)
    print("SISTEM RESERVASI HOTEL - DEMONSTRASI OOP")
    print("=" * 60)
    
    # Membuat hotel
    hotel = Hotel("Hotel Mewah Indah", "Jl. Raya No. 123, Jakarta")
    
    # Menambahkan kamar
    print("\n--- MENAMBAHKAN KAMAR ---")
    hotel.tambah_kamar(StandardRoom(101, 1))
    hotel.tambah_kamar(StandardRoom(102, 1))
    hotel.tambah_kamar(StandardRoom(103, 1))
    hotel.tambah_kamar(DeluxeRoom(201, 2))
    hotel.tambah_kamar(DeluxeRoom(202, 2))
    hotel.tambah_kamar(SuiteRoom(301, 3))
    
    # Tampilkan daftar kamar
    hotel.tampilkan_kamar()
    
    # Input data tamu
    print("\n--- INPUT DATA TAMU ---")
    nama = input("Masukkan nama tamu: ")
    identitas = input("Masukkan nomor identitas (KTP/Paspor): ")
    no_telp = input("Masukkan nomor telepon: ")
    
    tamu = Tamu(nama, identitas, no_telp)
    
    # Input tanggal
    print("\n--- INPUT TANGGAL MENGINAP ---")
    print("Format: DD-MM-YYYY")
    
    while True:
        try:
            tgl_in_str = input("Tanggal check-in (DD-MM-YYYY): ")
            tgl_out_str = input("Tanggal check-out (DD-MM-YYYY): ")
            
            check_in = datetime.strptime(tgl_in_str, '%d-%m-%Y')
            check_out = datetime.strptime(tgl_out_str, '%d-%m-%Y')
            
            if check_out > check_in:
                break
            else:
                print("Tanggal check-out harus setelah check-in!")
        except ValueError:
            print("Format tanggal salah! Gunakan DD-MM-YYYY")
    
    # Pilih kamar
    print("\n--- PILIH KAMAR ---")
    tersedia = hotel.cari_kamar_tersedia()
    for kamar in tersedia:
        print(f"  {kamar.info()}")
    
    while True:
        try:
            nomor = int(input("\nMasukkan nomor kamar yang dipilih: "))
            reservasi = hotel.buat_reservasi(tamu, nomor, check_in, check_out)
            if reservasi:
                print("\n" + reservasi.invoice())
                break
        except ValueError:
            print("Masukkan nomor kamar yang valid!")
    
    # Tampilkan kamar setelah reservasi
    print("\n--- KAMAR SETELAH RESERVASI ---")
    hotel.tampilkan_kamar()


if __name__ == "__main__":
    main()