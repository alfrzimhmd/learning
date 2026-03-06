# 📚 PANDUAN LENGKAP INSTALASI TEMA GRUB
> Elegant GRUB2 Themes - Mojave Window Right Dark
  
### *Panduan ini mencakup instalasi, perubahan, dan penghapusan tema GRUB pada sistem Ubuntu dual boot dengan Windows.*

## 📋 DAFTAR ISI
- [🖥️ PENGECEKAN AWAL](#-pengcekan-awal)
- [📦 PERSIAPAN FILE TEMA](#-persiapan-file-tema)
- [🚀 CARA INSTALL TEMA](#-cara-install-tema)
- [🔄 CARA GANTI TEMA](#-cara-ganti-tema)
- [🗑️ CARA HAPUS TEMA](#-cara-hapus-tema)
- [⏪ KEMBALI KE TEMA DEFAULT](#-kembali-ke-tema-default-grub-ubuntu)
- [🛡️ TROUBLESHOOTING](#-troubleshooting)
- [🎨 DAFTAR KOMBINASI TEMA](#-daftar-kombinasi-tema)
- [⚡ REFERENSI CEPAT](#-referensi-cepat-perintah-singkat)
- [📝 CATATAN PENTING](#-catatan-penting)
---
## 🖥️ PENGECEKAN AWAL
### 1. Cek resolusi layar
```bash
xrandr | grep "*"
# atau
xdpyinfo | grep dimensions
```
Contoh output: `1536x864 59.94*+`  
Catatan: Untuk resolusi 16:9 (seperti `1536x864`), gunakan opsi `-s 1080p`

### 2. Cek sistem dual boot  
```bash
lsblk | grep -i windows
# atau
efibootmgr
```
---
## 📦 PERSIAPAN FILE TEMA
### 1. Download tema dari GitHub
```bash
# Download ZIP
wget https://github.com/vinceliuice/Elegant-grub2-themes.zip
```
Atau 
```
https://github.com/Jacksaur/Gorgeous-GRUB/tree/main?tab=readme-ov-file
```
Setelah selesai download, lalu ekstrak:
`unzip Elegant-grup2-themes.zip -d ~/`

### 2. Masuk ke folder tema
```bash
cd ~/Elegant-grub2-themes-main
```
### 3. Lihat isi folder
```bash
ls -la
```
Akan terlihat file-file:
```bash
install.sh - Script installer
preview-01.jpg sampai preview-04.jpg - Preview tema
Folder assets/, backgrounds/, dll
```
### 4. Beri izin execute pada script
```bash
chmod +x install.sh
```
### 5. Lihat opsi yang tersedia
```bash
./install.sh -h
```
Output:
```
OPTIONS:
  -t, --theme     Background theme variant(s) [forest|mojave|mountain|wave]
  -p, --type      Theme style variant(s)      [window|float|sharp|blur]
  -i, --side      Picture display side        [left|right]
  -c, --color     Background color variant(s) [dark|light]
  -s, --screen    Screen display variant(s)   [1080p|2k|4k]
  -l, --logo      Show a logo on picture      [default|system]
  -r, --remove    Remove/Uninstall theme
  -b, --boot      Install theme into '/boot/grub' or '/boot/grub2'
  -h, --help      Show this help
```
---
## 🚀 CARA INSTALL TEMA
### 1. Backup konfigurasi GRUB (antisipasi error)
```bash
sudo cp /etc/default/grub /etc/default/grub.backup.$(date +%Y%m%d)
sudo cp /boot/grub/grub.cfg /boot/grub/grub.cfg.backup.$(date +%Y%m%d)
echo "✅ Backup created"
```
### 2. Install tema (pilih salah satu)
#### Opsi 1: MOJAVE (yang digunakan saat ini)
```bash
sudo ./install.sh -t mojave -p window -i right -c dark -s 1080p
```
#### Opsi 2: FOREST (default)
```bash
sudo ./install.sh
```
#### Opsi 3: MOUNTAIN
```bash
sudo ./install.sh -t mountain -p float -i left -c dark -s 1080p
```
#### Opsi 4: WAVE
```bash
sudo ./install.sh -t wave -p blur -i right -c dark -s 1080p
```
### 3. Verifikasi instalasi
```bash
# Cek apakah tema terinstall
ls -la /usr/share/grub/themes/

# Cek konfigurasi GRUB
cat /etc/default/grub | grep -E "GRUB_THEME|GRUB_GFXMODE"
```
Contoh output sukses:
```text
GRUB_GFXMODE=1920x1080,auto
GRUB_THEME="/usr/share/grub/themes/Elegant-mojave-window-right-dark/theme.txt"
```
### 4. Reboot sistem
```bash
sudo reboot
```
---
## 🔄 CARA GANTI TEMA
### 1. Masuk ke folder tema
```bash
cd ~/Elegant-grub2-themes-main
```
### 2. Lihat preview tema (untuk memilih)
```bash
# Buka file preview
xdg-open preview-01.jpg
xdg-open preview-02.jpg
xdg-open preview-03.jpg
xdg-open preview-04.jpg
```
### 3. Install tema baru (pilih kombinasi)
```bash
# Contoh: Ganti ke MOUNTAIN dengan style float
sudo ./install.sh -t mountain -p float -i left -c dark -s 1080p

# Contoh: Ganti ke FOREST dengan style sharp
sudo ./install.sh -t forest -p sharp -i right -c dark -s 1080p

# Contoh: Ganti ke WAVE dengan logo system
sudo ./install.sh -t wave -p blur -i left -c dark -s 1080p -l system
```
#### Catatan: Script akan otomatis menjalankan update-grub
### 4. Reboot
```bash
sudo reboot
```
---
## 🗑️ CARA HAPUS TEMA
### 1. Cari tahu tema yang sedang aktif
```bash
cat /etc/default/grub | grep GRUB_THEME
```
**Contoh output:** `GRUB_THEME="/usr/share/grub/themes/Elegant-mojave-window-right-dark/theme.txt"`
### 2. Uninstall tema spesifik
```bash
cd ~/Elegant-grub2-themes-main

# Format: sudo ./install.sh -r -t [tema] -p [style] -i [side] -c [color] -s [resolusi]

# Contoh hapus tema mojave-window-right-dark
sudo ./install.sh -r -t mojave -p window -i right -c dark -s 1080p

# Contoh hapus tema forest default
sudo ./install.sh -r -t forest -p window -i left -c dark -s 1080p
```
### 3. Update GRUB
```bash
sudo update-grub
```
### 4. Reboot
```bash
sudo reboot
```
---
## ⏪ KEMBALI KE TEMA DEFAULT GRUB UBUNTU
### Metode 1: Menggunakan backup
```bash
# Lihat file backup
ls -la /etc/default/grub.backup*

# Kembalikan backup terbaru
sudo cp /etc/default/grub.backup.[TANGGAL] /etc/default/grub

# Update GRUB
sudo update-grub

# Reboot
sudo reboot
```
### Metode 2: Hapus baris tema dari konfigurasi
```bash
# Edit file GRUB
sudo nano /etc/default/grub

# Hapus atau comment baris: GRUB_THEME=...
# Simpan dengan Ctrl+X, Y, Enter

# Update GRUB
sudo update-grub

# Reboot
sudo reboot
```
### Metode 3: Install ulang GRUB (jika bermasalah)
```bash
sudo apt update
sudo apt install --reinstall grub-efi grub2-common
sudo update-grub
```
---
## 🛡️ TROUBLESHOOTING
### 1. GRUB error/tidak muncul setelah install tema
#### Solusi: Boot dari Live USB dan perbaiki:
```bash
# Cari partisi root Ubuntu
lsblk -f

# Mount partisi root (misal /dev/nvme0n1p5)
sudo mount /dev/nvme0n1p5 /mnt

# Mount partisi EFI (jika ada)
sudo mount /dev/nvme0n1p1 /mnt/boot/efi

# Chroot ke sistem
sudo chroot /mnt

# Kembalikan backup GRUB
cp /etc/default/grub.backup.[TANGGAL] /etc/default/grub

# Update GRUB
update-grub

# Exit dan reboot
exit
sudo umount -R /mnt
sudo reboot
```
### 2. Tema tidak muncul setelah reboot
```bash
# Cek apakah tema masih terinstall
ls -la /usr/share/grub/themes/

# Cek konfigurasi GRUB
cat /etc/default/grub | grep GRUB_THEME

# Install ulang tema
cd ~/Elegant-grub2-themes-main
sudo ./install.sh -t mojave -p window -i right -c dark -s 1080p
```
### 3. Resolusi tidak sesuai
```bash
# Edit file /etc/default/grub:
sudo nano /etc/default/grub

# Ubah atau tambahkan:
GRUB_GFXMODE=1536x864,1920x1080,auto
GRUB_GFXPAYLOAD_LINUX=keep

# Simpan, lalu:
sudo update-grub
sudo reboot
```
### 4. Windows tidak muncul di menu GRUB
```bash
# Aktifkan os-prober
sudo nano /etc/default/grub

# Hapus tanda # di depan: GRUB_DISABLE_OS_PROBER=false

# Update GRUB
sudo update-grub
```
---
## 🎨 DAFTAR KOMBINASI TEMA

### 1. TEMA FOREST 🌲
| Style | Perintah |
|-------|----------|
| Forest + Window + Left + Dark | `sudo ./install.sh -t forest -p window -i left -c dark -s 1080p` |
| Forest + Float + Right + Dark | `sudo ./install.sh -t forest -p float -i right -c dark -s 1080p` |
| Forest + Sharp + Left + Light | `sudo ./install.sh -t forest -p sharp -i left -c light -s 1080p` |
| Forest + Blur + Right + Dark | `sudo ./install.sh -t forest -p blur -i right -c dark -s 1080p` |

### 2. TEMA MOJAVE 🏜️
| Style | Perintah |
|-------|----------|
| Mojave + Window + Left + Dark | `sudo ./install.sh -t mojave -p window -i left -c dark -s 1080p` |
| Mojave + Float + Right + Dark | `sudo ./install.sh -t mojave -p float -i right -c dark -s 1080p` |
| Mojave + Sharp + Left + Dark | `sudo ./install.sh -t mojave -p sharp -i left -c dark -s 1080p` |
| **Mojave + Window + Right + Dark** | **`sudo ./install.sh -t mojave -p window -i right -c dark -s 1080p`** |

### 3. TEMA MOUNTAIN ⛰️
| Style | Perintah |
|-------|----------|
| Mountain + Window + Left + Dark | `sudo ./install.sh -t mountain -p window -i left -c dark -s 1080p` |
| Mountain + Float + Right + Dark | `sudo ./install.sh -t mountain -p float -i right -c dark -s 1080p` |
| Mountain + Sharp + Left + Light | `sudo ./install.sh -t mountain -p sharp -i left -c light -s 1080p` |
| Mountain + Blur + Right + Dark | `sudo ./install.sh -t mountain -p blur -i right -c dark -s 1080p` |

### 4. TEMA WAVE 🌊
| Style | Perintah |
|-------|----------|
| Wave + Window + Left + Dark | `sudo ./install.sh -t wave -p window -i left -c dark -s 1080p` |
| Wave + Float + Right + Dark | `sudo ./install.sh -t wave -p float -i right -c dark -s 1080p` |
| Wave + Sharp + Left + Light | `sudo ./install.sh -t wave -p sharp -i left -c light -s 1080p` |
| Wave + Blur + Right + Dark | `sudo ./install.sh -t wave -p blur -i right -c dark -s 1080p` |

### 5. DENGAN LOGO 🖼️
| Opsi Logo | Perintah |
|-----------|----------|
| Logo default (gunung) | Tambahkan `-l default` di akhir perintah |
| Logo sistem (Ubuntu) | Tambahkan `-l system` di akhir perintah |
  
**Contoh dengan logo:**
```bash
sudo ./install.sh -t mojave -p window -i right -c dark -s 1080p -l system
```
---
## ⚡ REFERENSI CEPAT (PERINTAH SINGKAT)
### Install Tema
```bash
cd ~/Elegant-grub2-themes-main
sudo ./install.sh -t mojave -p window -i right -c dark -s 1080p
sudo reboot
```
### Ganti Tema
```bash
cd ~/Elegant-grub2-themes-main
sudo ./install.sh -t [tema] -p [style] -i [side] -c [color] -s 1080p
sudo reboot
```
### Uninstall Tema
```bash
cd ~/Elegant-grub2-themes-main
sudo ./install.sh -r -t [tema] -p [style] -i [side] -c [color] -s 1080p
sudo update-grub
sudo reboot
```
### Kembali ke Default Ubuntu
```bash
sudo nano /etc/default/grub
# Hapus baris GRUB_THEME=...
sudo update-grub
sudo reboot
```
### Update GRUB Manual
```bash
sudo update-grub
```
### Cek Tema Aktif
```bash
cat /etc/default/grub | grep GRUB_THEME
```
### Lihat Semua Tema Terinstall
```bash
ls -la /usr/share/grub/themes/
```
---
## 📝 CATATAN PENTING
1. Selalu gunakan sudo karena akses ke /boot/grub membutuhkan root
2. Backup selalu dilakukan sebelum install tema baru
3. Script auto update-grub, tidak perlu manual kecuali ada perubahan manual
4. Resolusi 1080p aman untuk semua layar 16:9
5. Dual boot terdeteksi otomatis oleh os-prober
6. Jika error, gunakan panduan troubleshooting di atas

## Selamat mencoba dan menikmati tema GRUB baru! 🚀  
### Panduan ini disusun berdasarkan pengalaman instalasi pada sistem Ubuntu dual boot dengan Windows.
