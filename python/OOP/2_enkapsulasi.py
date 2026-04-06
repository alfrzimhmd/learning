"""
ENKAPSULASI (DATA HIDING)
Menyembunyikan data internal class menggunakan private attribute (__)
"""


class BankAccount:
    """
    Class BankAccount dengan enkapsulasi
    
    Private attribute (__saldo) tidak bisa diakses langsung dari luar class
    Hanya bisa diakses melalui method public
    """
    
    def __init__(self, nama: str, saldo_awal: float = 0):
        """
        Constructor BankAccount
        
        Args:
            nama: Nama pemilik rekening
            saldo_awal: Saldo awal (default 0)
        """
        self.nama = nama  # Public attribute - bisa diakses langsung
        self.__saldo = saldo_awal  # Private attribute - TIDAK bisa diakses langsung
        self.__transaksi = []  # Private attribute untuk riwayat transaksi
        self._no_rekening = self.__generate_no_rekening()  # Protected attribute
    
    def __generate_no_rekening(self) -> str:
        """Private method - hanya bisa dipanggil dari dalam class"""
        import random
        return f"BR{random.randint(100000, 999999)}"
    
    def lihat_saldo(self) -> None:
        """Public method - melihat saldo (read-only)"""
        print(f"Saldo {self.nama} (No. Rek: {self._no_rekening}): Rp {self.__saldo:,.0f}")
    
    def setor(self, jumlah: float) -> bool:
        """Public method - menambah saldo"""
        if jumlah <= 0:
            print("Jumlah setor harus lebih dari 0!")
            return False
        
        self.__saldo += jumlah
        self.__transaksi.append(f"SETOR: +Rp{jumlah:,.0f}")
        print(f"Berhasil menyetor Rp {jumlah:,.0f}")
        return True
    
    def tarik_tunai(self, jumlah: float) -> bool:
        """Public method - mengurangi saldo dengan validasi"""
        if jumlah <= 0:
            print("Jumlah tarik harus lebih dari 0!")
            return False
        
        if jumlah <= self.__saldo:
            self.__saldo -= jumlah
            self.__transaksi.append(f"TARIK: -Rp{jumlah:,.0f}")
            print(f"Berhasil menarik Rp {jumlah:,.0f}")
            return True
        else:
            print(f"Saldo tidak mencukupi! Saldo Anda: Rp {self.__saldo:,.0f}")
            return False
    
    def lihat_transaksi(self) -> None:
        """Public method - melihat riwayat transaksi"""
        print(f"\n--- RIWAYAT TRANSAKSI {self.nama} ---")
        if not self.__transaksi:
            print("Belum ada transaksi")
        else:
            for t in self.__transaksi:
                print(t)
    
    # GETTER untuk saldo (read-only)
    @property
    def saldo(self) -> float:
        """Property getter - mengakses saldo seperti atribut biasa"""
        return self.__saldo
    
    # SETTER untuk saldo (dengan validasi)
    @saldo.setter
    def saldo(self, value: float) -> None:
        """Property setter - tidak bisa langsung mengubah saldo"""
        raise AttributeError("Tidak bisa langsung mengubah saldo! Gunakan method setor() atau tarik_tunai()")


# CONTOH PENGGUNAAN
def main():
    print("=" * 50)
    print("CONTOH ENKAPSULASI - BANK ACCOUNT")
    print("=" * 50)
    
    # Membuat objek
    akun1 = BankAccount("Andi", 500000)
    akun2 = BankAccount("Budi", 1000000)
    
    # Menampilkan saldo awal
    print("\n--- SALDO AWAL ---")
    akun1.lihat_saldo()
    akun2.lihat_saldo()
    
    # Melakukan transaksi
    print("\n--- TRANSAKSI ---")
    akun1.setor(100000)
    akun1.tarik_tunai(200000)
    akun1.tarik_tunai(500000)  # Coba tarik lebih dari saldo
    
    akun2.tarik_tunai(1500000)  # Saldo tidak cukup
    akun2.setor(500000)
    akun2.tarik_tunai(750000)
    
    # Menampilkan saldo akhir
    print("\n--- SALDO AKHIR ---")
    akun1.lihat_saldo()
    akun2.lihat_saldo()
    
    # Menampilkan riwayat transaksi
    akun1.lihat_transaksi()
    akun2.lihat_transaksi()
    
    # Demonstrasi enkapsulasi
    print("\n--- DEMONSTRASI ENKAPSULASI ---")
    print("Public attribute (nama):", akun1.nama)
    
    # Ini akan ERROR karena private attribute
    try:
        print("Private attribute (__saldo):", akun1.__saldo)
    except AttributeError as e:
        print(f"Error: {e}")
    
    # Tapi bisa diakses melalui property
    print(f"Property saldo: Rp {akun1.saldo:,.0f}")
    
    # Ini juga ERROR karena setter diblok
    try:
        akun1.saldo = 999999
    except AttributeError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()