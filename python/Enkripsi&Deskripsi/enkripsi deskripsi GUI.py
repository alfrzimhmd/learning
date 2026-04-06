# Import Library 
import base64
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import hashlib

# Fungsi Enkripsi/Dekripsi 
# Base64
def encrypt_base64(text):
    return base64.urlsafe_b64encode(text.encode()).decode()

def decrypt_base64(encoded_text):
    try:
        return base64.urlsafe_b64decode(encoded_text.encode()).decode()
    except Exception:
        return "❌ Format Base64 tidak valid atau rusak."

# Caesar
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Vigenère
def vigenere_encrypt(text, key):
    result = ""
    key = key.lower()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + shift) % 26 + offset)
            key_index += 1
        else:
            result += char
    return result

def vigenere_decrypt(text, key):
    result = ""
    key = key.lower()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset - shift) % 26 + offset)
            key_index += 1
        else:
            result += char
    return result

# AES
def get_aes_key(key_str):
    return hashlib.sha256(key_str.encode()).digest()

def aes_encrypt(text, key_str):
    key = get_aes_key(key_str)
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(text.encode(), AES.block_size))
    iv = cipher.iv
    result = base64.b64encode(iv + ct_bytes).decode('utf-8')
    return result

def aes_decrypt(enc_text, key_str):
    try:
        key = get_aes_key(key_str)
        raw = base64.b64decode(enc_text)
        iv = raw[:16]
        ct = raw[16:]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        return pt.decode('utf-8')
    except Exception:
        return "❌ Kunci salah atau teks terenkripsi rusak."


# Fungsi Proses
def proses():
    aksi = aksi_var.get()
    metode = metode_var.get()
    teks = teks_entry.get()
    kunci = kunci_entry.get()

    if not teks:
        messagebox.showwarning("Peringatan", "Masukkan teks terlebih dahulu.")
        return

    try:
        if metode == "Base64":
            hasil = encrypt_base64(teks) if aksi == "Enkripsi" else decrypt_base64(teks)

        elif metode == "Caesar":
            shift = int(kunci)
            hasil = caesar_encrypt(teks, shift) if aksi == "Enkripsi" else caesar_decrypt(teks, shift)

        elif metode == "Vigenère":
            if not kunci.isalpha():
                raise ValueError("Kunci harus berupa huruf.")
            hasil = vigenere_encrypt(teks, kunci) if aksi == "Enkripsi" else vigenere_decrypt(teks, kunci)

        elif metode == "AES":
            if not kunci:
                raise ValueError("Kunci AES tidak boleh kosong.")
            hasil = aes_encrypt(teks, kunci) if aksi == "Enkripsi" else aes_decrypt(teks, kunci)

        else:
            hasil = "❌ Metode tidak dikenali."

    except Exception as e:
        hasil = f"❌ Error: {str(e)}"

    hasil_entry.config(state="normal")
    hasil_entry.delete("1.0", tk.END)
    hasil_entry.insert(tk.END, hasil)
    hasil_entry.config(state="normal")

# Fungsi Reset 
def reset_form():
    teks_entry.delete(0, tk.END)
    kunci_entry.delete(0, tk.END)
    hasil_entry.config(state="normal")
    hasil_entry.delete("1.0", tk.END)

def toggle_kunci(*args):
    metode = metode_var.get()
    if metode in ["Caesar", "Vigenère", "AES"]:
        kunci_label.grid()
        kunci_entry.grid()
    else:
        kunci_label.grid_remove()
        kunci_entry.grid_remove()

# GUI Setup 

app = ttk.Window(title="Enkripsi & Dekripsi", themename="darkly", size=(720, 520))
app.resizable(False, False)

ttk.Label(app, text="PROGRAM ENKRIPSI & DEKRIPSI", font=("Segoe UI", 18, "bold")).pack(pady=20)
main_frame = ttk.Frame(app, padding=10)
main_frame.pack(fill=BOTH, expand=True)

# Pilihan Aksi
ttk.Label(main_frame, text="Pilih Aksi:").grid(row=0, column=0, sticky=W, padx=5, pady=5)
aksi_var = ttk.StringVar(value="Enkripsi")
aksi_combo = ttk.Combobox(main_frame, textvariable=aksi_var, values=["Enkripsi", "Dekripsi"], width=30)
aksi_combo.grid(row=0, column=1, sticky=W, padx=5, pady=5)

# Pilihan Metode
ttk.Label(main_frame, text="Pilih Metode:").grid(row=1, column=0, sticky=W, padx=5, pady=5)
metode_var = ttk.StringVar(value="Base64")
metode_combo = ttk.Combobox(main_frame, textvariable=metode_var, width=30, values=["Base64", "Caesar", "Vigenère", "AES"])
metode_combo.grid(row=1, column=1, sticky=W, padx=5, pady=5)
metode_var.trace_add("write", toggle_kunci)

# Input Teks
ttk.Label(main_frame, text="Teks:").grid(row=2, column=0, sticky=W, padx=5, pady=5)
teks_entry = ttk.Entry(main_frame, width=50)
teks_entry.grid(row=2, column=1, padx=5, pady=5)

# Kunci / Shift
kunci_label = ttk.Label(main_frame, text="Kunci / Shift:")
kunci_label.grid(row=3, column=0, sticky=W, padx=5, pady=5)
kunci_entry = ttk.Entry(main_frame, width=50)
kunci_entry.grid(row=3, column=1, padx=5, pady=5)

# Tombol
btn_frame = ttk.Frame(main_frame)
btn_frame.grid(row=4, column=1, sticky=E, pady=10)
reset_btn = ttk.Button(btn_frame, text="🔄 Reset", bootstyle=SECONDARY, command=reset_form)
proses_btn = ttk.Button(btn_frame, text="🔐 Proses", bootstyle=PRIMARY, command=proses)
reset_btn.pack(side=LEFT, padx=5)
proses_btn.pack(side=LEFT)

# Hasil
ttk.Label(main_frame, text="Hasil:").grid(row=5, column=0, sticky=NW, padx=5, pady=5)
hasil_entry = tk.Text(main_frame, width=50, height=5, wrap="word")
hasil_entry.grid(row=5, column=1, padx=5, pady=5)
hasil_entry.config(state="normal")

# Inisialisasi tampilan kunci
toggle_kunci()

# Jalankan aplikasi
app.mainloop()
