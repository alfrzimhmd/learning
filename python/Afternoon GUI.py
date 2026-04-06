import tkinter as tk
import tkinter.messagebox as messagebox
import ttkbootstrap as ttk

# Konstanta
PPN_RATE = 0.2
DISKON_LEVELS = {
    500000: 0.3,
    300000: 0.2,
    200000: 0.1,
}

# Data menu kopi
menu_kopi = {
    1: ("Kopi Susu", 7000),
    2: ("Kopi Capucino", 11000),
    3: ("Kopi Hitam", 9000),
    4: ("Kopi Jahat", 20000),
    5: ("Kopi Ekspreso", 23000),
    6: ("KOPI Americano", 27000),
    7: ("Kopi Arabika", 28000),
    8: ("Kopi Robusta", 26000),
}

pesanan = []

def tambah_pesanan():
    try:
        selected_option = combo_menu.get().strip()
        if not selected_option:
            show_message("Pilih menu kopi terlebih dahulu.")
            return

        kode = int(selected_option.split(".", 1)[0]) # Pisahkan kode dan nama kopi
        jumlah_str = entry_jumlah.get().strip()
        if not jumlah_str.isdigit():
            raise ValueError("Jumlah pesanan harus berupa angka.")
        jumlah = int(jumlah_str)

        if 1 <= kode <= len(menu_kopi) and jumlah > 0:
            nama_kopi, harga = menu_kopi[kode]
            total_harga = harga * jumlah
            pesanan.append({
                "nama_kopi": nama_kopi,
                "harga_satuan": harga,
                "jumlah": jumlah,
                "total_harga": total_harga,
            })
            update_pesanan()
            entry_jumlah.delete(0, tk.END)
        else:
            show_message("Kode menu atau jumlah pesanan tidak valid.")
    except (ValueError, IndexError) as e:
        show_message(str(e)) # Menampilkan pesan kesalahan yang lebih informatif


def hitung_total_dan_diskon(total):
    ppn = int(total * PPN_RATE)
    diskon = 0
    for threshold, rate in DISKON_LEVELS.items():
        if total >= threshold:
            diskon = total * rate
    return ppn, diskon


def update_pesanan():
    text_pesanan.delete("1.0", tk.END)
    total = sum(p["total_harga"] for p in pesanan)
    for p in pesanan:
        text_pesanan.insert(tk.END, f"- {p['nama_kopi']} x {p['jumlah']} = Rp {p['total_harga']}\n")
    text_pesanan.insert(tk.END, f"\nTotal: Rp {total}")


def selesaikan_pesanan():
    if not pesanan:
        show_message("Belum ada pesanan.")
        return

    total = sum(p["total_harga"] for p in pesanan)
    ppn, diskon = hitung_total_dan_diskon(total)
    total_akhir = total + ppn - diskon

    ringkasan = f"""
Nama Pembeli: {entry_nama.get()}
Detail Pesanan:
{text_pesanan.get("1.0", tk.END)}
Total: Rp {total}
PPN: Rp {ppn}
Diskon: Rp {diskon}
Total Bayar: Rp {total_akhir}
"""

    def bayar():
        nonlocal total_akhir # Menambahkan nonlocal untuk bisa mengubah variabel di luar scope
        try:
            bayar = int(entry_bayar.get())
            if bayar >= total_akhir:
                kembalian = bayar - total_akhir
                show_message(f"Kembalian: Rp {kembalian}\nTerima kasih!\nSemoga Harimu Senin Terus :)")
                root.destroy()
            else:
                show_message("Uang yang dibayarkan kurang!!, Tidak boleh hutang!!")
        except ValueError:
            show_message("Input tidak valid.")

    dialog = ttk.Toplevel(root)
    dialog.title("Ringkasan Pesanan")
    label_ringkasan = ttk.Label(dialog, text=ringkasan, justify="left")
    label_ringkasan.pack(pady=10)
    ttk.Label(dialog, text="Bayar:").pack()
    entry_bayar = ttk.Entry(dialog)
    entry_bayar.pack()
    ttk.Button(dialog, text="Bayar", command=bayar).pack(pady=10)

def show_message(message):
    messagebox.showinfo("Pesan", message)

# Membuat jendela utama
root = ttk.Window(themename="darkly")
root.title("Afternoon Coffee")

# Input nama pembeli
ttk.Label(root, text="Nama Pembeli:").grid(row=0, column=0, sticky=tk.W)
entry_nama = ttk.Entry(root)
entry_nama.grid(row=0, column=1, padx=5, pady=5)

# Menu kopi 
ttk.Label(root, text="Menu Kopi:").grid(row=1, column=0, sticky=tk.W)
menu_options = [f"{kode}. {nama} (Rp {harga})" for kode, (nama, harga) in menu_kopi.items()]
combo_menu = ttk.Combobox(root, values=menu_options)
combo_menu.grid(row=1, column=1, padx=5, pady=5)

# Jumlah pesanan
ttk.Label(root, text="Jumlah:").grid(row=2, column=0, sticky=tk.W)
entry_jumlah = ttk.Entry(root)
entry_jumlah.grid(row=2, column=1, padx=5, pady=5)

# Tombol Tambah Pesanan
ttk.Button(root, text="Tambah Pesanan", command=tambah_pesanan).grid(row=3, column=1, pady=10)

# Daftar pesanan
ttk.Label(root, text="Daftar Pesanan:").grid(row=4, column=0, sticky=tk.W, columnspan=2)
text_pesanan = tk.Text(root, height=10, width=30)
text_pesanan.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Tombol Selesaikan Pesanan
ttk.Button(root, text="Selesaikan Pesanan", command=selesaikan_pesanan).grid(row=6, column=1, pady=10)

root.mainloop()