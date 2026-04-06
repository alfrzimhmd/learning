"""
INHERITANCE (PEWARISAN)
Class child mewarisi atribut dan method dari class parent
"""


class Kendaraan:
    """
    Class dasar (parent) untuk semua kendaraan
    """
    
    def __init__(self, merk: str, tahun: int, warna: str = "Putih"):
        self.merk = merk
        self.tahun = tahun
        self.warna = warna
        self._kecepatan = 0  # Protected attribute
    
    def info(self) -> str:
        """Method dasar - bisa di-override"""
        return f"Kendaraan {self.merk} tahun {self.tahun}"
    
    def gas(self, increment: int) -> None:
        """Menambah kecepatan"""
        self._kecepatan += increment
        print(f"{self.merk} menambah kecepatan +{increment} km/jam")
    
    def rem(self, decrement: int) -> None:
        """Mengurangi kecepatan"""
        self._kecepatan = max(0, self._kecepatan - decrement)
        print(f"{self.merk} mengurangi kecepatan -{decrement} km/jam")
    
    def kecepatan_saat_ini(self) -> int:
        return self._kecepatan


class Mobil(Kendaraan):
    """Class Mobil mewarisi Kendaraan"""
    
    def __init__(self, merk: str, tipe: str, tahun: int, warna: str = "Putih"):
        # Memanggil constructor parent dengan super()
        super().__init__(merk, tahun, warna)
        self.tipe = tipe  # Atribut tambahan khusus Mobil
        self.jumlah_pintu = 4
    
    def info(self) -> str:
        """Override method info dari parent"""
        return f"Mobil {self.merk} tipe {self.tipe} tahun {self.tahun} warna {self.warna}"
    
    def buka_pintu(self) -> None:
        """Method khusus mobil"""
        print(f"Mobil {self.merk} membuka {self.jumlah_pintu} pintu")
    
    def nyalakan_wiper(self) -> None:
        """Method khusus mobil"""
        print(f"Mobil {self.merk} menyalakan wiper")


class Motor(Kendaraan):
    """Class Motor mewarisi Kendaraan"""
    
    def __init__(self, merk: str, tipe: str, tahun: int, warna: str = "Hitam"):
        super().__init__(merk, tahun, warna)
        self.tipe = tipe
        self.jumlah_roda = 2
    
    def info(self) -> str:
        """Override method info dari parent"""
        return f"Motor {self.merk} tipe {self.tipe} tahun {self.tahun} warna {self.warna}"
    
    def wheelie(self) -> None:
        """Method khusus motor"""
        print(f"Motor {self.merk} melakukan wheelie! ")
    
    def standar_ganda(self) -> None:
        """Method khusus motor"""
        print(f"Motor {self.merk} menurunkan standar ganda")


class Truk(Kendaraan):
    """Class Truk mewarisi Kendaraan"""
    
    def __init__(self, merk: str, kapasitas: int, tahun: int, warna: str = "Biru"):
        super().__init__(merk, tahun, warna)
        self.kapasitas = kapasitas  # dalam ton
        self.muatan_saat_ini = 0
    
    def info(self) -> str:
        return f"Truk {self.merk} kapasitas {self.kapasitas} ton tahun {self.tahun}"
    
    def muat_barang(self, berat: int) -> bool:
        """Method khusus truk"""
        if self.muatan_saat_ini + berat <= self.kapasitas:
            self.muatan_saat_ini += berat
            print(f"Truk {self.merk} memuat {berat} ton. Total muatan: {self.muatan_saat_ini} ton")
            return True
        else:
            print(f"Muatan {berat} ton melebihi kapasitas! Sisa: {self.kapasitas - self.muatan_saat_ini} ton")
            return False
    
    def info_muatan(self) -> None:
        print(f"Truk {self.merk} membawa {self.muatan_saat_ini}/{self.kapasitas} ton")


# CONTOH PENGGUNAAN
def main():
    print("=" * 50)
    print("CONTOH INHERITANCE - KENDARAAN")
    print("=" * 50)
    
    # Membuat objek dari berbagai class
    mobil = Mobil("Toyota", "SUV", 2022, "Merah")
    motor = Motor("Honda", "Sport", 2023, "Hitam")
    truk = Truk("Hino", 10, 2021, "Biru")
    
    kendaraan_list = [mobil, motor, truk]
    
    # Menampilkan info
    print("\n--- INFO KENDARAAN ---")
    for k in kendaraan_list:
        print(k.info())
    
    # Menggunakan method dari parent
    print("\n--- METHOD DARI PARENT ---")
    mobil.gas(30)
    print(f"Kecepatan mobil: {mobil.kecepatan_saat_ini()} km/jam")
    
    motor.gas(20)
    motor.rem(5)
    print(f"Kecepatan motor: {motor.kecepatan_saat_ini()} km/jam")
    
    # Menggunakan method khusus masing-masing class
    print("\n--- METHOD KHUSUS ---")
    mobil.buka_pintu()
    mobil.nyalakan_wiper()
    
    motor.wheelie()
    motor.standar_ganda()
    
    truk.muat_barang(5)
    truk.muat_barang(4)
    truk.muat_barang(3)  # Akan gagal
    truk.info_muatan()
    
    # Demonstrasi isinstance() dan issubclass()
    print("\n--- CEK JENIS CLASS ---")
    print(f"mobil adalah Mobil? {isinstance(mobil, Mobil)}")
    print(f"mobil adalah Kendaraan? {isinstance(mobil, Kendaraan)}")
    print(f"Motor adalah subclass Kendaraan? {issubclass(Motor, Kendaraan)}")
    print(f"Mobil adalah subclass Motor? {issubclass(Mobil, Motor)}")


if __name__ == "__main__":
    main()