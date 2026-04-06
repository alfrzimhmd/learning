from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

# Fungsi padding untuk teks yang panjangnya tidak kelipatan 16
def pad(text):
    pad_len = 16 - (len(text) % 16)
    return text + chr(pad_len) * pad_len

# Fungsi unpadding saat dekripsi
def unpad(text):
    pad_len = ord(text[-1])
    return text[:-pad_len]

# Fungsi enkripsi AES
def aes_encrypt(plain_text, key):
    key = key.encode('utf-8').ljust(16, b' ')[:16]  # key jadi 16 byte
    plain_text = pad(plain_text)
    iv = get_random_bytes(16)  # IV acak
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(plain_text.encode('utf-8'))
    result = base64.b64encode(iv + ciphertext).decode('utf-8')
    return result

# Fungsi dekripsi AES
def aes_decrypt(ciphertext_b64, key):
    key = key.encode('utf-8').ljust(16, b' ')[:16]
    data = base64.b64decode(ciphertext_b64)
    iv = data[:16]
    ciphertext = data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(ciphertext).decode('utf-8')
    return unpad(decrypted)

# PROGRAM UTAMA 
print("🔐 AES Enkripsi & Dekripsi")
mode = input("Pilih mode (enkripsi / dekripsi): ").strip().lower()

if mode == "enkripsi":
    plaintext = input("Masukkan teks yang ingin dienkripsi: ")
    key = input("Masukkan kunci rahasia (maks 16 karakter): ")
    encrypted = aes_encrypt(plaintext, key)
    print(f"\nHasil Enkripsi (Base64):\n{encrypted}")

elif mode == "dekripsi":
    ciphertext_b64 = input("Masukkan ciphertext (Base64): ")
    key = input("Masukkan kunci rahasia (sama dengan saat enkripsi): ")
    try:
        decrypted = aes_decrypt(ciphertext_b64, key)
        print(f"\nHasil Dekripsi:\n{decrypted}")
    except Exception as e:
        print("❌ Gagal mendekripsi. Pastikan ciphertext & kunci benar.")
else:
    print("❗ Mode tidak dikenali. Pilih 'enkripsi' atau 'dekripsi'.")
