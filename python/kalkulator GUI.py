import tkinter as tk  # Mengimpor modul tkinter untuk GUI dasar
import ttkbootstrap as ttk  # Mengimpor ttkbootstrap untuk tampilan dan widget yang lebih modern

# Fungsi untuk menangani aksi tombol

def button_click(number):
    """Menambahkan angka atau operator ke input entry."""

    current = entry.get()  # Mendapatkan teks yang sudah ada di entry
    entry.delete(0, tk.END)  # Menghapus semua teks di entry
    entry.insert(0, str(current) + str(number))  # Menambahkan angka/operator baru ke awal entry


def button_clear():
    """Menghapus semua input di entry (fungsi untuk tombol 'AC')."""
    entry.delete(0, tk.END)  # Menghapus semua teks di entry


def button_equal():
    """
    Mengevaluasi ekspresi matematika di entry dan menampilkan hasilnya.
    Menangani potensi error seperti pembagian dengan nol, kesalahan sintaks, dll.
    """
    try:
        expression = entry.get()
        # Mengganti simbol 'x' dengan '*' dan '%' dengan '//' untuk kompatibilitas dengan eval()
        expression = expression.replace('x', '*').replace('%', '//')  
        result = eval(expression) # Menggunakan eval() - hati-hati dengan keamanan!  Lihat catatan di bawah.
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except (SyntaxError, NameError, ZeroDivisionError, TypeError) as e:  # Menangani berbagai jenis error
        entry.delete(0, tk.END)
        entry.insert(0, f"Error: {e}") # Menampilkan pesan error yang lebih informatif


# Membuat jendela kalkulator 

root = ttk.Window(themename="darkly")  # Membuat jendela utama dengan tema "darkly" dari ttkbootstrap
root.title("Kalkulator Sederhana")  # Mengatur judul jendela

# Entry untuk menampilkan input dan hasil perhitungan
entry = ttk.Entry(root, width=30)  # Membuat field input
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)  # Menempatkan entry di grid layout


# Menambahkan tombol-tombol 

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', 'x',
    '1', '2', '3', '-',
    '0', '.', '%', '+',
    '=', 'AC'
]

row = 1
col = 0
for button_text in buttons:
    # Menentukan command berdasarkan teks tombol
    if button_text == '=':
        command = button_equal
    elif button_text == 'AC':
        command = button_clear
    else:
        command = lambda text=button_text: button_click(text) # Menggunakan lambda untuk membuat fungsi anonim

    button = ttk.Button(root, text=button_text, width=5, command=command) # Membuat tombol
    button.grid(row=row, column=col, padx=5, pady=5)  # Menempatkan tombol di grid layout
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()  # Memulai loop utama untuk menjalankan GUI


# Catatan Penting: Penggunaan `eval()`
# Fungsi `eval()` dapat menjadi rentan terhadap serangan keamanan jika input berasal dari sumber yang tidak tepercaya.
# Untuk aplikasi yang lebih aman, pertimbangkan untuk menggunakan parser ekspresi matematika yang lebih robust
# daripada `eval()`.