# 📘 MATERI LENGKAP LAMP STACK UNTUK PEMULA
> Linux, Apache, MySQL, PHP - Dari Nol Sampai Siap Pakai
---
## APA ITU LAMP?
### LAMP adalah singkatan dari:

    Linux - Sistem Operasi

    Apache - Web Server

    MySQL/MariaDB - Database

    PHP - Bahasa Pemrograman

### Perbedaan LAMP vs XAMPP:
| Aspek                    | LAMP (Linux Native)     | XAMPP (Windows)        |
|--------------------------|--------------------------|------------------------|
| Struktur Komponen        | Komponen terpisah        | Satu paket all-in-one  |
| Cara Kontrol             | Kontrol via terminal     | Kontrol via GUI        |
| Integrasi Sistem         | Terintegrasi sistem      | Aplikasi mandiri       |
| Ukuran / Resource        | Ringan (±500MB)          | Berat (±1–2GB)         |
| Lokasi File              | File tersebar di sistem  | File di 1 folder       |
---
##🏗️ INSTALASI LAMP
### 1 Update System
```bash
sudo apt update
sudo apt upgrade -y
```
### 2 Install Apache
```bash
# Instal apache2
sudo apt install apache2 -y

# Cek Apache:
sudo systemctl status apache2

#Masuk Browser: http://localhost → Harus muncul Apache2 Default Page
```

### 3 Install MySQL/MariaDB
``` bash
sudo apt install mariadb-server mariadb-client -y
# atau
sudo apt install mysql-server mysql-client -y

# Amankan MySQL:
sudo mysql_secure_installation

# Konfigurasi:

Switch to unix_socket authentication? n
Change root password? y
New password: root123
Remove anonymous users? y
Disallow root login remotely? y
Remove test database? y
Reload privilege tables? y
```
### 4 Install PHP
```bash
# PHP dasar + ekstensi umum
sudo apt install php libapache2-mod-php php-mysql -y
sudo apt install php-curl php-gd php-mbstring php-xml php-zip php-intl -y

sudo systemctl restart apache2

# Cek PHP:
echo "<?php phpinfo(); ?>" | sudo tee /var/www/html/info.php

masuk Browser: http://localhost/info.php
```
---
## 📁 STRUKTUR DIREKTORI LAMP
### 1 Lokasi File Penting Apache
| Path                          | Fungsi                                   |
|--------------------------------|------------------------------------------|
| /etc/apache2/                 | Direktori utama konfigurasi Apache       |
| /etc/apache2/apache2.conf     | File konfigurasi utama                   |
| /etc/apache2/sites-available/ | Konfigurasi virtual host (tersedia)      |
| /etc/apache2/sites-enabled/   | Konfigurasi virtual host (aktif)         |
| /etc/apache2/conf-available/  | Konfigurasi tambahan (tersedia)          |
| /etc/apache2/conf-enabled/    | Konfigurasi tambahan (aktif)             |
| /etc/apache2/mods-available/  | Modul Apache (tersedia)                  |
| /etc/apache2/mods-enabled/    | Modul Apache (aktif)                     |
| /var/www/html/                | Default document root (tidak disarankan untuk development) |
| /var/log/apache2/error.log    | Log error Apache                         |
| /var/log/apache2/access.log   | Log akses Apache                         |

### 2 Lokasi File Penting MySQL
| Path                     | Fungsi                                  |
|--------------------------|------------------------------------------|
| /etc/mysql/              | Direktori utama konfigurasi MySQL       |
| /etc/mysql/my.cnf        | File konfigurasi utama                  |
| /var/lib/mysql/          | **Lokasi penyimpanan database utama** 🔴 |
| /var/log/mysql/error.log | Log error MySQL                         |

📌 CATATAN PENTING:
Semua database yang dibuat akan disimpan di: /var/lib/mysql/
```bash
# Lihat ukuran semua database
sudo du -sh /var/lib/mysql/*

# Lihat folder database tertentu
sudo ls -la /var/lib/mysql/nama_database/
```

