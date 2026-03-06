# 🐧 Panduan Lengkap Terminal Linux untuk Developer

> "Dari Windows ke Ubuntu - Cheat Sheet yang Wajib Dikuasai!"

## 📋 Daftar Isi
- [Navigasi Dasar](#-navigasi-dasar-pindah-pindah-folder)
- [Manipulasi File & Folder](#-manipulasi-file--folder)
- [Melihat & Mengedit File](#-melihat--mengedit-file)
- [Permission & Kepemilikan](#-permission--izin-akses)
- [Manajemen Service & Proses](#-manajemen-service--proses)
- [Search & Filter](#-search--filter-grep--find)
- [Install Software (APT)](#-install-software-apt)
- [Network](#-network)
- [Shortcut Terminal](#-shortcut--tips-terminal)
- [Command Developer](#-command-yang-sering-dipakai-developer)
- [Latihan Soal](#-challenge-latihan-mandiri)
- [Troubleshooting](#-error-yang-sering-terjadi)

---

## 🏠 **NAVIGASI DASAR (Pindah-pindah folder)**

```bash
# CEK POSISI
pwd                    # Print working directory - lagi dimana?
# Output: /home/username

# LIHAT ISI FOLDER
ls                     # Lihat isi folder (sederhana)
ls -la                 # Lihat detail lengkap + file tersembunyi
ls -lh                 # Ukuran file dalam format KB/MB/GB
ls -lt                 # Urutkan berdasarkan waktu modifikasi
ls *.php               # Lihat hanya file PHP

# PINDAH FOLDER
cd /var/www           # Pindah ke folder /var/www
cd ~                  # Pindah ke home (/home/username)
cd ..                 # Mundur 1 folder ke atas
cd ../..              # Mundur 2 folder
cd -                  # Kembali ke folder sebelumnya
cd /                  # Pindah ke root folder (paling atas)
```
---

## 📁 MANIPULASI FILE & FOLDER
```bash
# MEMBUAT (CREATE)
mkdir project                    # Buat 1 folder
mkdir -p project/php/css        # Buat folder bertingkat
touch index.php                 # Buat file kosong
touch .env                      # Buat file hidden (titik di depan)
echo "<?php phpinfo(); ?>" > info.php  # Buat file dengan isi

# MENGGANDAKAN (COPY)
cp file.txt file2.txt           # Copy & rename
cp file.txt /var/www/           # Copy ke folder lain
cp -r folder1 folder2           # Copy folder beserta isinya
cp -r * /var/www/html/          # Copy semua file ke folder lain

# MEMINDAHKAN / RENAME (MOVE)
mv file.txt /var/www/           # Pindahkan file
mv lama.txt baru.txt           # Rename file
mv folder1 folder2             # Rename folder
mv *.php ./php-folder/         # Pindah semua file PHP

# MENGHAPUS (REMOVE) - HATI-HATI! ⚠️
rm file.txt                    # Hapus 1 file
rm -f file.txt                # Force hapus (tanpa konfirmasi)
rm -rf folder                 # Hapus folder + isinya (PERMANEN!)
rm -rf *.log                  # Hapus semua file .log

# LINK (Shortcut ala Linux)
ln -s /var/www/html ~/website  # Buat shortcut di home
```
---
## 📝 MELIHAT & MENGEDIT FILE
```bash
# LIHAT ISI FILE
cat file.txt                   # Tampilkan semua isi
cat file1.txt file2.txt > gabungan.txt  # Gabung 2 file
less file.txt                 # Lihat file panjang (spasi=scroll, q=keluar)
head -n 10 file.txt           # Lihat 10 baris pertama
tail -n 20 file.txt           # Lihat 20 baris terakhir
tail -f error.log             # Monitor real-time (Ctrl+C stop)
wc -l file.txt                # Hitung jumlah baris

# EDIT FILE - NANO (Paling mudah untuk pemula)
nano file.txt                 
# Ctrl+O = Simpan, Ctrl+X = Keluar, Ctrl+W = Cari

# EDIT FILE - VS CODE (Kalo udah install)
code .                        # Buka VS Code di folder sekarang
code index.php                # Buka file tertentu

# BANDINGKAN FILE
diff file1.txt file2.txt      # Lihat perbedaan 2 file
```
---
## 👤 PERMISSION & KEPEMILIKAN
```bash
# LIHAT PERMISSION
ls -l file.txt               # -rw-r--r-- (baca detail)
namei -l /var/www/html       # Lihat permission lengkap 1 folder

# UBAH PERMISSION (chmod)
chmod 755 script.sh          # rwx r-x r-x (owner full, group & other read+exec)
chmod 644 index.php          # rw- r-- r-- (owner read/write, group/other read only)
chmod +x script.sh           # Tambah izin execute
chmod -x script.sh           # Hapus izin execute
chmod 777 file.txt           # ⚠️ JANGAN! Kecuali darurat (full akses semua)

# UBAH KEPEMILIKAN (chown)
sudo chown user file.txt     # Ganti owner
sudo chown :group file.txt   # Ganti group
sudo chown user:group file   # Ganti owner & group
sudo chown -R $USER:www-data /var/www/html/  # ★ PALING SERING DIPAKAI!

# UMASK (Default permission untuk file baru)
umask 022                    # File: 644, Folder: 755
```
🔢 **Tabel Angka Permission:**

| Angka | Izin  | Arti                     |
|-------|-------|--------------------------|
| 7     | rwx   | Read, Write, Execute    |
| 6     | rw-   | Read, Write             |
| 5     | r-x   | Read, Execute           |
| 4     | r--   | Read only               |
| 0     | ---   | No access               |

**Penjelasan:**
- **r** = read (4)  - baca
- **w** = write (2) - tulis
- **x** = execute (1) - jalankan
- **-** = tidak ada izin

**Kombinasi Umum:**
| Angka | Izin      | Penggunaan                  |
|-------|-----------|----------------------------|
| 755   | rwx r-x r-x | Folder (default)          |
| 644   | rw- r-- r-- | File (default)           |
| 777   | rwx rwx rwx | ⚠️ JANGAN! (full akses)  |
| 700   | rwx ------  | Private file             |

---
## 🚀 MANAJEMEN SERVICE & PROSES
```bash
# SYSTEMD (Service Manager)
sudo systemctl status apache2     # Cek status Apache
sudo systemctl start apache2      # Start Apache
sudo systemctl stop apache2       # Stop Apache
sudo systemctl restart apache2    # Restart Apache
sudo systemctl reload apache2     # Reload config (tanpa matiin)
sudo systemctl enable apache2     # Auto-start saat boot
sudo systemctl disable apache2    # Matiin auto-start
sudo systemctl daemon-reload      # Reload semua service (setelah edit config)

# LIHAT PROSES
ps aux                          # Semua proses yang jalan
ps aux | grep apache           # Cari proses Apache
ps aux | grep mysql           # Cek MySQL jalan atau tidak
top                            # Monitor real-time (q=keluar)
htop                           # Version top yang lebih keren
pstree                         # Lihat proses dalam tree

# KILL PROSES (T_T)
kill 1234                      # Matiin proses ID 1234
kill -9 1234                  # Paksa mati (force kill)
pkill apache                  # Matiin semua proses Apache
pkill -f "php artisan serve"  # Matiin berdasarkan pattern

# BACKGROUND & FOREGROUND
command &                     # Jalanin di background
Ctrl+Z                       # Suspend proses (pause)
bg                           # Lanjutkan di background
fg                           # Bawa ke foreground
jobs                         # Lihat background jobs
```
---
## 🔍 SEARCH & FILTER (GREP & FIND)
```bash
# GREP - Mencari teks dalam file (WAJIB BISA!)
grep "error" log.txt                # Cari kata "error"
grep -i "user" database.sql        # Case insensitive
grep -r "function" .              # Cari di semua file & subfolder
grep -n "TODO" index.php         # Tampilkan nomor baris
grep -l "config" *.php          # Hanya tampilkan nama file
grep -L "config" *.php          # File yang TIDAK mengandung "config"
grep -c "error" log.txt         # Hitung jumlah kemunculan
grep -v "exclude" file.txt      # Invert - tampilkan yang TIDAK mengandung
grep "^$" file.txt              # Cari baris kosong
grep -E "error|warning" log.txt # Regex - cari error ATAU warning

# GREP COMBO (Sering dipakai)
history | grep apt              # Cari perintah apt yang pernah dijalankan
ps aux | grep mysql           # Cek proses MySQL
php -m | grep mysqli         # Cek extension PHP
composer show | grep laravel # Cek package Laravel
cat /etc/passwd | grep bash  # Cari user yang pake bash

# FIND - Mencari file/folder
find . -name "*.php"                    # Cari semua file PHP
find . -iname "ReadMe.md"              # Case insensitive
find /var -size +100M                 # File lebih dari 100MB
find . -type f -mtime -7             # File diubah 7 hari terakhir
find . -type d -name "vendor"        # Cari folder vendor
find . -empty                       # File/folder kosong
find . -perm 777                    # File dengan permission berbahaya

# FIND + EXECUTE (Advanced)
find . -name "*.tmp" -delete        # Cari dan hapus semua .tmp
find . -name "*.php" -exec chmod 644 {} \;  # Ganti permission semua PHP
find /var/www -user www-data -ls    # Lihat file milik www-data

# WHICH & WHEREIS
which php                          # Lokasi executable PHP
whereis php                       # Semua lokasi terkait PHP
which node                        # Cek Node.js terinstall atau tidak
```
---
## 📦 INSTALL SOFTWARE (APT)
```bash
# UPDATE & UPGRADE (WAJIB RUTIN!)
sudo apt update                  # Update daftar package (cek versi terbaru)
sudo apt upgrade               # Upgrade semua software
sudo apt full-upgrade         # Upgrade total (termasuk dependency)
sudo apt autoremove          # Hapus package ga kepake
sudo apt autoclean          # Hapus file .deb yang udah ga dipake

# SEARCH & INFO
apt search php7.4           # Cari package PHP 7.4
apt show php               # Lihat detail package
apt list --installed       # Semua package terinstall
apt list --upgradable     # Package yang bisa di-upgrade

# INSTALL & REMOVE
sudo apt install nginx     # Install Nginx
sudo apt install -y git curl wget  # Install banyak sekaligus (auto yes)
sudo apt remove nginx      # Uninstall (config masih ada)
sudo apt purge nginx      # Uninstall total + hapus config
sudo apt reinstall php    # Reinstall ulang

# DOWNLOAD .DEB
wget http://archive.ubuntu.com/.../package.deb
sudo dpkg -i package.deb   # Install .deb manual
sudo dpkg -r package      # Remove package .deb
sudo dpkg -l | grep php  # Lihat package .deb terinstall
```
---
## 🌐 NETWORK
```bash
# CEK KONEKSI
ping google.com            # Tes koneksi (Ctrl+C stop)
ping -c 4 google.com      # Ping 4 kali aja
curl google.com           # Tampilkan source HTML
curl -I google.com       # Lihat header aja
wget https://...         # Download file

# IP ADDRESS
ip a                    # Lihat semua interface network (modern)
ip addr show           # Sama seperti di atas
ifconfig              # Legacy (install: sudo apt install net-tools)
hostname -I          # Lihat IP aja

# DNS
nslookup google.com    # Cari IP dari domain
dig google.com        # DNS lookup lebih detail
host google.com       # Simple DNS lookup

# PORT & KONEKSI
netstat -tulpn        # Lihat port yang terbuka (install net-tools)
ss -tulpn            # Modern replacement netstat
lsof -i :80         # Cek proses yang pake port 80
lsof -i :3306       # Cek proses yang pake port MySQL

# SSH
ssh user@192.168.1.10     # Remote ke server
ssh-keygen -t rsa        # Generate SSH key
ssh-copy-id user@server  # Copy public key ke server
```
---
## 🎮 SHORTCUT & TIPS TERMINAL
```bash
# SHORTCUT YANG MENYELAMATKAN!
Tab                     # Auto-complete (SAVE LIVES!)
Tab Tab                # Lihat semua kemungkinan

Ctrl + C              # STOP/Cancel perintah (DARURAT!)
Ctrl + D              # Logout/EOF (keluar terminal)
Ctrl + Z              # Suspend proses (pause)
Ctrl + L              # Bersihkan layar (clear)
Ctrl + A              # Kursor ke AWAL baris
Ctrl + E              # Kursor ke AKHIR baris
Ctrl + U              # Hapus dari kursor ke KIRI
Ctrl + K              # Hapus dari kursor ke KANAN
Ctrl + W              # Hapus 1 kata ke kiri
Alt + Backspace       # Hapus 1 kata ke kiri
Alt + D              # Hapus 1 kata ke kanan

# HISTORY
history               # Lihat semua perintah
history 20           # Lihat 20 perintah terakhir
!!                   # Ulangi perintah TERAKHIR
!100                 # Ulangi perintah nomor 100
!php                 # Ulangi perintah terakhir yang dimulai "php"
sudo !!              # Ulangi perintah terakhir dengan sudo (HIDUP!)
Ctrl + R            # Cari di history (reverse search)
Ctrl + R lagi       # Next match

# VARIABEL & ALIAS
echo $PATH           # Lihat PATH environment
export EDITOR=nano   # Set default editor
alias webserver='cd /var/www/html'  # Buat shortcut
alias ..='cd ..'     # Biar bisa ketik ".." aja
unalias webserver   # Hapus alias

# MULTIPLE COMMANDS
command1 ; command2        # Jalanin berurutan
command1 && command2       # Command2 jalan KALO command1 sukses
command1 || command2       # Command2 jalan KALO command1 gagal
command1 & command2       # Jalanin di background & foreground
```
---
## 🛠️ COMMAND YANG SERING DIPAKAI DEVELOPER
```bash
# GIT (Version Control)
git init
git add .
git commit -m "pesan"
git push origin main
git pull origin main
git status
git log --oneline

# COMPOSER (PHP)
composer init
composer install
composer require laravel/ui
composer update
composer dump-autoload

# NPM (Node.js)
npm init -y
npm install
npm install axios
npm run dev
npm run build

# PHP
php -v                     # Cek versi PHP
php -m                     # Lihat semua extension
php -i | grep memory      # Cek konfigurasi PHP
php artisan serve         # Jalanin Laravel
php -S localhost:8000     # Built-in server

# MYSQL
mysql -u root -p          # Login MySQL
mysql -u root -p dbname < dump.sql  # Import database
mysqldump -u root -p dbname > dump.sql  # Export database
systemctl status mysql   # Cek status MySQL

# DOCKER
docker ps                # Lihat container jalan
docker ps -a           # Semua container
docker images          # Lihat images
docker-compose up -d  # Jalanin docker compose

# LOGS (Error hunting)
sudo tail -f /var/log/apache2/error.log
sudo tail -f /var/log/nginx/error.log
sudo journalctl -u apache2 -f
sudo journalctl -u mysql -f

# PERMISSION FIX (Sering banget!)
sudo chown -R $USER:www-data .
sudo chmod -R 775 .
sudo chmod -R 775 storage bootstrap/cache  # Khusus Laravel
```
---
## ⚠️ ERROR YANG SERING TERJADI
### ❌ "Permission denied"
```bash
# Penyebab: File/folder bukan milik user
# Solusi:
sudo chown -R $USER:www-data folder/
sudo chmod -R 755 folder/
```
### ❌ "Command not found"
```bash
# Penyebab: Belum install / PATH salah
# Solusi:
sudo apt install [nama-command]
which [command]  # Cek lokasi
```
### ❌ "Port 80 already in use"
```bash
# Penyebab: Apache/Nginx udah jalan
# Solusi:
sudo systemctl stop apache2
sudo lsof -i :80  # Cek siapa yang pake
```
### ❌ "Connection refused"
```bash
# Penyebab: Service belum jalan
# Solusi:
sudo systemctl start mysql
sudo systemctl status mysql
```
---
## 📚 SUMBER BELAJAR LANJUTAN
```bash
# BUILT-IN HELP
command --help        # TL;DR - ringkas
man command          # Manual lengkap (q untuk keluar)
info command        # Alternative manual
tldr command       # Contoh praktis (install: sudo apt install tldr)

# WEBSITE & CHEATSHEET
# - https://explainshell.com  (Jelasin arti command)
# - https://cheat.sh        (Cheat sheet via terminal)
# - https://linuxjourney.com (Interaktif learning)

# INSTALL CHEAT (CLI Cheatsheet)
sudo apt install cheat
cheat tar           # Lihat contoh command tar
cheat grep          # Lihat contoh command grep
```
