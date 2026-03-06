# 📘 Management System LAMP
> Linux, Apache, MySQL, PHP - Complete Guide dengan Troubleshooting
---
## 📘 Daftar Isi 
- [🚦 MANAJEMEN SERVICE LENGKAP](#-manajemen-service-lengkap)
- [🆘 TROUBLESHOOTING LENGKAP](#-troubleshooting-lengkap)
- [📊 MONITORING DAN LOGGING](#-monitoring-dan-logging)
- [🔐 KEAMANAN LAMP](#-keamanan-lamp)
- [🚀 OPTIMASI PERFORMANCE](#-optimasi-performance)
- [🔥 APACHE & MYSQL: AUTO START VS MANUAL START](#-apache--mysql-auto-start-vs-manual-start)
- [📦 BACKUP DAN RESTORE](#-backup-dan-restore)
- [🎯 VIRTUAL HOST (MULTIPLE DOMAIN)](#-virtual-host-multiple-domain)
- [🐘 PHP VERSI MANAGEMENT](#-php-versi-management)
- [📈 PERFORMANCE TESTING](#-performance-testing)
- [🐳 DOCKER ALTERNATIVE](#-docker-alternative)
- [🎓 CHEAT SHEET LENGKAP](#-cheat-sheet-lengkap)
- [📋 TEMPLATE PROJECT READY-TO-USE](#-template-project-ready-to-use)
- [🎯 KESIMPULAN AKHIR](#-kesimpulan-akhir)
---
## 🚦 MANAJEMEN SERVICE LENGKAP
### 1. Systemd Service Management (Cara Modern)
```bash
# 🔵 CEK STATUS SERVICE
sudo systemctl status apache2      # Cek status Apache
sudo systemctl status mysql        # Cek status MySQL
sudo systemctl status mariadb      # Cek status MariaDB
sudo systemctl status --all | grep -E "apache2|mysql|mariadb"  # Cek semua

# 🟢 MENYALAKAN SERVICE
sudo systemctl start apache2       # Start Apache
sudo systemctl start mysql         # Start MySQL
sudo systemctl start mariadb       # Start MariaDB
sudo systemctl start apache2 mysql # Start kedua service sekaligus

# 🔴 MEMATIKAN SERVICE
sudo systemctl stop apache2        # Stop Apache
sudo systemctl stop mysql          # Stop MySQL
sudo systemctl stop mariadb        # Stop MariaDB
sudo systemctl stop apache2 mysql  # Stop kedua service

# 🔄 RESTART / RELOAD SERVICE
sudo systemctl restart apache2     # Restart Apache (mati dulu baru nyala)
sudo systemctl reload apache2      # Reload Apache (tanpa mati total)
sudo systemctl restart mysql       # Restart MySQL
sudo systemctl restart mariadb     # Restart MariaDB

# ⚡ ENABLE / DISABLE (AUTO START SAAT BOOT)
sudo systemctl enable apache2      # Apache nyala otomatis saat boot
sudo systemctl disable apache2     # Apache tidak nyala otomatis
sudo systemctl enable mysql        # MySQL nyala otomatis saat boot
sudo systemctl disable mysql       # MySQL tidak nyala otomatis
sudo systemctl is-enabled apache2  # Cek status enable/disable
sudo systemctl is-enabled mysql    # Cek status enable/disable

# 📋 LIHAT DEPENDENCIES
sudo systemctl list-dependencies apache2  # Service yang dibutuhkan Apache
sudo systemctl list-dependencies mysql    # Service yang dibutuhkan MySQL
```
### 2. Service Management Cara Lama (SysVinit)
```bash
# Cara lama (masih support)
sudo service apache2 status
sudo service apache2 start
sudo service apache2 stop
sudo service apache2 restart
sudo service apache2 reload

sudo service mysql status
sudo service mysql start
sudo service mysql stop
sudo service mysql restart

sudo service mariadb status
sudo service mariadb start
sudo service mariadb stop
sudo service mariadb restart
```
### 3. Cek Proses dan Port
```bash
# 🔍 CEK PROSES YANG BERJALAN
ps aux | grep apache2      # Lihat proses Apache
ps aux | grep mysql        # Lihat proses MySQL
ps aux | grep mariadb      # Lihat proses MariaDB
pgrep -la apache2          # PID Apache
pgrep -la mysql            # PID MySQL
pgrep -la mariadb          # PID MariaDB

# 🔌 CEK PORT YANG DIGUNAKAN
sudo lsof -i :80           # Siapa yang pakai port 80 (HTTP)
sudo lsof -i :443          # Siapa yang pakai port 443 (HTTPS)
sudo lsof -i :3306         # Siapa yang pakai port 3306 (MySQL)
sudo netstat -tlnp | grep -E ":80|:443|:3306"  # Lihat port listening
sudo ss -tlnp | grep -E ":80|:443|:3306"       # Alternatif netstat
```
---
## 🆘 TROUBLESHOOTING LENGKAP
### 1. Apache Tidak Bisa Start - Diagnosa Lengkap
```bash
# ❌ APACHE ERROR - SOLUSI LENGKAP

# 1. CEK ERROR LOG (WAJIB!)
sudo tail -f /var/log/apache2/error.log           # Real-time log
sudo tail -100 /var/log/apache2/error.log         # 100 baris terakhir
sudo cat /var/log/apache2/error.log | grep -i error  # Filter error
sudo journalctl -u apache2 --since "5 minutes ago"   # Log via systemd

# 2. CEK SINTAKS KONFIGURASI
sudo apache2ctl configtest        # Test semua konfigurasi
sudo apache2ctl -S                # Lihat virtual host aktif
sudo apache2ctl -M               # Lihat module yang aktif
sudo apache2ctl -V               # Lihat versi dan setting

# 3. CEK PORT 80
sudo lsof -i :80                  # Cek apakah port 80 dipakai
sudo netstat -tlnp | grep :80     # Alternatif
# Kalau dipakai nginx:
sudo systemctl stop nginx         # Matikan nginx
sudo systemctl disable nginx      # Nonaktifkan auto-start

# 4. CEK PERMISSION
ls -la /var/www/html/            # Cek permission web root
ls -ld /home/[user]/pemrograman/php/  # Cek permission folder project
sudo chown -R www-data:www-data /var/www/html/  # Fix ownership

# 5. CEK MODUL PHP
sudo a2enmod php8.2              # Aktifkan modul PHP (sesuai versi)
sudo a2dismod php8.2            # Nonaktifkan modul PHP
sudo systemctl restart apache2

# 6. RESET APACHE KE DEFAULT
sudo apt install --reinstall apache2 -y  # Reinstall Apache
sudo systemctl start apache2
```
### 2. MySQL/MariaDB Tidak Bisa Start - Diagnosa Lengkap
```bash
# ❌ MYSQL ERROR - SOLUSI LENGKAP

# 1. CEK ERROR LOG
sudo tail -f /var/log/mysql/error.log           # MySQL error log
sudo tail -100 /var/log/mysql/error.log
sudo journalctl -u mysql --since "5 minutes ago"
sudo journalctl -u mariadb --since "5 minutes ago"

# 2. CEK PORT 3306
sudo lsof -i :3306                # Cek apakah port 3306 dipakai
sudo netstat -tlnp | grep :3306

# 3. CEK FOLDER DATABASE
sudo ls -la /var/lib/mysql/      # Cek folder database
sudo du -sh /var/lib/mysql/      # Cek ukuran total database
sudo chown -R mysql:mysql /var/lib/mysql/  # Fix ownership

# 4. RESET PASSWORD MYSQL (LUPA PASSWORD)
sudo mysql                      # Kalau bisa login tanpa password
# atau
sudo mysqld_safe --skip-grant-tables &  # Start dalam mode safe
mysql -u root
FLUSH PRIVILEGES;
ALTER USER 'root'@'localhost' IDENTIFIED BY 'root123';
FLUSH PRIVILEGES;
EXIT;
sudo pkill mysqld
sudo systemctl restart mysql

# 5. REPAIR DATABASE CORRUPT
sudo mysqlcheck -u root -p --auto-repair --all-databases
sudo mysqlcheck -u root -p --optimize --all-databases
sudo mysqlcheck -u root -p --analyze --all-databases

# 6. REINSTALL MYSQL (TANPA HILANGKAN DATABASE)
sudo apt install --reinstall mysql-server mysql-client -y
sudo mysql_upgrade -u root -p   # Upgrade/repair system tables
sudo systemctl restart mysql
```
### 3. PHP Error - Diagnosa Lengkap
```bash
# ❌ PHP ERROR - SOLUSI LENGKAP

# 1. CEK VERSI PHP
php -v                          # Versi PHP CLI
php -m                          # Module yang terinstall
php -i | grep "Loaded Configuration File"  # Lokasi php.ini

# 2. CEK MODUL PHP DI APACHE
ls /etc/apache2/mods-enabled/ | grep php
sudo a2enmod php8.2            # Aktifkan modul PHP 8.2
sudo a2enmod php8.3            # Aktifkan modul PHP 8.3
sudo systemctl restart apache2

# 3. CEK EXTENSIONS PHP
php -m | grep mysql            # Cek extension database
php -m | grep gd               # Cek extension gambar
php -m | grep curl             # Cek extension curl
php -m | grep mbstring         # Cek extension multibyte
php -m | grep xml              # Cek extension XML
php -m | grep zip              # Cek extension ZIP

# 4. INSTALL EXTENSIONS PHP
sudo apt search php- | grep -E "^php-.*/"  # Cari semua extension
sudo apt install php-mysql php-curl php-gd php-mbstring php-xml php-zip php-intl -y

# 5. UBAH PHP.INI UNTUK DEVELOPMENT
sudo nano /etc/php/8.2/apache2/php.ini  # Sesuai versi PHP

# SETTING UNTUK DEVELOPMENT (WAJIB!)
error_reporting = E_ALL
display_errors = On
display_startup_errors = On
log_errors = On
error_log = /var/log/php_errors.log
max_execution_time = 300
max_input_time = 300
memory_limit = 256M
post_max_size = 64M
upload_max_filesize = 64M
date.timezone = Asia/Jakarta

# 6. BUAT LOG PHP SENDIRI
sudo touch /var/log/php_errors.log
sudo chown www-data:www-data /var/log/php_errors.log
sudo chmod 644 /var/log/php_errors.log

# 7. RESTART APACHE
sudo systemctl restart apache2
```
---
## 📊 MONITORING DAN LOGGING
### 1. Log Files Lengkap
```bash
# 📁 LOKASI LOG PENTING

# APACHE LOGS
/var/log/apache2/access.log     # Semua akses ke web server
/var/log/apache2/error.log      # Semua error Apache
/var/log/apache2/other_vhosts_access.log  # Akses virtual host

# MYSQL LOGS
/var/log/mysql/error.log        # Error MySQL
/var/log/mysql/mysql.log        # Semua query (jika diaktifkan)
/var/log/mysql/mariadb.log      # Error MariaDB

# PHP LOGS
/var/log/php_errors.log         # Custom PHP error log
/var/log/apache2/php-error.log  # PHP error via Apache

# SYSTEM LOGS
/var/log/syslog                 # System log
/var/log/auth.log              # Authentication log
```
### 2. Cara Membaca Log Real-time
``` bash
# 👁️ MONITORING REAL-TIME

# 1. TONTON LIVE LOGS
sudo tail -f /var/log/apache2/error.log      # Live Apache error
sudo tail -f /var/log/apache2/access.log     # Live akses website
sudo tail -f /var/log/mysql/error.log        # Live MySQL error
sudo tail -f /var/log/php_errors.log         # Live PHP error

# 2. FILTER LOG
sudo tail -f /var/log/apache2/error.log | grep -i "php"  # Hanya PHP error
sudo tail -f /var/log/apache2/access.log | grep -i "404"  # Hanya 404
sudo tail -f /var/log/mysql/error.log | grep -i "access"  # Hanya access denied

# 3. CEK ERROR TERAKHIR
sudo tail -50 /var/log/apache2/error.log     # 50 error terakhir
sudo head -20 /var/log/apache2/error.log     # 20 error pertama
sudo cat /var/log/apache2/error.log | wc -l  # Hitung jumlah error

# 4. LOG ROTATION (Jangan sampai log penuh)
ls -la /var/log/apache2/error.log*           # Lihat log yang sudah di-rotate
sudo logrotate -f /etc/logrotate.conf        # Force rotate log
```
### 3. Monitoring Resource
```bash
# 💻 CEK RESOURCE

# 1. CPU & MEMORY
htop                                    # Interactive process viewer
top                                     # Task manager
sudo apt install htop -y               # Install htop

# 2. APACHE PERFORMANCE
sudo apache2ctl -S                     # Virtual host list
sudo apache2ctl -M                    # Loaded modules
sudo apache2ctl status                # Apache status (perlu mod_status)

# 3. MYSQL PERFORMANCE
mysqladmin -u root -p status          # Status MySQL
mysqladmin -u root -p processlist     # Query yang sedang jalan
mysqladmin -u root -p variables       # Semua variabel MySQL

# 4. DISK USAGE
df -h                                 # Kapasitas disk
du -sh /var/lib/mysql/               # Ukuran database
du -sh /var/www/                     # Ukuran website
```
---
## 🔐 KEAMANAN LAMP
### 1. Firewall Setup
```bash
# 🛡️ UFW - Uncomplicated Firewall

# 1. CEK STATUS
sudo ufw status                      # Cek status firewall
sudo ufw status verbose              # Status detail

# 2. SETUP DASAR
sudo ufw default deny incoming       # Blok semua incoming
sudo ufw default allow outgoing      # Allow semua outgoing
sudo ufw allow ssh                  # Allow SSH (port 22)
sudo ufw allow 80/tcp              # Allow HTTP
sudo ufw allow 443/tcp             # Allow HTTPS
sudo ufw allow 3306/tcp            # Allow MySQL (hati-hati!)

# 3. AKTIFKAN
sudo ufw enable                     # Aktifkan firewall
sudo ufw status numbered           # Lihat rules dengan nomor
sudo ufw delete [number]           # Hapus rule tertentu

# 4. UNTUK DEVELOPMENT (Lokal aja)
sudo ufw allow from 127.0.0.1 to any port 3306  # MySQL hanya lokal
sudo ufw allow from 192.168.0.0/24 to any port 80  # Allow LAN
```
### 2. MySQL Security Hardening
```bash
# 🔒 AMANKAN MYSQL

# 1. JALANKAN SECURITY SCRIPT
sudo mysql_secure_installation

# 2. HAPUS USER ANONIM
mysql -u root -p -e "DELETE FROM mysql.user WHERE User='';"
mysql -u root -p -e "FLUSH PRIVILEGES;"

# 3. NONAKTIFKAN REMOTE ROOT LOGIN
mysql -u root -p -e "DELETE FROM mysql.user WHERE User='root' AND Host NOT IN ('localhost', '127.0.0.1', '::1');"
mysql -u root -p -e "FLUSH PRIVILEGES;"

# 4. BUAT USER KHUSUS (BUKAN ROOT)
mysql -u root -p -e "CREATE USER 'developer'@'localhost' IDENTIFIED BY 'password123';"
mysql -u root -p -e "GRANT ALL PRIVILEGES ON *.* TO 'developer'@'localhost';"
mysql -u root -p -e "FLUSH PRIVILEGES;"

# 5. BATASI AKSES FILE
sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf

# Tambahkan:
[mysqld]
local-infile=0                     # Nonaktifkan LOAD DATA LOCAL
skip-symbolic-links               # Nonaktifkan symbolic links
max_allowed_packet=64M           # Limit packet size
wait_timeout=600                # Timeout 10 menit
interactive_timeout=600        # Timeout untuk interactive
max_connections=100           # Limit koneksi
```
### 3. Apache Security Hardening
```bash
# 🔒 AMANKAN APACHE

# 1. SEMBUNYIKAN VERSI APACHE
sudo nano /etc/apache2/apache2.conf

ServerTokens Prod                # Hanya tampilkan "Apache"
ServerSignature Off             # Jangan tampilkan signature

# 2. NONAKTIFKAN DIRECTORY LISTING
sudo nano /etc/apache2/apache2.conf

<Directory /home/[user]/pemrograman/php>
    Options -Indexes            # Tambahkan minus (-) sebelum Indexes
    AllowOverride All
    Require all granted
</Directory>

# 3. BATASI AKSES KE .HTACCESS DAN .HTPASSWD
sudo nano /etc/apache2/apache2.conf

<FilesMatch "^\.">
    Require all denied
</FilesMatch>

# 4. INSTALL MODUL SECURITY (OPSIONAL)
sudo apt install libapache2-mod-security2 -y
sudo a2enmod security2
sudo systemctl restart apache2

# 5. PROTECT DIRECTORY DENGAN PASSWORD
sudo apt install apache2-utils -y
sudo htpasswd -c /etc/apache2/.htpasswd admin  # Buat user admin
```
---
## 🚀 OPTIMASI PERFORMANCE
### 1. Optimasi Apache
```bash
# ⚡ MEMPERCEPAT APACHE

# 1. AKTIFKAN COMPRESSION
sudo a2enmod deflate
sudo a2enmod headers
sudo systemctl restart apache2

sudo nano /etc/apache2/apache2.conf
# Tambahkan:
AddOutputFilterByType DEFLATE text/html text/plain text/xml text/css text/javascript application/javascript

# 2. AKTIFKAN CACHING
sudo a2enmod expires
sudo a2enmod cache
sudo a2enmod cache_disk
sudo systemctl restart apache2

# 3. OPTIMASI MAX CLIENTS
sudo nano /etc/apache2/mods-available/mpm_prefork.conf

<IfModule mpm_prefork_module>
    StartServers             5
    MinSpareServers          5
    MaxSpareServers         10
    MaxRequestWorkers      150
    MaxConnectionsPerChild 3000
</IfModule>

# 4. KEEP ALIVE
sudo nano /etc/apache2/apache2.conf

KeepAlive On
MaxKeepAliveRequests 100
KeepAliveTimeout 5
```
### 2. Optimasi MySQL
```bash
# ⚡ MEMPERCEPAT MYSQL

# 1. OPTIMASI DENGAN MySQLTuner
sudo apt install mysqltuner -y
sudo mysqltuner

# 2. SETUP INNODB
sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf

[mysqld]
innodb_buffer_pool_size = 256M    # 60-70% dari RAM
innodb_log_file_size = 64M
innodb_flush_log_at_trx_commit = 2  # 1 = paling aman, 2 = lebih cepat
innodb_flush_method = O_DIRECT

# 3. QUERY CACHE (MariaDB)
sudo nano /etc/mysql/mariadb.conf.d/50-server.cnf

query_cache_type = 1
query_cache_size = 32M
query_cache_limit = 1M

# 4. RESTART MYSQL
sudo systemctl restart mysql
```
### 3. Optimasi PHP
```bash
# ⚡ MEMPERCEPAT PHP

# 1. OPCACHE
sudo nano /etc/php/8.2/apache2/php.ini

[opcache]
opcache.enable=1
opcache.memory_consumption=128
opcache.interned_strings_buffer=8
opcache.max_accelerated_files=4000
opcache.revalidate_freq=60
opcache.fast_shutdown=1

# 2. REALPATH CACHE
; Realpath cache
realpath_cache_size = 4096k
realpath_cache_ttl = 120

# 3. PHP WORKERS
sudo apt install php-fpm -y
sudo a2enmod proxy_fcgi setenvif
sudo a2enconf php8.2-fpm
sudo systemctl restart apache2
```
---
## 🔥 APACHE & MYSQL: AUTO START VS MANUAL START
> Saat ini: Apache dan MySQL TIDAK otomatis nyala saat laptop dinyalakan. HARUS MANUAL!
> Bisa diatur: Bisa dibuat OTOMATIS atau MANUAL sesuai kebutuhan.
### 🎯 MANAJEMEN AUTO START SERVICE
### 1. CEK STATUS AUTO START SAAT INI
```bash
# Cek apakah service otomatis nyala saat boot
sudo systemctl is-enabled apache2
sudo systemctl is-enabled mysql

# Output:
# - "enabled"  → Otomatis nyala saat boot
# - "disabled" → Tidak otomatis nyala (harus manual)
# - "static"   → Tidak bisa diatur enable/disable
```
### 2. Jika Ingin OTOMATIS NYALA SAAT BOOT:
```bash

# Apache otomatis nyala saat laptop dinyalakan
sudo systemctl enable apache2

# MySQL otomatis nyala saat laptop dinyalakan
sudo systemctl enable mysql

# Cek hasilnya
sudo systemctl is-enabled apache2  # Harusnya "enabled"
sudo systemctl is-enabled mysql    # Harusnya "enabled"
```
### ✅ KEUNTUNGAN AUTO START:
- Tidak perlu repot start manual setiap kali
- Langsung bisa akses localhost dan database
- Cocok untuk daily development

### ❌ KERUGIAN AUTO START:
- Boros resource (RAM/CPU) walau laptop tidak dipakai ngoding
- Service jalan di background terus
- Baterai laptop lebih cepat habis
- Laptop lebih panas
---
### 3. Jika Ingin MANUAL SAJA (START SENDIRI):
```bash
# Matikan auto start
sudo systemctl disable apache2
sudo systemctl disable mysql

# Cek hasilnya
sudo systemctl is-enabled apache2  # Harusnya "disabled"
sudo systemctl is-enabled mysql    # Harusnya "disabled"
```
### ✅ KEUNTUNGAN MANUAL:
- Hemat resource saat tidak ngoding
- Baterai lebih awet
- Laptop lebih dingin
- Kontrol penuh kapan service nyala/mati

### ❌ KERUGIAN MANUAL:
- Harus ingat start dulu sebelum ngoding
- Kalau lupa start, website error
- Repot kalau tiap hari ngoding

### 4. KOMBINASI TERBAIK (REKOMENDASI):
```bash
# 1. SET KE MANUAL (disabled)
sudo systemctl disable apache2
sudo systemctl disable mysql

# 2. BUAT ALIAS SUPER CEPAT 
echo "alias startweb='sudo systemctl start apache2 && sudo systemctl start mysql'" >> ~/.bashrc
echo "alias stopweb='sudo systemctl stop apache2 && sudo systemctl stop mysql'" >> ~/.bashrc
source ~/.bashrc

# 3. TAMBAHKAN ALIAS CEK STATUS
echo "alias cekweb='sudo systemctl status apache2 | grep Active && sudo systemctl status mysql | grep Active'" >> ~/.bashrc
source ~/.bashrc
```
CARA PAKAI:
```bash
# Pagi mulai ngoding
startweb   # 1 detik, service nyala

# Cek status
cekweb     # Lihat apakah sudah running

# Sore selesai ngoding
stopweb    # 1 detik, service mati
```
---
## 🔄 SKENARIO LENGKAP
### SKENARIO 1: LAPTOP PRIBADI (NGODING TIAP HARI)
```bash

# SETUP: Auto start
sudo systemctl enable apache2
sudo systemctl enable mysql

# KONDISI:
# - Nyalakan laptop → Apache & MySQL otomatis nyala
# - Buka browser → localhost langsung bisa
# - Matikan laptop → Service ikut mati
# - Nyalakan lagi → Service nyala lagi otomatis

# CEK:
sudo systemctl status apache2 | grep "Active"
# Output: Active: active (running) since...
```
### SKENARIO 2: LAPTOP KULIAH/KANTOR (NGODING KADANG-KADANG)
```bash
# SETUP: Manual
sudo systemctl disable apache2
sudo systemctl disable mysql

# KONDISI:
# - Nyalakan laptop → Service mati
# - Mau ngoding → ketik: startweb
# - Selesai ngoding → ketik: stopweb
# - Lupa matikan → Service tetap jalan sampai shutdown
# - Shutdown laptop → Service ikut mati

# CEK STATUS DI PAGI HARI:
cekweb
# Output: Active: inactive (dead)
```
### SKENARIO 3: SERVER PRODUCTION (24/7)
```bash
# SETUP: Auto start + Auto restart kalau crash
sudo systemctl enable apache2
sudo systemctl enable mysql

# Tambahkan auto restart kalau crash
sudo nano /etc/systemd/system/multi-user.target.wants/apache2.service

# Tambahkan di [Service] section:
Restart=always
RestartSec=10

# Reload systemd
sudo systemctl daemon-reload
sudo systemctl restart apache2
```
---
## ⚡ APA YANG TERJADI SAAT LAPTOP DIMATIKAN?
### 1. PROSES SHUTDOWN NORMAL:
```bash
# Saat shutdown laptop:
sudo shutdown now
# atau
sudo poweroff
# atau klik tombol power di GUI

# YANG TERJADI:
# 1. Systemd mengirim sinyal TERM ke semua service
# 2. Apache menerima sinyal → stop gracefully
# 3. MySQL menerima sinyal → stop dengan commit data terakhir
# 4. Semua service mati dengan aman
# 5. Laptop mati

# TIDAK ADA RISIKO KORUPSI DATA!
```
### 2. PROSES RESTART:
```bash
# Saat restart:
sudo reboot

# SAMA SEPERTI SHUTDOWN:
# 1. Service mati dengan aman
# 2. Laptop restart
# 3. Service nyala lagi (kalau enable)
# 4. Atau tetap mati (kalau disable)
```
### 3. YANG HARUS DIHINDARI:
```bash
# ❌ JANGAN PERNAH LAKUKAN INI:
# 1. Tekan tombol power 5 detik (force shutdown)
# 2. Cabut baterai saat laptop menyala
# 3. Tutup laptop tanpa shutdown (sleep mode OK)

# ⚠️ RESIKO:
# - Database corrupt
# - File config corrupt
# - Error saat start ulang
# - Perlu repair database
```
---
## 💡 TIPS & TRIK MANAJEMEN SERVICE
### 1. BUAT MENU INTERAKTIF (COOL!)
```bash
nano ~/web-manager.sh
```
```bash
#!/bin/bash
# Web Server Manager - LAMP Control Panel

while true; do
    clear
    echo "=================================="
    echo "   🌐 LAMP WEB MANAGER"
    echo "=================================="
    echo "1. Start Apache & MySQL"
    echo "2. Stop Apache & MySQL"
    echo "3. Restart Apache & MySQL"
    echo "4. Status Apache & MySQL"
    echo "5. Enable Auto Start (Boot)"
    echo "6. Disable Auto Start (Manual)"
    echo "7. View Error Log"
    echo "8. Exit"
    echo "=================================="
    read -p "Pilih menu [1-8]: " menu
    
    case $menu in
        1) sudo systemctl start apache2 mysql
           echo "✅ Service started!"
           sleep 2;;
        2) sudo systemctl stop apache2 mysql
           echo "🛑 Service stopped!"
           sleep 2;;
        3) sudo systemctl restart apache2 mysql
           echo "🔄 Service restarted!"
           sleep 2;;
        4) sudo systemctl status apache2 mysql | grep Active
           sleep 5;;
        5) sudo systemctl enable apache2 mysql
           echo "✅ Auto Start ENABLED"
           sleep 2;;
        6) sudo systemctl disable apache2 mysql
           echo "✅ Auto Start DISABLED"
           sleep 2;;
        7) sudo tail -30 /var/log/apache2/error.log
           read -p "Press enter..." ;;
        8) echo "Bye!"; exit 0;;
        *) echo "Pilihan tidak valid!"; sleep 2;;
    esac
done
```
```bash
# Buat executable
chmod +x ~/web-manager.sh

# Jalankan
./web-manager.sh

# Buat alias
echo "alias webman='~/web-manager.sh'" >> ~/.bashrc
source ~/.bashrc

# Tinggal ketik:
webman
```
### 2. MONITORING SERVICE REAL-TIME
```bash
# 1. Install tmux (terminal multiplexer)
sudo apt install tmux -y

# 2. Buat session monitor
tmux new -s lamp-monitor

# 3. Split terminal (Ctrl+b, ")
# Panel 1: htop
htop

# Panel 2: (Ctrl+b, arrow down)
sudo tail -f /var/log/apache2/error.log

# Panel 3: (Ctrl+b, arrow down lagi)
watch -n 1 'sudo systemctl status apache2 mysql | grep Active'

# Keluar: Ctrl+b, d (detach)
# Masuk lagi: tmux attach -t lamp-monitor
```
### 3. AUTO START TAPI HEMAT BATTERY
```bash
#!/bin/bash
# ~/.config/autostart/lamp.desktop
# Untuk GUI Ubuntu - Start service tapi hanya saat dibutuhkan?

# Sebenarnya ini tidak direkomendasikan
# Lebih baik manual dengan alias startweb
```
---
## 🎯 REKOMENDASI
Berdasarkan kebutuhan typical developer:
```bash
# ✅ SETUP IDEAL UNTUK KAMU:
sudo systemctl disable apache2
sudo systemctl disable mysql

# ✅ ALIAS SUPER CEPAT (udah dibuat):
startweb    # Start service
stopweb     # Stop service
statusweb   # Cek status
cekweb      # Cek status singkat
gotophp     # Ke folder project
```
### 📋 ROUTINE HARIAN:
```text
🟢 PAGI (Mulai ngoding):
1. Buka laptop
2. Buka terminal
3. Ketik: startweb
4. Ketik: gotophp
5. Buka VS Code: code .
6. Buka browser: localhost/php/projectmu
7. Mulai ngoding!

🔴 SORE (Selesai ngoding):
1. Simpan semua file
2. Buka terminal
3. Ketik: stopweb
4. Tutup laptop / shutdown
```
### ❓ KAPAN PAKAI AUTO START:
PAKAI AUTO START KALAU:
    ✅ Ngoding tiap hari, pagi sampai sore

    ✅ Lupa start service

    ✅ Malas ketik startweb

    ✅ Laptop tidak terlalu boros baterai

JANGAN PAKAI AUTO START KALAU:

    ❌ Ngoding seminggu sekali

    ❌ Laptop baterainya cepat habis

    ❌ Suka lupa matikan service

    ❌ RAM cuma 4GB atau kurang
---
## 📊 PERBANDINGAN LENGKAP
| Mode               | Auto Start (enable)                 | Manual (disable)                   |
|--------------------|--------------------------------------|-------------------------------------|
| Saat boot          | Langsung nyala                      | Mati                                |
| Saat mau ngoding   | Buka browser langsung               | Ketik `startweb` dulu              |
| Resource saat idle | Boros RAM/CPU                       | Hemat                               |
| Baterai            | Cepat habis                         | Awet                                |
| Suhu laptop        | Lebih panas                         | Dingin                              |
| Kontrol            | Otomatis                            | Manual                              |
| Risiko lupa stop   | Jalan terus                        | Harus stop manual                  |
| Cocok untuk        | Daily dev, Server                  | Kadang-kadang, Belajar             |
---
## 📦 BACKUP DAN RESTORE
### 1. Backup Database Lengkap
```bash
# 💾 BACKUP MYSQL

# 1. BACKUP SINGLE DATABASE
mysqldump -u root -p --databases apotek > ~/backup_apotek.sql
mysqldump -u root -p apotek > ~/backup_apotek.sql  # Tanpa CREATE DATABASE

# 2. BACKUP ALL DATABASES
mysqldump -u root -p --all-databases > ~/backup_all_$(date +%Y%m%d_%H%M%S).sql

# 3. BACKUP DENGAN COMPRESS
mysqldump -u root -p apotek | gzip > ~/backup_apotek.sql.gz
gunzip -c backup_apotek.sql.gz | mysql -u root -p apotek  # Restore

# 4. BACKUP TABEL TERTENTU
mysqldump -u root -p apotek users products > ~/backup_tables.sql

# 5. BACKUP TANPA DATA (HANYA STRUKTUR)
mysqldump -u root -p --no-data apotek > ~/backup_struktur.sql

# 6. BACKUP DENGAN SCHEDULE (CRON)
crontab -e
# Tambahkan: 0 2 * * * mysqldump -u root -p[password] --all-databases > ~/backup/backup_$(date +\%Y\%m\%d).sql
```
### 2. Restore Database
```bash
# 🔄 RESTORE MYSQL

# 1. RESTORE SINGLE DATABASE
mysql -u root -p apotek < ~/backup_apotek.sql

# 2. RESTORE ALL DATABASES
mysql -u root -p < ~/backup_all.sql

# 3. RESTORE DARI COMPRESSED FILE
gunzip < ~/backup_apotek.sql.gz | mysql -u root -p apotek

# 4. IMPORT SQL BESAR (BYPASS LOG)
mysql -u root -p --max_allowed_packet=1024M apotek < ~/backup_besar.sql
```
### 3. Backup File Project
```bash
# 📁 BACKUP FILE PROJECT

# 1. BACKUP FOLDER PROJECT
tar -czvf ~/backup_php_$(date +%Y%m%d).tar.gz ~/pemrograman/php/

# 2. BACKUP DENGAN EXCLUDE
tar -czvf ~/backup_php_exclude_vendor.tar.gz \
    --exclude="~/pemrograman/php/*/vendor" \
    --exclude="~/pemrograman/php/*/node_modules" \
    ~/pemrograman/php/

# 3. RESTORE FILE PROJECT
tar -xzvf ~/backup_php_20250213.tar.gz -C ~/

# 4. SYNC KE EXTERNAL DRIVE
sudo mount /dev/sdb1 /mnt/usb
rsync -avh ~/pemrograman/php/ /mnt/usb/backup_php/
sudo umount /mnt/usb
```
---
## 🎯 VIRTUAL HOST (MULTIPLE DOMAIN)
### 1. Setup Virtual Host untuk Local Development
```bash
# 🌐 VIRTUAL HOST SETUP

# 1. BUAT KONFIGURASI VIRTUAL HOST
sudo nano /etc/apache2/sites-available/apotek.local.conf

<VirtualHost *:80>
    ServerAdmin webmaster@localhost
    ServerName apotek.local
    ServerAlias www.apotek.local
    DocumentRoot /home/all/pemrograman/php/apotek
    
    <Directory /home/all/pemrograman/php/apotek>
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>
    
    ErrorLog ${APACHE_LOG_DIR}/apotek-error.log
    CustomLog ${APACHE_LOG_DIR}/apotek-access.log combined
</VirtualHost>

# 2. AKTIFKAN VIRTUAL HOST
sudo a2ensite apotek.local.conf
sudo a2dissite 000-default.conf  # Nonaktifkan default (opsional)
sudo systemctl reload apache2

# 3. EDIT HOSTS FILE
sudo nano /etc/hosts

127.0.0.1   localhost
127.0.0.1   apotek.local
127.0.0.1   taskflow.local
127.0.0.1   toko-buku.local

# 4. TEST
# Browser: http://apotek.local
```
### 2. Virtual Host dengan SSL (HTTPS) Lokal
```bash
# 🔐 VIRTUAL HOST HTTPS

# 1. AKTIFKAN MODUL SSL
sudo a2enmod ssl
sudo systemctl restart apache2

# 2. BUAT SELF-SIGNED CERTIFICATE
sudo mkdir /etc/apache2/ssl
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/apache2/ssl/apotek.key \
    -out /etc/apache2/ssl/apotek.crt

# 3. BUAT VIRTUAL HOST HTTPS
sudo nano /etc/apache2/sites-available/apotek.local-ssl.conf

<VirtualHost *:443>
    ServerName apotek.local
    DocumentRoot /home/all/pemrograman/php/apotek
    
    SSLEngine on
    SSLCertificateFile /etc/apache2/ssl/apotek.crt
    SSLCertificateKeyFile /etc/apache2/ssl/apotek.key
    
    <Directory /home/all/pemrograman/php/apotek>
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>
</VirtualHost>

# 4. AKTIFKAN
sudo a2ensite apotek.local-ssl.conf
sudo systemctl reload apache2

# 5. TEST
# Browser: https://apotek.local
```
---
## 🐘 PHP VERSI MANAGEMENT
### 1. Install Multiple PHP Versi
```bash
# 🔄 PHP VERSION MANAGEMENT

# 1. TAMBAHKAN REPOSITORY ONDREJ PHP
sudo add-apt-repository ppa:ondrej/php -y
sudo apt update

# 2. INSTALL PHP 7.4, 8.0, 8.1, 8.2, 8.3
sudo apt install php7.4 php7.4-fpm php7.4-mysql -y
sudo apt install php8.0 php8.0-fpm php8.0-mysql -y
sudo apt install php8.1 php8.1-fpm php8.1-mysql -y
sudo apt install php8.2 php8.2-fpm php8.2-mysql -y
sudo apt install php8.3 php8.3-fpm php8.3-mysql -y

# 3. SWITCH PHP VERSI (CLI)
sudo update-alternatives --config php
# Pilih nomor sesuai versi yang diinginkan

# 4. SWITCH PHP VERSI (APACHE)
sudo a2dismod php8.2
sudo a2enmod php8.3
sudo systemctl restart apache2

# 5. CEK VERSI
php -v
```
### 2. Setup PHP-FPM
```bash
# ⚡ PHP-FPM (Lebih Cepat dari mod_php)

# 1. INSTALL PHP-FPM
sudo apt install php8.2-fpm -y

# 2. AKTIFKAN MODUL APACHE UNTUK FPM
sudo a2enmod proxy_fcgi setenvif
sudo a2enconf php8.2-fpm
sudo systemctl restart apache2

# 3. CEK STATUS
sudo systemctl status php8.2-fpm

# 4. KONFIGURASI FPM
sudo nano /etc/php/8.2/fpm/pool.d/www.conf

pm = dynamic
pm.max_children = 50
pm.start_servers = 5
pm.min_spare_servers = 5
pm.max_spare_servers = 35
pm.max_requests = 500
```
---
## 📈 PERFORMANCE TESTING
### 1. Test Kecepatan Website
```bash
# ⏱️ LOAD TESTING

# 1. INSTALL APACHE BENCH
sudo apt install apache2-utils -y

# 2. TEST SINGLE URL
ab -n 1000 -c 10 http://localhost/php/apotek/
# -n 1000: 1000 requests
# -c 10: 10 concurrent requests

# 3. TEST DENGAN KEEP-ALIVE
ab -k -n 1000 -c 10 http://localhost/php/apotek/

# 4. INSTALL SIEGE
sudo apt install siege -y
siege -c 50 -t 30s http://localhost/php/apotek/

# 5. MONITOR SELAMA TEST
htop
sudo tail -f /var/log/apache2/access.log
```
### 2. MySQL Performance Test
```bash
# ⏱️ MYSQL BENCHMARK

# 1. INSTALL MYSQL BENCHMARK
sudo apt install sysbench -y

# 2. TEST CPU
sysbench cpu run

# 3. TEST DISK IO
sysbench fileio --file-total-size=1G prepare
sysbench fileio --file-total-size=1G --file-test-mode=rndrw run
sysbench fileio --file-total-size=1G cleanup

# 4. TEST MYSQL
sysbench oltp_read_write --db-driver=mysql \
    --mysql-user=root --mysql-password=root123 \
    --mysql-db=test --table-size=1000000 prepare
    
sysbench oltp_read_write --db-driver=mysql \
    --mysql-user=root --mysql-password=root123 \
    --mysql-db=test --table-size=1000000 run
    
sysbench oltp_read_write --db-driver=mysql \
    --mysql-user=root --mysql-password=root123 \
    --mysql-db=test cleanup
```
---
## 🐳 DOCKER ALTERNATIVE
### 1. LAMP dengan Docker Compose
```yaml
# docker-compose.yml
version: '3.8'

services:
  apache:
    image: php:8.2-apache
    container_name: lamp-apache
    ports:
      - "8080:80"
    volumes:
      - ~/pemrograman/php:/var/www/html
    depends_on:
      - mysql

  mysql:
    image: mysql:8.0
    container_name: lamp-mysql
    ports:
      - "3307:3306"
    environment:
      MYSQL_ROOT_PASSWORD: root123
      MYSQL_DATABASE: app_db
    volumes:
      - mysql_data:/var/lib/mysql

  phpmyadmin:
    image: phpmyadmin/phpmyadmin
    container_name: lamp-phpmyadmin
    ports:
      - "8081:80"
    environment:
      PMA_HOST: mysql
      PMA_USER: root
      PMA_PASSWORD: root123
    depends_on:
      - mysql

volumes:
  mysql_data:
```
```bash
# Jalankan Docker LAMP
docker-compose up -d
# Akses: http://localhost:8080
# phpMyAdmin: http://localhost:8081
```
---
## 🎓 CHEAT SHEET LENGKAP
### 1. 100+ Perintah LAMP yang Sering Digunakan
```bash
# ============================================
# APACHE COMMANDS - LENGKAP
# ============================================

# INSTALL & REMOVE
sudo apt install apache2 -y
sudo apt remove apache2 -y
sudo apt purge apache2 -y
sudo apt autoremove -y

# SERVICE MANAGEMENT
sudo systemctl start apache2
sudo systemctl stop apache2
sudo systemctl restart apache2
sudo systemctl reload apache2
sudo systemctl status apache2
sudo systemctl enable apache2
sudo systemctl disable apache2
sudo systemctl is-enabled apache2
sudo systemctl is-active apache2

# CONFIG TEST
sudo apache2ctl configtest
sudo apache2ctl -S
sudo apache2ctl -M
sudo apache2ctl -V
sudo apache2ctl -t

# MODULE MANAGEMENT
sudo a2enmod [module]
sudo a2dismod [module]
ls /etc/apache2/mods-available/
ls /etc/apache2/mods-enabled/

# SITE MANAGEMENT
sudo a2ensite [site.conf]
sudo a2dissite [site.conf]
ls /etc/apache2/sites-available/
ls /etc/apache2/sites-enabled/

# LOGS
sudo tail -f /var/log/apache2/error.log
sudo tail -f /var/log/apache2/access.log
sudo grep "ERROR" /var/log/apache2/error.log
sudo journalctl -u apache2 --since today

# ============================================
# MYSQL COMMANDS - LENGKAP
# ============================================

# INSTALL & REMOVE
sudo apt install mysql-server mysql-client -y
sudo apt install mariadb-server mariadb-client -y
sudo apt remove mysql-server -y
sudo apt purge mysql-server -y

# SERVICE MANAGEMENT
sudo systemctl start mysql
sudo systemctl stop mysql
sudo systemctl restart mysql
sudo systemctl status mysql
sudo systemctl enable mysql
sudo systemctl disable mysql

# LOGIN
mysql -u root -p
mysql -u root -p -h localhost
mysql -u root -p --port=3306
mysql -u username -p database_name

# DATABASE OPERATIONS
CREATE DATABASE dbname;
DROP DATABASE dbname;
SHOW DATABASES;
USE dbname;
SHOW TABLES;
DESCRIBE tablename;
SELECT DATABASE();

# USER MANAGEMENT
CREATE USER 'user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'user'@'localhost';
GRANT SELECT, INSERT ON db.* TO 'user'@'localhost';
REVOKE ALL PRIVILEGES ON *.* FROM 'user'@'localhost';
DROP USER 'user'@'localhost';
FLUSH PRIVILEGES;
SELECT user, host FROM mysql.user;

# BACKUP & RESTORE
mysqldump -u root -p dbname > backup.sql
mysqldump -u root -p --all-databases > backup.sql
mysql -u root -p dbname < backup.sql
mysql -u root -p < backup.sql
mysqldump -u root -p dbname table1 table2 > backup_tables.sql

# IMPORT/EXPORT
mysqlimport -u root -p dbname file.txt
mysql -u root -p -e "SELECT * FROM users" dbname > output.csv

# STATUS & INFO
mysqladmin -u root -p status
mysqladmin -u root -p processlist
mysqladmin -u root -p variables
mysqladmin -u root -p extended-status
mysqlcheck -u root -p --all-databases

# ============================================
# PHP COMMANDS - LENGKAP
# ============================================

# INSTALL PHP
sudo apt install php -y
sudo apt install php8.2 php8.2-cli php8.2-common -y
sudo apt install php-mysql php-curl php-gd php-mbstring php-xml php-zip php-intl -y

# VERSION MANAGEMENT
php -v
php -m
php -i
php -ini
php -r "phpinfo();"
php -l filename.php  # Check syntax

# PHP-FPM
sudo systemctl start php8.2-fpm
sudo systemctl stop php8.2-fpm
sudo systemctl restart php8.2-fpm
sudo systemctl status php8.2-fpm

# CONFIGURATION
php -i | grep "Loaded Configuration File"
sudo nano /etc/php/8.2/apache2/php.ini
sudo nano /etc/php/8.2/cli/php.ini

# COMPOSER
composer --version
composer init
composer install
composer update
composer require vendor/package
composer dump-autoload

# ============================================
# FILE SYSTEM & PERMISSION
# ============================================

# PERMISSION
chmod 755 folder/
chmod 644 file.php
chmod -R 775 folder/
chown user:group file
chown -R user:group folder/
sudo usermod -a -G user www-data

# PATH PENTING
/etc/apache2/                  # Konfigurasi Apache
/var/www/html/                 # Default web root
/home/user/pemrograman/php/    # Folder project
/var/lib/mysql/               # Lokasi database
/usr/share/phpmyadmin/       # phpMyAdmin
/etc/mysql/                  # Konfigurasi MySQL
/etc/php/                    # Konfigurasi PHP
/var/log/apache2/            # Log Apache
/var/log/mysql/              # Log MySQL

# ============================================
# NETWORK & PORT
# ============================================

sudo lsof -i :80
sudo lsof -i :3306
sudo netstat -tlnp | grep 80
sudo ss -tlnp | grep 80
sudo ufw status
sudo ufw allow 80/tcp
sudo ufw deny 3306/tcp

# ============================================
# SYSTEM INFO
# ============================================

uname -a                      # Info kernel
lsb_release -a               # Info Ubuntu
df -h                        # Disk space
free -h                      # RAM
htop                         # Process viewer
uptime                       # Waktu nyala
whoami                       # Username
hostname                     # Nama komputer
ip a                         # IP Address
```
---
## 📋 TEMPLATE PROJECT READY-TO-USE
### 1. Template Project PHP dengan Database
```php
<?php
// ============================================
// TEMPLATE PROJECT PHP + MYSQL
// ============================================

// config.php
<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASS', 'root123');
define('DB_NAME', 'project_db');

function getConnection() {
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    $conn->set_charset("utf8mb4");
    return $conn;
}
?>

// index.php
<?php
require_once 'config.php';

// Create connection
$conn = getConnection();

// Test query
$sql = "SELECT 1 as test";
$result = $conn->query($sql);

if ($result) {
    echo "✅ Database connected successfully!";
} else {
    echo "❌ Error: " . $conn->error;
}

$conn->close();
?>

// .htaccess
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ index.php?url=$1 [QSA,L]
```
### 2. Setup Project Baru - 1 Menit!
```bash
#!/bin/bash
# create-php-project.sh
# Script untuk bikin project baru cepat

echo "🚀 Create New PHP Project"
echo "========================"

# Input project name
read -p "Project name: " project_name

# Create folder structure
mkdir -p ~/pemrograman/php/$project_name
mkdir -p ~/pemrograman/php/$project_name/{css,js,images,includes}

# Create index.php
cat > ~/pemrograman/php/$project_name/index.php << 'EOF'
<?php
require_once 'config.php';
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>New Project</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <h1>🚀 Project <?php echo basename(__DIR__); ?></h1>
    <?php
    $conn = getConnection();
    if ($conn) {
        echo "<p style='color: green'>✅ Database connected!</p>";
    }
    ?>
    <script src="js/script.js"></script>
</body>
</html>
EOF

# Create config.php
cat > ~/pemrograman/php/$project_name/config.php << 'EOF'
<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASS', 'root123');
define('DB_NAME', 'PROJECT_NAME');

function getConnection() {
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
    if ($conn->connect_error) {
        return null;
    }
    $conn->set_charset("utf8mb4");
    return $conn;
}
EOF

sed -i "s/PROJECT_NAME/$project_name/g" ~/pemrograman/php/$project_name/config.php

# Create CSS
cat > ~/pemrograman/php/$project_name/css/style.css << 'EOF'
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    padding: 20px;
    background: #f4f4f4;
}
.container {
    max-width: 1200px;
    margin: 0 auto;
    background: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}
EOF

# Create database
mysql -u root -proot123 -e "CREATE DATABASE IF NOT EXISTS $project_name;"

# Set permission
chmod 755 ~/pemrograman/php/$project_name
chmod 644 ~/pemrograman/php/$project_name/*.php

echo "✅ Project $project_name created!"
echo "📍 Location: ~/pemrograman/php/$project_name/"
echo "🌐 URL: http://localhost/php/$project_name/"
echo "🗄️ Database: $project_name"
```
### Cara pakai:
```bash
chmod +x create-php-project.sh
./create-php-project.sh
```
---
## 🎯 KESIMPULAN AKHIR
### ✅ Checklist Developer LAMP:
```text
☐ Apache running → http://localhost/
☐ MySQL running → mysql -u root -p
☐ PHP running → php -v
☐ phpMyAdmin → http://localhost/phpmyadmin/
☐ Project folder → ~/pemrograman/php/
☐ Alias /php/ → http://localhost/php/project/
☐ Database bisa connect
☐ Error log bisa diakses
☐ Permission benar
☐ Firewall configured
☐ Backup routine set
```
### 📌 Prinsip Penting:
- Selalu cek error log - 90% masalah ketahuan dari sini
- Permission is key - Apache harus bisa baca folder
- Password MySQL - Harus konsisten (root123)
- Folder project - Simpan di home, bukan di /var/www/
- Start/Stop service - Systemctl is your friend
- Backup - Lakukan rutin

### 💡 Tips Terakhir:
```bash
# Alias super untuk daily use
echo 'alias sys="sudo systemctl"' >> ~/.bashrc
echo 'alias apa="sudo systemctl status apache2"' >> ~/.bashrc
echo 'alias my="sudo systemctl status mysql"' >> ~/.bashrc
echo 'alias log="sudo tail -f /var/log/apache2/error.log"' >> ~/.bashrc
source ~/.bashrc

# Sekarang tinggal ketik:
sys start apache2
sys status apache2
apa
my
log
```
# Happy Coding! 🐧🚀✨  
# "Service management itu seperti lampu kamar - matian kalau tidak dipakai, nyalakan kalau butuh. Simple!"