### 3 Lokasi File Penting PHP
| Path                              | Fungsi                                   |
|------------------------------------|------------------------------------------|
| /etc/php/                         | Direktori utama konfigurasi PHP          |
| /etc/php/8.x/apache2/php.ini      | Konfigurasi PHP untuk Apache             |
| /etc/php/8.x/cli/php.ini          | Konfigurasi PHP untuk terminal (CLI)     |
| /var/lib/php/                     | Penyimpanan file session PHP             |
---
## 🎨 KONFIGURASI PROJECT STRUCTURE
### 1 Struktur Folder Ideal untuk Development
```bash 
/home/username/
├── pemrograman/
│   ├── php/
│   │   ├── project1/
│   │   │   ├── index.php
│   │   │   ├── config.php
│   │   │   ├── auth/
│   │   │   └── css/
│   │   ├── project2/
│   │   ├── project3/
│   │   └── db_config.php (konfigurasi terpusat)
│   ├── python/
│   └── javascript/
```
### 2 Setup Alias Apache untuk Project
```bash
1. Buat konfigurasi:

sudo nano /etc/apache2/conf-available/clean-urls.conf

2. Isi:
# ============================================
# KONFIGURASI CLEAN URLS + PHPMYADMIN
# ============================================

# 1️⃣ PHPMYADMIN 
Alias /phpmyadmin /usr/share/phpmyadmin

<Directory /usr/share/phpmyadmin>
    Options Indexes FollowSymLinks
    DirectoryIndex index.php
    Require all granted
    <IfModule mod_authz_core.c>
        Require all granted
    </IfModule>
</Directory>

# 2️⃣ IZINKAN AKSES KE FOLDER PROJECT
<Directory /home/all/pemrograman/php>
    Options Indexes FollowSymLinks
    AllowOverride All
    Require all granted
</Directory>

# 3️⃣ FILE STATIS (CSS, JS, GAMBAR)
AliasMatch ^/(.+\.(css|js|jpg|jpeg|png|gif|ico|svg|woff|ttf|pdf|txt))$ /home/all/pemrograman/php/$1

# 4️⃣ PROJECT ROUTES - Pastikan ini TIDAK menimpa phpmyadmin
AliasMatch ^/([^/.]+)(/.*)?$ /home/all/pemrograman/php/$1$2

# 5️⃣ ERROR DOCUMENTS
ErrorDocument 404 /404.html
ErrorDocument 403 /403.html

3. Aktifkan:

sudo a2enconf php-projects.conf
sudo systemctl reload apache2

4. Akses project: http://localhost/nama_project/
```
### 3 Permission yang Benar
```bash
# Permission folder
chmod 755 /home/[username]
chmod 755 /home/[username]/pemrograman
chmod 755 /home/[username]/pemrograman/php
chmod 755 /home/[username]/pemrograman/php/*
chmod 644 /home/[username]/pemrograman/php/*/*.php

# Group permission (biar Apache bisa baca/tulis)
sudo usermod -a -G [username] www-data
sudo chown -R [username]:www-data /home/[username]/pemrograman/php
chmod -R 775 /home/[username]/pemrograman/php
```
---
## 🐬 MANAJEMEN DATABASE
### 1 Perintah Dasar MySQL
```bash

# Login ke MySQL
mysql -u root -p

# Buat database
CREATE DATABASE nama_database;

# Lihat semua database
SHOW DATABASES;

# Pilih database
USE nama_database;

# Lihat semua tabel
SHOW TABLES;

# Buat tabel
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100)
);

# Hapus database
DROP DATABASE nama_database;

# Keluar
EXIT;
```
### 2 Lokasi Fisik Database
Semua database tersimpan di:
```bash
cd /var/lib/mysql/
ls -la
```
Struktur:
```
/var/lib/mysql/
├── apotek/              # Folder untuk database apotek
│   ├── users.ibd       # File data tabel users
│   ├── products.ibd    # File data tabel products
│   └── db.opt          # Konfigurasi database
├── taskflow/           # Folder untuk database taskflow
├── mysql/              # Database sistem
└── performance_schema/ # Database performance
```
### 3 Backup dan Restore Database
```bash

# Backup database ke file SQL
mysqldump -u root -p nama_database > ~/backup_nama_database.sql

# Restore database dari file SQL
mysql -u root -p nama_database < ~/backup_nama_database.sql

# Backup semua database
mysqldump -u root -p --all-databases > ~/backup_all.sql
```
---
## 🔧 KONFIGURASI FILE PHP
### 1 File Konfigurasi Database Terpusat

