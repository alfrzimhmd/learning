"""
POLIMORFISME
Method yang sama memiliki perilaku berbeda di class berbeda
"""

class Hewan:
    """
    Class dasar (parent) untuk semua hewan
    """
    
    def __init__(self, nama: str, umur: int = 0):
        self.nama = nama
        self.umur = umur
    
    def bersuara(self) -> str:
        """Method dasar - akan di-override oleh subclass"""
        return "Hewan ini bersuara"
    
    def info(self) -> str:
        return f"{self.nama} (umur {self.umur} tahun)"


class Kucing(Hewan):
    """Subclass Kucing"""
    
    def bersuara(self) -> str:
        """Override method bersuara"""
        return "Meong! Meong!"
    
    def mengejar_tikus(self) -> str:
        """Method khusus kucing"""
        return f"{self.nama} sedang mengejar tikus!"


class Anjing(Hewan):
    """Subclass Anjing"""
    
    def bersuara(self) -> str:
        """Override method bersuara"""
        return "Guk! Guk! Guk!"
    
    def menggonggong(self) -> str:
        """Method khusus anjing"""
        return f"{self.nama} sedang menggonggong!"


class Sapi(Hewan):
    """Subclass Sapi"""
    
    def bersuara(self) -> str:
        """Override method bersuara"""
        return "Moooo!"
    
    def merumput(self) -> str:
        """Method khusus sapi"""
        return f"{self.nama} sedang merumput!"


class Bebek(Hewan):
    """Subclass Bebek"""
    
    def bersuara(self) -> str:
        """Override method bersuara"""
        return "Kwek! Kwek! Kwek!"


# Fungsi polimorfik - menerima objek apapun yang memiliki method bersuara()
def cetak_suara(hewan: Hewan) -> None:
    """Fungsi ini bekerja untuk semua jenis hewan (polimorfisme)"""
    print(f"{hewan.info()} bersuara: {hewan.bersuara()}")


# CONTOH PENGGUNAAN
def main():
    print("=" * 50)
    print("CONTOH POLIMORFISME - SUARA HEWAN")
    print("=" * 50)
    
    # Membuat objek dari berbagai class
    hewan_list = [
        Kucing("Tom", 3),
        Anjing("Spike", 4),
        Sapi("Moo", 5),
        Bebek("Donal", 2),
        Hewan("Hewan Unknown", 1)  # Class dasar
    ]
    
    # Memanggil method yang sama untuk objek berbeda
    print("\n--- METHOD Bersuara() ---")
    for hewan in hewan_list:
        print(f"{hewan.info()} → {hewan.bersuara()}")
    
    # Menggunakan fungsi polimorfik
    print("\n--- FUNGSI POLIMORFIK ---")
    for hewan in hewan_list:
        cetak_suara(hewan)
    
    # Method khusus per class
    print("\n--- METHOD KHUSUS PER CLASS ---")
    for hewan in hewan_list:
        if isinstance(hewan, Kucing):
            print(hewan.mengejar_tikus())
        elif isinstance(hewan, Anjing):
            print(hewan.menggonggong())
        elif isinstance(hewan, Sapi):
            print(hewan.merumput())
    
    # Demonstrasi polimorfisme dengan list
    print("\n--- DEMONSTRASI POLIMORFISME ---")
    print("Semua hewan memiliki method bersuara(), tapi hasilnya berbeda!")
    print("Ini yang disebut POLIMORFISME - satu interface, banyak implementasi")


if __name__ == "__main__":
    main()