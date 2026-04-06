# List untuk menyimpan pesanan
pesanan = []
pembeli = input("Masukkan Nama Anda : ")  
print("Nama Pembeli :", pembeli)

print("__________________________________________________")
print("_______ Selamat Datang di Afternoon Coffee _______")
print("__________________________________________________")


def daftar_kopi():
    # Menampilkan Daftar Menu Kopi
    print("  No  |     Nama KOPI      |    Harga   ")
    print("______|____________________|____________")
    print("  1.  |    Kopi Susu       |  Rp 7.000  ")
    print("  2.  |    Kopi Capucino   |  Rp 11.000 ")
    print("  3.  |    Kopi Hitam      |  Rp 9.000  ")
    print("  4.  |    Kopi Jahat      |  Rp 20.000 ")
    print("  5.  |    Kopi Ekspreso   |  Rp 23.000 ")
    print("  6.  |    KOPI Americano  |  Rp 27.000 ")
    print("  7.  |    Kopi Arabika    |  Rp 28.000 ")
    print("  8.  |    Kopi Robusta    |  Rp 26.000 ")
    print("________________________________________")

    while True:  # Looping tanpa henti sampai break terpenuhi
        try:       
            kode = int(input("Masukkan Kode Menu Kopi (1-8) : "))
            if 1 <= kode <= 8:
                break  #keluar dari while loop jika kode sudah benar
            else:
                print("Kode menu tidak valid. Masukkan angka antara 1 dan 8.")
        except ValueError:
            print("Input tidak valid. Masukkan angka.")

    while True:  # Loop untuk validasi input jumlah pesanan
        try:
            jumlahpesanan = int(input("Masukkan Jumlah Pesanan : "))
            if jumlahpesanan > 0:
                break
            else:
                print("Jumlah pesanan harus lebih dari 0.")
        except ValueError:   # Blok kode ini akan di jalankan jika terjadi valueError (jika memasukkan input berupa huruf/simbol (bukan angka))
            print("Input tidak valid. Masukkan angka.")

    # Mendefinisikan Harga dan Nama untuk setiap jenis kopi
    menu_coffie = {
        1: ("Kopi Susu", 7000),
        2: ("Kopi Capucino", 11000),
        3: ("Kopi Hitam", 9000),
        4: ("Kopi Jahat", 20000),
        5: ("Kopi Ekspreso", 23000),
        6: ("KOPI Americano", 27000),
        7: ("Kopi Arabika", 28000),
        8: ("Kopi Robusta", 26000)
    }

    nama_kopi, price = menu_coffie[kode]  # mengambil nama dan harga kopi berdasarkan kode
    total_harga = price * jumlahpesanan  # menghitung total harga berdasarkan harga kopi dan jumlah pesanan
    # menyimpan detail pesanan
    pesanan.append({
        "nama kopi": nama_kopi,  # menyimpan nama kopi
        "harga satuan": price,  # menyimpan harga satuan
        "jumlah": jumlahpesanan,  # menyimpan jumlah pesanan
        "harga": total_harga,  # menyimpan total harga
        "nama pembeli": pembeli
    })
    tanya()  # menanyakan apakah ingin memesan lagi
    return


def tanya():
    print("______________________________________________________")
    # menanyakan kepada pembeli apakah ingin memilih kopi yang lain
    tanya1 = input("Apakah Ingin Memilih Kopi yang lain??? yaa/tidak: ")
    print("______________________________________________________")

    # memeriksa jawaban pembeli
    if tanya1.lower() == "yaa":
        # jika pembeli menjawab "yaa" maka akan kembali ke tampilan daftar barang lagi
        daftar_kopi()
    elif tanya1.lower() == "tidak":
        # jika pembeli menjawab "tidak" maka akan lanjut ke proses akhir
        akhir()
    else:
        # jika jawaban tidak valid maka akan menanyakan kembali
        print("Maaf, jawaban Anda tidak valid!!!, silakan jawab dengan yaa/tidak!!!")
        tanya()


def akhir():
    # menghitung total harga dari semua pesanan
    total = sum(pesan["harga"] for pesan in pesanan)
    # menghitung jumlah total pesanan dari semua pesanan
    totalpesanan = sum(pesan["jumlah"] for pesan in pesanan)
    # menghitung PPN (Pajak Pertambahan Nilai) 20% dari total
    ppn = int(total * 0.2)
    diskon = 0  # inisialisasi diskon

    # menghitung diskon berdasarkan total
    if total >= 500000:
        diskon = total * 0.3  # Diskon 30 % jika total lebih dari 500.000
    elif total >= 300000:
        diskon = total * 0.2  # Diskon 20 % jika total lebih dari 300.000
    elif total >= 200000:
        diskon = total * 0.1  # Diskon 10 % jika total lebih dari 200.000
    elif total >= 100000:
        diskon = total * 0.0  # Diskon 0 % jika total lebih dari 100.000

    # Menghitung Total akhir setelah ditambahkan PPN dan dikurangi diskon
    total_akhir = total + ppn - diskon

    # Menampilkan ringkasan pesanan
    print("_______________________________________")
    print("___________ Afternoon Coffee __________")
    print("_______________________________________")
    print("Nama Pembeli         :", pembeli) 
    print("Detail Pesanan:")

    # menampilkan detail pesanan
    for pesan in pesanan:
        print(f"-{pesan['nama kopi']} Rp {pesan['harga satuan']} x {pesan['jumlah']} = Rp {pesan['harga']} ")

    # menampilkan total harga, PPN, Diskon, dan total akhir
    print("Total Harga          = Rp", total)
    print("Total Pesanan        =   ", totalpesanan)
    print("PPN                  = Rp", ppn)
    print("Potongan Harga       = Rp", diskon)
    print("Total Bayar          = Rp", total_akhir)
    # memulai loop untuk meminta input dari pembeli
    while True:
        try:
            # Meminta input dari pembeli untuk memasukkan jumlah uang yang dibayarkan
            bayar = int(input("Bayar                = Rp "))
            if bayar >= total_akhir:
                break  # Keluar dari loop jika input valid dan cukup
            else:
                print("Uang yang dibayarkan kurang!! Tidak Boleh Hutang!!!")
        except ValueError:
            # menangani kesalahan jika input tidak valid (bukan angka)
            print("Input tidak valid. Harap masukkan angka.")
    kembalian = bayar - total_akhir
    print("Kembalian            = Rp", kembalian)  # Menampilkan kembalian
    print("_______________________________________")
    print("_____________ Terima Kasih ____________")
    print("__Semoga Harimu Selalu Senin Terus :)__")


# memulai program dengan menampilkan daftar kopi
daftar_kopi()