Buat file: /home/[username]/pemrograman/php/db_config.php
```php
<?php
/**
 * Konfigurasi Database Terpusat
 * Include file ini di semua project
 */

define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASS', 'root123');

/**
 * Fungsi koneksi database
 * @param string $db_name Nama database
 * @return object MySQLi connection
 */
function getConnection($db_name = '') {
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, $db_name);
    
    if ($conn->connect_error) {
        die("Koneksi gagal: " . $conn->connect_error);
    }
    
    $conn->set_charset("utf8mb4");
    return $conn;
}

/**
 * Fungsi untuk cek database
 * @param string $db_name Nama database
 * @return bool
 */
function checkDatabase($db_name) {
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASS);
    $result = $conn->select_db($db_name);
    $conn->close();
    return $result;
}
?>
```
### 2 Contoh Config.php per Project
```php
<?php
// /home/username/pemrograman/php/apotek/config.php
require_once '/home/username/pemrograman/php/db_config.php';

// Koneksi ke database apotek
$conn = getConnection('apotek');

// Atau cek dulu
if (!checkDatabase('apotek')) {
    die("Database apotek belum dibuat. Jalankan: CREATE DATABASE apotek;");
}
?>
```
### 3 Test Koneksi Database
```php
<?php
// test_db.php
error_reporting(E_ALL);
ini_set('display_errors', 1);

echo "<h2>🔍 Test Koneksi Database</h2>";

// 1. Test koneksi MySQL
$conn = new mysqli('localhost', 'root', 'root123');
if ($conn->connect_error) {
    die("❌ MySQL: " . $conn->connect_error);
}
echo "✅ MySQL: Berhasil konek<br>";

// 2. Cek database
$db_name = 'apotek';
if ($conn->select_db($db_name)) {
    echo "✅ Database '$db_name': ADA<br>";
    
    // 3. Cek tabel
    $tables = $conn->query("SHOW TABLES");
    echo "📋 Jumlah tabel: " . $tables->num_rows . "<br>";
} else {
    echo "❌ Database '$db_name': TIDAK ADA<br>";
    echo "🔧 Buat: CREATE DATABASE $db_name;<br>";
}

$conn->close();
?>
```
---
## 🛠️ COMMAND DAN ALIAS PENTING
### 1 Service Management
```bash
# Start/Stop/Restart Apache
sudo systemctl start apache2
sudo systemctl stop apache2
sudo systemctl restart apache2
sudo systemctl reload apache2
sudo systemctl status apache2

# Start/Stop/Restart MySQL
sudo systemctl start mysql
sudo systemctl stop mysql
sudo systemctl restart mysql
sudo systemctl status mysql

# Enable auto-start saat boot
sudo systemctl enable apache2
sudo systemctl enable mysql
```
### 2 Setup Alias di Terminal
```bash
nano ~/.bash_aliases
```
Isi:
```bash
# Web Server
alias startweb='sudo systemctl start apache2 && sudo systemctl start mysql'
alias stopweb='sudo systemctl stop apache2 && sudo systemctl stop mysql'
alias restartweb='sudo systemctl restart apache2 && sudo systemctl restart mysql'
alias statusweb='sudo systemctl status apache2 && sudo systemctl status mysql'

# Project
alias gotophp='cd ~/pemrograman/php'
alias listprojects='ls -la ~/pemrograman/php/'

# Database
alias mysql-login='mysql -u root -p'
alias mysql-backup='mysqldump -u root -p'

# Logs
alias apache-log='sudo tail -f /var/log/apache2/error.log'
alias mysql-log='sudo tail -f /var/log/mysql/error.log'

# Edit Config
alias edit-apache='sudo nano /etc/apache2/apache2.conf'
alias edit-php='sudo nano /etc/php/8.2/apache2/php.ini'
```
Aktifkan:
```bash
source ~/.bashrc
```
---
## 📊 TROUBLESHOOTING
### 1 Error 403 Forbidden
``` bash
# Fix permission
chmod 755 /home/[username]
chmod 755 /home/[username]/pemrograman
chmod 755 /home/[username]/pemrograman/php
sudo systemctl reload apache2
```
### 2 Error 500 Internal Server Error
```bash
# 1. Cek error log
sudo tail -30 /var/log/apache2/error.log

# 2. Aktifkan error reporting di PHP
nano ~/pemrograman/php/project/index.php
error_reporting(E_ALL);
ini_set('display_errors', 1);

# 3. Cek password MySQL di config.php
```
### 3 MySQL "Access Denied"
```bash
# Reset password
sudo mysql
ALTER USER 'root'@'localhost' IDENTIFIED BY 'root123';
FLUSH PRIVILEGES;
EXIT;
```
### 4 Port 80 already in use
```bash

# Cek aplikasi yang pakai port 80
sudo lsof -i :80

# Stop aplikasi lain
sudo systemctl stop nginx

# Restart Apache
sudo systemctl restart apache2
```
---
## 🚀 INSTALASI TOOLS TAMBAHAN
### 1 phpMyAdmin
```bash

sudo apt install phpmyadmin -y
sudo ln -s /usr/share/phpmyadmin /var/www/html/phpmyadmin
sudo systemctl restart apache2

Akses: http://localhost/phpmyadmin
```
### 2 Composer (PHP Dependency Manager)
```bash
sudo apt install composer -y
composer --version
```
### 3 Git (Version Control)
```bash
sudo apt install git -y
git --version
```
### 4 VS Code (Code Editor)
```bash
sudo snap install code --classic
```
---
## 📝 CHEAT SHEET CEPAT
### 1. 30 Detik Setup Project Baru
```bash
# 1. Buat folder
mkdir ~/pemrograman/php/project-baru
chmod 755 ~/pemrograman/php/project-baru

# 2. Buat file index.php
echo "<?php phpinfo(); ?>" > ~/pemrograman/php/project-baru/index.php

# 3. Buat database
mysql -u root -p -e "CREATE DATABASE project_baru;"

# 4. Buka browser
# http://localhost/php/project-baru/
```
### 2 Checklist Harian Developer
```bash
# Pagi hari - Start server
startweb
gotophp

# Sore hari - Stop server
stopweb
```
### 3 Path Penting yang Harus Dihafal
```
📁 Konfigurasi Apache    → /etc/apache2/
📁 Konfigurasi MySQL     → /etc/mysql/
📁 Konfigurasi PHP       → /etc/php/
📁 Log Apache            → /var/log/apache2/error.log
📁 Log MySQL            → /var/log/mysql/error.log
📁 Lokasi Database      → /var/lib/mysql/
📁 Default Web Root     → /var/www/html/
📁 Project Pribadi      → ~/pemrograman/php/
📁 phpMyAdmin           → /usr/share/phpmyadmin/
```
---
## 🎯 KESIMPULAN
### Keunggulan LAMP dibanding XAMPP:
    ✅ Lebih Ringan - Hanya 500MB vs XAMPP 2GB

    ✅ Lebih Cepat - Native di Linux

    ✅ Terintegrasi - Update via system package manager

    ✅ Production Ready - Bisa langsung deploy

    ✅ Learning Curve - Memahami cara kerja web server

    ✅ Folder Rapi - Project di home, bukan campur aduk

### Alur Kerja Ideal:
    Start server → startweb

    Buka project → gotophp lalu code .

    Akses browser → http://localhost/php/nama_project/

    Manage DB → http://localhost/phpmyadmin/

    Stop server → stopweb

### Cheat Sheet:
```bash
# Backup semua database
mysqldump -u root -p --all-databases > ~/backup-$(date +%Y%m%d).sql

# Restore Apache config default
sudo cp /etc/apache2/apache2.conf.backup /etc/apache2/apache2.conf

# Cek versi semua komponen
apache2 -v
mysql --version
php -v
```

## 🎉 SELAMAT BELAJAR!
### Ingat:

    Practice makes perfect - Semakin sering install, semakin paham

    Jangan takut error - Error adalah guru terbaik

    Google is your friend - Semua problem pasti sudah ada solusinya

# Happy Coding! 🚀🐧✨
