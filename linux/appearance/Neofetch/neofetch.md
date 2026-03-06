# 📚 PANDUAN LENGKAP INSTALASI DAN KONFIGURASI NEOFETCH
> Mempercantik Tampilan Terminal 
## 📋 DAFTAR ISI
- [🖥️ APA ITU NEOFETCH?](#-apa-itu-neofetch)
- [📦 CARA INSTAL NEOFETCH](#-cara-instal-neofetch)
- [⚙️ KONFIGURASI DASAR](#️-konfigurasi-dasar)
- [📋 PENJELASAN LENGKAP INFO YANG DITAMPILKAN](#-penjelasan-lengkap-info-yang-ditampilkan)
- [🎨 KUSTOMISASI TAMPILAN](#-kustomisasi-tampilan)
- [🖼️ ASCII ART & LOGO](#️-ascii-art--logo)
- [🌈 PANDUAN WARNA LENGKAP](#-panduan-warna-lengkap)
- [📝 INTEGRASI DENGAN .BASHRC](#-integrasi-dengan-bashrc)
- [🔧 SCRIPT KUSTOM NEOFETCH](#-script-kustom-neofetch)
- [🔄 BACKUP DAN RESTORE KONFIGURASI](#-backup-dan-restore-konfigurasi)
- [🛡️ TROUBLESHOOTING](#️-troubleshooting)
- [🎯 CONTOH KONFIGURASI LENGKAP](#-contoh-konfigurasi-lengkap)
- [⚡ REFERENSI CEPAT](#-referensi-cepat-perintah-singkat)
- [📝 CATATAN PENTING](#-catatan-penting)
---
## 🖥️ APA ITU NEOFETCH?
Neofetch adalah alat baris perintah yang menampilkan informasi sistem Anda bersama dengan logo distribusi Linux secara aesthetic. Informasi yang ditampilkan meliputi:
- OS (Ubuntu, versi)
- Host (model laptop/PC)
- Kernel (versi Linux)
- Uptime (berapa lama menyala)
- Packages (jumlah paket terinstall)
- Shell (bash/zsh/fish)
- Resolution (resolusi layar)
- DE (Desktop Environment seperti GNOME)
- WM (Window Manager)
- Theme (tema yang digunakan)
- Icons (ikon yang digunakan)
- Terminal (gnome-terminal, dll)
- CPU (prosesor)
- GPU (kartu grafis)
- Memory (RAM digunakan/total)
---
## 📦 CARA INSTAL NEOFETCH
### Metode 1: Install dari Repository Ubuntu (Mudah)
```bash
sudo apt update
sudo apt install neofetch
```
### Metode 2: Install dari GitHub (Versi Terbaru)
```bash
# Install dependensi
sudo apt install git make w3m img2txt

# Clone repository
git clone https://github.com/dylanaraps/neofetch.git
cd neofetch

# Install
sudo make install
```
### Metode 3: Install via Snap
```bash
sudo snap install neofetch
```
**Verifikasi Instalasi**
```bash
# Cek versi
neofetch --version

# Jalankan pertama kali
neofetch
```
## ⚙️ KONFIGURASI DASAR
### 1. Lokasi File Konfigurasi
```bash
# Buat folder konfigurasi jika belum ada
mkdir -p ~/.config/neofetch

# Salin konfigurasi default
cp /etc/neofetch/config.conf ~/.config/neofetch/config.conf
# atau jika dari GitHub
cp ~/neofetch/config.conf ~/.config/neofetch/config.conf
```
### 2. Edit Konfigurasi
```bash
nano ~/.config/neofetch/config.conf
```
### 3. Struktur Dasar Config
```bash
print_info() {
    # Informasi Dasar Sistem
    info title                    # Menampilkan "user@hostname" (contoh: all@Ubuntu)
    info underline                # Garis pembatas di bawah title
    
    # Informasi Sistem Operasi
    info "OS" distro               # Nama dan versi OS (Ubuntu 22.04 LTS)
    info "Host" model              # Model laptop/PC (Lenovo ThinkPad X1, dll)
    info "Kernel" kernel            # Versi kernel Linux (6.17.0-14-generic)
    info "Uptime" uptime            # Lama sistem menyala (2 hours, 30 mins)
    info "Packages" packages        # Jumlah paket terinstall (via apt, snap, flatpak)
    info "Shell" shell              # Shell yang digunakan (bash, zsh, fish)
    
    # Informasi Tampilan
    info "Resolution" resolution     # Resolusi layar (1920x1080, 1536x864)
    info "DE" de                     # Desktop Environment (GNOME, KDE, XFCE)
    info "WM" wm                     # Window Manager (mutter, i3, awesome)
    info "WM Theme" wm_theme         # Tema Window Manager (Adwaita, dll)
    info "Theme" theme               # Tema GTK/desktop (Yaru, Adwaita-dark)
    info "Icons" icons               # Tema ikon (Yaru, Papirus, Tela)
    
    # Informasi Terminal
    info "Terminal" term             # Terminal emulator (gnome-terminal, konsole)
    info "Terminal Font" term_font   # Font yang digunakan di terminal (Monospace 11)
    
    # Informasi Hardware
    info "CPU" cpu                   # Prosesor (Intel i7-1165G7, 8 cores)
    info "GPU" gpu                    # Kartu grafis (Intel Iris Xe, NVIDIA RTX 3060)
    info "Memory" memory              # Penggunaan RAM (2.4GB / 15.6GB)
    info "Disk" disk                  # Penggunaan disk (/dev/nvme0n1p5: 45G/234G)
    info "Battery" battery            # Status baterai (94% [charging])
    
    # Informasi Tambahan
    info "Song" song                  # Lagu yang sedang diputar (jika ada)
    info "Local IP" local_ip          # Alamat IP lokal (192.168.1.10)
    info "Public IP" public_ip        # Alamat IP publik (jika terhubung internet)
    info "Users" users                # Jumlah user yang login
    info "Birthday" birthday          # Tanggal install sistem (jika dikonfigurasi)
}
```
---
## 🎨 KUSTOMISASI TAMPILAN
### 1. Mengatur Info yang Ditampilkan
**Buka file konfigurasi** `nano ~/.config/neofetch/config.conf:`
```bash
# Tampilan minimal (hanya info penting)
print_info() {
    info title                    # user@hostname
    info underline                # garis pembatas
    info "OS" distro               # OS
    info "Kernel" kernel           # kernel
    info "Uptime" uptime           # waktu menyala
    info "Packages" packages       # jumlah paket
    info "Shell" shell             # shell
    info "Memory" memory           # RAM
}
```
### 2. Mengatur Lebar Tampilan
```bash
# Jarak antara logo dan info (default: 3)
gap=4

# Lebar total tampilan (default: auto)
width=80  # Lebar dalam karakter
```
### 3. Mengatur Format Waktu
```bash
# Format uptime
uptime_shorthand="on"   # on = "2h 30m", off = "2 hours 30 minutes"
uptime_short="off"       # Tampilan lebih singkat

# Format tanggal
birthday_format="%Y-%m-%d %H:%M"  # Format: 2024-01-15 14:30
```
---
## 🖼️ ASCII ART & LOGO
### 1. Memilih Logo Distribusi
```bash
# Di file config.conf
distro="Ubuntu"           # Akan menampilkan logo Ubuntu
# atau
distro="auto"             # Mendeteksi otomatis

# Daftar logo yang tersedia:
# Ubuntu, Debian, Fedora, Arch, Manjaro, Mint, Kali, Pop!_OS, dll
```
### 2. Mengatur Ukuran Logo
```bash
# Ukuran logo (small, medium, large)
image_size="medium"

# Cara menampilkan logo
image_backend="ascii"     # ascii, w3m, iterm2, kitty, sixel
ascii_distro="auto"       # auto, Ubuntu, dll
```
### 3. Custom ASCII Art
```bash
# Buat file ascii art sendiri
nano ~/.config/neofetch/custom_logo

# Contoh isi file:
#           .-.
#          (   )
#           |-|
#          /   \
#         /     \
#        /       \
#       /         \

# Di config.conf
ascii_distro="custom"
ascii_file="~/.config/neofetch/custom_logo"
```
---
## 🌈 PANDUAN WARNA LENGKAP
| Angka | Warna | Kode Hex | Contoh Penggunaan |
|-------|-------|----------|-------------------|
| **0** | Hitam | `#000000` | Background, teks gelap, shadow |
| **1** | Merah | `#FF0000` | Error, peringatan, memory usage |
| **2** | Hijau | `#00FF00` | Sukses, packages, informasi positif |
| **3** | Kuning/Oranye | `#FFFF00` | CPU usage, warning, shell |
| **4** | Biru | `#0000FF` | OS info, judul, link |
| **5** | Ungu/Magenta | `#FF00FF` | Hostname, aksen, GPU info |
| **6** | Cyan | `#00FFFF` | Kernel, info teknis, uptime |
| **7** | Putih | `#FFFFFF` | Teks utama, default |
| **8** | Abu-abu | `#808080` | Teks secondary, keterangan |
| **9** | Hitam Terang | `#555555` | Background terang, shadow terang |

### Cara Mengatur Warna
``` bash
# Warna untuk ASCII art (3 angka)
ascii_colors=(4 6 7)  # Biru, Cyan, Putih

# Warna teks info (array untuk setiap baris)
colors=(4 6 7 8 9 10 11 12)  # Warna bergantian

# Warna judul
title_color="4"        # Biru untuk judul

# Warna underline
underline_color="4"    # Biru untuk garis bawah

# Warna spesifik untuk info tertentu
color_os="4"           # OS pakai biru
color_host="5"         # Host pakai ungu
color_kernel="6"       # Kernel pakai cyan
color_uptime="7"       # Uptime pakai putih
color_packages="2"     # Packages pakai hijau
color_shell="3"        # Shell pakai kuning
color_memory="1"       # Memory pakai merah
```
### Test Warna di Terminal
```bash
# Test semua warna dasar
for i in {0..7}; do
    echo -e "\033[1;3${i}mWarna $i - Contoh Teks\033[0m"
done

# Test dengan background
for i in {40..47}; do
    echo -e "\033[${i}mBackground $((i-40))\033[0m"
done
```
### Kombinasi Warna Populer
```bash
# Kombinasi 1: Biru - Cyan - Putih (elegan)
ascii_colors=(4 6 7)

# Kombinasi 2: Merah - Hijau - Kuning (ceria)
ascii_colors=(1 2 3)

# Kombinasi 3: Ungu - Cyan - Putih (modern)
ascii_colors=(5 6 7)

# Kombinasi 4: Monokrom (abu-abu)
ascii_colors=(8 7 8)

# Kombinasi 5: Warna Ubuntu (merah-oranye-putih)
ascii_colors=(1 3 7)
```
---
## 📝 INTEGRASI DENGAN .BASHRC
### 1. Jalankan Neofetch Otomatis Saat Buka Terminal
```bash
# Edit .bashrc
nano ~/.bashrc

# Tambahkan di akhir file
echo ""
neofetch
echo ""
```
### 2. Jalankan dengan Konfigurasi Tertentu
```bash
# Di .bashrc
echo ""
neofetch --ascii_colors 4 6 7 --gap 4 --bold on
echo ""
```
### 3. Tampilkan Hanya Sekali Per Hari
```bash
# Di .bashrc
LAST_RUN_FILE="/tmp/neofetch_last_run"
TODAY=$(date +%Y%m%d)

if [ ! -f "$LAST_RUN_FILE" ] || [ "$(cat $LAST_RUN_FILE)" != "$TODAY" ]; then
    echo ""
    neofetch --ascii_colors 4 6 7
    echo ""
    echo "$TODAY" > "$LAST_RUN_FILE"
fi
```
### 4. Simpan Dan Restart
```bash
# Simpan
Ctrl + O, Enter, Ctrl + X

# Restart bashrc
source ~/.bashrc
```
---
## 🔧 SCRIPT KUSTOM NEOFETCH
### Script dengan Pilihan Tampilan
**Buat file:** ` ~/neofetch-custom.sh`
```bash
#!/bin/bash

# Pilihan tampilan berdasarkan argumen
case $1 in
    "minimal")
        # Hanya info dasar
        neofetch --disable model packages shell de wm theme icons term cpu gpu disk
        ;;
    "lengkap")
        # Semua info
        neofetch --enable all
        ;;
    "game")
        # Tema gaming (hijau)
        neofetch --ascii_colors 2 3 1 --gap 2 --bold on
        ;;
    "elegan")
        # Tema elegan (biru-cyan)
        neofetch --ascii_colors 4 6 7 --gap 4 --bold on
        ;;
    "ubuntu")
        # Tema Ubuntu (merah-oranye)
        neofetch --ascii_colors 1 3 7 --gap 4
        ;;
    "dark")
        # Tema dark (abu-putih)
        neofetch --ascii_colors 8 7 8 --gap 4
        ;;
    *)
        # Default
        neofetch
        ;;
esac
```
### Beri izin execute:
```bash
chmod +x ~/neofetch-custom.sh
```
### Gunakan:
```bash
~/neofetch-custom.sh elegan
~/neofetch-custom.sh minimal
~/neofetch-custom.sh ubuntu
```
---
## 🔄 BACKUP DAN RESTORE KONFIGURASI
### Backup Konfigurasi
```bash
# Backup file config
cp ~/.config/neofetch/config.conf ~/.config/neofetch/config.conf.backup.$(date +%Y%m%d)

# Backup semua (termasuk script custom)
tar -czf ~/neofetch-backup-$(date +%Y%m%d).tar.gz ~/.config/neofetch/ ~/neofetch-custom.sh 2>/dev/null
```
### Restore Konfigurasi
```bash
# Restore file config
cp ~/.config/neofetch/config.conf.backup.[TANGGAL] ~/.config/neofetch/config.conf

# Restore dari tar
tar -xzf ~/neofetch-backup-[TANGGAL].tar.gz -C ~/
```
---
## 🛡️ TROUBLESHOOTING
### Masalah dan Solusi

| Masalah | Penyebab | Solusi |
|---------|----------|--------|
| Neofetch tidak menampilkan info tertentu | Info tidak tersedia atau disabled | `neofetch --enable all` atau `neofetch --help \| grep -A 5 "INFO"` |
| Logo tidak muncul | Backend salah atau logo tidak ada | `neofetch --backend ascii` atau `neofetch --ascii_distro list` |
| Logo rusak/tidak rapi | Terminal tidak support atau font salah | Ganti font terminal ke monospace, set `ascii_bold="off"` |
| Warna tidak sesuai | Konfigurasi warna salah | `neofetch --ascii_colors 4 6 7` untuk test |
| Neofetch lambat | Info disk/public_ip memperlambat | `neofetch --disable disk public_ip` |
| Neofetch error setelah update | Versi baru tidak kompatibel | `sudo apt update && sudo apt upgrade neofetch` |
| Info battery tidak muncul | Laptop tidak terdeteksi | Cek dengan `upower -e` |
| Info GPU tidak muncul | Driver tidak terdeteksi | Install `lshw` atau `pciutils` |
| Terminal freeze | Image backend bermasalah | Ganti ke `image_backend="ascii"` |

### Perintah Debugging

| Perintah | Fungsi |
|----------|--------|
| `neofetch --version` | Cek versi neofetch |
| `neofetch --help` | Lihat semua opsi |
| `neofetch --help config` | Lihat opsi konfigurasi |
| `neofetch --help colors` | Lihat panduan warna |
| `neofetch --test --colors` | Test semua warna |
| `neofetch --ascii_distro list` | Lihat daftar logo tersedia |
| `neofetch --backend off` | Nonaktifkan logo (info saja) |
| `neofetch --disable all --enable title os memory` | Tampilkan hanya info tertentu |

---
## 🎯 CONTOH KONFIGURASI LENGKAP
### Berikut contoh konfigurasi lengkap dengan penjelasan:
```bash
# ~/.config/neofetch/config.conf

# ============================================
# INFORMASI YANG DITAMPILKAN
# ============================================
print_info() {
    info title                    # user@hostname
    info underline                # garis pembatas
    
    # Informasi Sistem
    info "OS" distro               # Ubuntu 22.04 LTS
    info "Host" model              # Lenovo ThinkPad X1
    info "Kernel" kernel           # 6.17.0-14-generic
    info "Uptime" uptime           # 2h 30m
    info "Packages" packages       # 2345 (apt, snap)
    info "Shell" shell             # bash 5.1.16
    
    # Informasi Tampilan
    info "Resolution" resolution   # 1536x864
    info "DE" de                   # GNOME
    info "Theme" theme             # Yaru-dark
    info "Icons" icons             # Yaru
    
    # Informasi Hardware
    info "CPU" cpu                 # Intel i7-1165G7 (8)
    info "GPU" gpu                 # Intel Iris Xe
    info "Memory" memory           # 2.4GiB / 15.6GiB
}

# ============================================
# PENGATURAN TAMPILAN
# ============================================
gap=4                             # Jarak antara logo dan info
bold="on"                          # Teks tebal

# ============================================
# PENGATURAN WARNA
# ============================================
# Warna ASCII art (biru, cyan, putih)
ascii_colors=(4 6 7)

# Warna judul dan underline
title_color="4"                    # Biru
underline_color="4"                # Biru
underline_char="-"                 # Karakter underline

# Warna spesifik per info
color_os="4"                       # OS: Biru
color_host="5"                      # Host: Ungu
color_kernel="6"                    # Kernel: Cyan
color_uptime="7"                    # Uptime: Putih
color_packages="2"                  # Packages: Hijau
color_memory="1"                    # Memory: Merah

# ============================================
# PENGATURAN LOGO
# ============================================
ascii_distro="Ubuntu"               # Logo Ubuntu
ascii_bold="on"                     # Logo tebal
image_backend="ascii"               # Tampilkan sebagai ASCII

# ============================================
# FORMAT TAMPILAN
# ============================================
uptime_shorthand="on"               # 2h 30m (bukan 2 hours 30 minutes)
memory_percent="on"                  # Tampilkan persentase RAM
cpu_display="off"                    # Nonaktifkan tampilan CPU detail
```
---
## ⚡ REFERENSI CEPAT (PERINTAH SINGKAT)
### Perintah Dasar

| Perintah | Keterangan |
|----------|------------|
| `sudo apt install neofetch` | Install neofetch |
| `neofetch` | Jalankan dengan konfigurasi default |
| `neofetch --ascii_colors 4 6 7` | Jalankan dengan warna biru-cyan-putih |
| `neofetch --disable gpu disk` | Nonaktifkan info GPU dan disk |
| `nano ~/.config/neofetch/config.conf` | Edit file konfigurasi |
| `mkdir -p ~/.config/neofetch` | Buat folder konfigurasi |
| `cp /etc/neofetch/config.conf ~/.config/neofetch/` | Salin config default |

### Opsi Warna Cepat

| Perintah | Hasil Warna |
|----------|-------------|
| `neofetch --ascii_colors 4 6 7` | Biru, Cyan, Putih |
| `neofetch --ascii_colors 1 2 3` | Merah, Hijau, Kuning |
| `neofetch --ascii_colors 5 6 4` | Ungu, Cyan, Biru |
| `neofetch --ascii_colors 8 7 8` | Abu, Putih, Abu |

### Integrasi .bashrc

| Tambahkan di `.bashrc` | Efek |
|------------------------|------|
| `neofetch` | Tampil setiap buka terminal |
| `neofetch --ascii_colors 4 6 7` | Tampil dengan warna khusus |
| `sleep 1; neofetch` | Tampil dengan jeda 1 detik |
| `clear; neofetch` | Bersihkan layar dulu, baru tampil |

### Backup/Restore

| Perintah | Fungsi |
|----------|--------|
| `cp ~/.config/neofetch/config.conf ~/.config/neofetch/config.conf.backup` | Backup config |
| `cp ~/.config/neofetch/config.conf.backup ~/.config/neofetch/config.conf` | Restore config |
| `tar -czf neofetch-backup.tar.gz ~/.config/neofetch/` | Backup semua folder config |
| `tar -xzf neofetch-backup.tar.gz -C ~/` | Restore semua folder config |

---
📝 CATATAN PENTING
1. File konfigurasi berada di ~/.config/neofetch/config.conf
2. Kode warna 0-7 untuk dasar, 8-9 untuk variasi terang/gelap
3. Backup config sebelum melakukan perubahan besar
4. Neofetch hanya untuk tampilan, tidak mempengaruhi kinerja sistem
5. Beberapa info mungkin tidak muncul jika hardware tidak mendukung
6. Warna tergantung terminal yang digunakan (GNOME Terminal, Konsole, dll)

## Selamat menikmati terminal Ubuntu yang lebih cantik dengan Neofetch! ✨  
### *Panduan ini disusun berdasarkan pengalaman instalasi dan konfigurasi Neofetch pada Ubuntu dengan GNOME terminal.*
