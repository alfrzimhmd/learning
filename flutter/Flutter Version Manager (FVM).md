# Flutter Version Management (FVM)

> Panduan lengkap mengenai penggunaan Flutter Version Management (FVM) dalam pengembangan aplikasi Flutter.

Materi ini membahas berbagai aspek penting mulai dari pengertian dasar FVM, proses instalasi, cara membuat project Flutter menggunakan FVM, hingga manajemen project dan troubleshooting error yang sering terjadi. Dokumentasi ini disusun sebagai catatan pembelajaran sekaligus referensi penggunaan FVM dalam pengembangan project Flutter.   

---
## Daftar Isi

1. [Pengertian FVM](#1-pengertian-fvm)
2. [Fungsi FVM](#2-fungsi-fvm)
3. [Cara Kerja FVM](#3-cara-kerja-fvm)
4. [Instalasi FVM](#4-instalasi-fvm)
5. [Membuat Project Flutter Menggunakan FVM](#5-membuat-project-flutter-menggunakan-fvm)
6. [Bagaimana Jika Suatu Project Menggunakan FVM Tapi Developer Lain Tidak Menggunakan FVM](#6-bagaimana-jika-suatu-project-menggunakan-fvm-tapi-developer-lain-tidak-menggunakan-fvm)
7. [Bagaimana Jika Pengguna FVM Menjalankan Project Yang Tidak Menggunakan FVM](#7-bagaimana-jika-pengguna-fvm-menjalankan-project-yang-tidak-menggunakan-fvm)
8. [Kelebihan & Kekurangan FVM](#8-kelebihan--kekurangan-fvm)
9. [Manajemen Project Flutter Menggunakan FVM](#9-manajemen-project-flutter-menggunakan-fvm)
10. [Kumpulan Perintah FVM](#10-kumpulan-perintah-fvm)
11. [Troubleshooting Error FVM](#11-troubleshooting-error-fvm)
12. [Kesimpulan](#12-kesimpulan)
---
## 1. Pengertian FVM

Flutter Version Management (FVM) adalah alat yang digunakan untuk mengelola berbagai versi Flutter SDK dalam satu komputer. Dalam pengembangan aplikasi Flutter, sering terjadi kondisi di mana satu project dibuat menggunakan versi Flutter tertentu, sementara project lain menggunakan versi yang berbeda. Jika hanya menggunakan satu instalasi Flutter secara global, perubahan versi Flutter dapat menyebabkan masalah seperti kegagalan build, konflik dependency, atau perubahan perilaku framework.

FVM hadir untuk mengatasi masalah tersebut dengan memungkinkan setiap project menggunakan versi Flutter yang berbeda tanpa saling mengganggu. Dengan kata lain, setiap project dapat "dikunci" pada versi Flutter tertentu sehingga lingkungan pengembangan tetap konsisten.

Konsep ini mirip dengan version manager pada bahasa pemrograman lain, seperti:

* **NVM (Node Version Manager)** pada Node.js
* **Pyenv** pada Python

Dengan menggunakan FVM, setiap project Flutter memiliki konfigurasi versi Flutter sendiri. Hal ini membuat project tetap stabil walaupun terdapat banyak project lain dengan versi Flutter yang berbeda dalam satu komputer.

---

## 2. Fungsi FVM

FVM memiliki beberapa fungsi penting dalam proses pengembangan aplikasi Flutter, terutama ketika bekerja dengan banyak project atau dalam tim.

### 1) Mengelola Banyak Versi Flutter

FVM memungkinkan satu komputer memiliki beberapa versi Flutter sekaligus. Setiap versi disimpan secara terpisah sehingga tidak saling menimpa.

Contoh versi Flutter yang dapat terinstal bersamaan:
* Flutter 3.19.0
* Flutter 3.22.0
* Flutter 3.41.4
* Stable
  
Setiap project dapat menggunakan versi yang berbeda sesuai kebutuhan.
Tanpa FVM, developer harus mengganti versi Flutter secara manual, yang berisiko merusak project lain.

### 2) Menjaga Stabilitas Project
Ketika Flutter diperbarui, terkadang terdapat perubahan pada framework yang menyebabkan project lama mengalami error.  
Dengan menggunakan FVM, sebuah project dapat dikunci pada versi Flutter tertentu sehingga tidak terpengaruh oleh update Flutter global.  
Contoh:
- Project A menggunakan Flutter 3.22.0
- Project B menggunakan Flutter 3.41.4
  
Dengan FVM, kedua project tetap dapat berjalan secara stabil tanpa konflik.

### 3) Mempermudah Kolaborasi Tim

Dalam pengembangan tim, sering terjadi perbedaan versi Flutter antar developer. Hal ini dapat menyebabkan masalah seperti:

* error build
* dependency conflict
* perbedaan hasil build

FVM menyimpan konfigurasi versi Flutter dalam project sehingga seluruh anggota tim dapat menggunakan versi yang sama.

Dengan demikian, lingkungan pengembangan menjadi konsisten di seluruh anggota tim.

### 4) Menghindari Konflik Antar Project

Jika Flutter diperbarui secara global, project lama terkadang tidak dapat dijalankan lagi.

Dengan FVM, setiap project memiliki lingkungan Flutter sendiri sehingga perubahan versi Flutter tidak akan mempengaruhi project lain.

---

### 3. Cara Kerja FVM

FVM bekerja dengan cara mengunduh berbagai versi Flutter SDK dan menyimpannya dalam direktori cache khusus. Setiap project kemudian dapat menunjuk ke versi Flutter tertentu melalui file konfigurasi.

Proses kerja FVM secara umum:

1. FVM mengunduh Flutter SDK dengan versi tertentu.
2. Flutter SDK disimpan pada direktori cache FVM.
3. Project menentukan versi Flutter yang digunakan.
4. FVM mengarahkan perintah Flutter pada project tersebut ke versi yang telah ditentukan.

### Lokasi FVM

Linux / macOS:

```
~/.fvm/versions/
```

Windows:

```
C:\Users\USERNAME\fvm\versions\
```

Contoh struktur folder:

```
.fvm

versions
 ├── 3.41.4
 ├── 3.22.0
 └── stable
```

Ketika sebuah project menggunakan FVM, maka akan muncul konfigurasi tambahan pada project tersebut.

Contoh struktur project:

```
project_flutter/

.fvm/
.fvmrc
lib/
android/
ios/
```

File `.fvmrc` berisi informasi versi Flutter yang digunakan oleh project.

Contoh isi file:

```
{
  "flutter": "3.41.4"
}
```

Ketika perintah Flutter dijalankan melalui FVM, maka FVM akan memastikan bahwa Flutter SDK yang digunakan sesuai dengan konfigurasi tersebut.

---

## 4. Instalasi FVM

Berikut langkah instalasi FVM dari awal hingga siap digunakan.

### 1) Memastikan Dart SDK Terinstal

FVM dibuat menggunakan bahasa Dart sehingga Dart SDK harus tersedia.

Cek instalasi Dart:

```
dart --version
```

Jika Dart belum terinstal, instal terlebih dahulu melalui situs resmi Dart.

### 2) Instalasi FVM

FVM dapat diinstal menggunakan perintah berikut:

```
dart pub global activate fvm
```
Perintah ini akan menginstal FVM secara global pada sistem.

### 3) Menambahkan PATH

Agar perintah `fvm` dapat digunakan di terminal, direktori berikut harus dimasukkan ke PATH.

Linux / macOS:

```
$HOME/.pub-cache/bin
```

Tambahkan pada `.bashrc` atau `.zshrc`:

```
export PATH="$PATH:$HOME/.pub-cache/bin"
```

Kemudian jalankan:

```
source ~/.bashrc
```

Windows:

Tambahkan path berikut pada Environment Variable:

```
C:\Users\USERNAME\AppData\Local\Pub\Cache\bin
```

Setelah itu restart terminal atau command prompt.

### 4) Mengecek Instalasi FVM

Beberapa perintah untuk memastikan FVM telah terinstal dengan benar:

```
fvm --version
```

```
fvm list
```

```
fvm doctor
```

Jika tidak ada error maka FVM telah siap digunakan.

---

## 5. Membuat Project Flutter Menggunakan FVM

Langkah membuat project Flutter menggunakan FVM.

### 1) Membuat Project

```
fvm flutter create \
--org com.example \
--platforms=android,ios \
nama_project
```

Penjelasan parameter:

`--org`

Menentukan organization atau package name aplikasi.

Contoh:

```
com.example.aplikasi
```

`--platforms`

Menentukan platform yang akan dibuat.

Contoh jika hanya ingin membuat aplikasi mobile:

```
android,ios
```

Contoh pembuatan project:

```
fvm flutter create \
--org com.tekekid \
--platforms=android,ios \
project_flutter
```

### 2) Masuk ke Folder Project

```
cd project_flutter
```

### 3) Menentukan Versi Flutter
```
fvm use 3.41.4
```
Perintah ini akan:

* mengunduh Flutter jika belum tersedia
* membuat file `.fvmrc`
* menghubungkan project dengan versi Flutter tersebut

### 4) Mengambil Dependency
```
fvm flutter pub get
```
Perintah ini digunakan untuk mengunduh seluruh dependency yang terdapat pada file `pubspec.yaml`.

### 5) Menjalankan Project

```
fvm flutter run
```

Perintah ini akan menjalankan aplikasi menggunakan Flutter yang dikelola oleh FVM.

### Apakah harus selalu menggunakan `fvm`?

Disarankan untuk menjalankan semua perintah Flutter melalui FVM.

Contoh:

```
fvm flutter run
```

```
fvm flutter build apk
```

```
fvm flutter doctor
```

Jika menggunakan perintah biasa seperti:

```
flutter run
```

maka Flutter global yang akan digunakan. Jika versi Flutter global berbeda dengan versi yang digunakan project, maka dapat menyebabkan error.

---

## 6. Bagaimana jika suatu project menggunakan FVM tapi developer lain tidak menggunakan FVM?

Project yang menggunakan FVM tetap dapat dijalankan tanpa FVM.

Developer hanya perlu menggunakan versi Flutter yang sama dengan versi yang ditentukan pada file `.fvmrc`.

Contoh isi file `.fvmrc`:

```
{
 "flutter": "3.41.4"
}
```

Developer lain dapat menginstal Flutter versi tersebut secara manual.

Namun jika menggunakan versi Flutter yang berbeda, kemungkinan dapat terjadi:

* error build
* dependency conflict
* perubahan perilaku framework

Oleh karena itu penggunaan FVM oleh seluruh anggota tim tetap lebih disarankan.

---

## 7. Bagaimana jika pengguna FVM menjalankan project yang tidak menggunakan FVM?

Jika seorang developer menggunakan FVM tetapi project tidak memiliki konfigurasi FVM, maka project tersebut tetap dapat dijalankan seperti project Flutter biasa.

Ada dua cara menjalankannya.

### 1) Menjalankan Tanpa FVM

```
flutter run
```

Cara ini menggunakan Flutter global yang terinstal pada sistem.

### 2) Menambahkan FVM ke Project

Jika ingin project tersebut dikelola oleh FVM, jalankan:

```
fvm use stable
```

atau

```
fvm use 3.41.4
```

Perintah tersebut akan membuat konfigurasi `.fvmrc`.

---

## 8. Kelebihan & Kekurangan FVM

### 1) Kelebihan

1. Mendukung banyak versi Flutter dalam satu komputer
2. Setiap project dapat menggunakan versi Flutter yang berbeda
3. Mempermudah kolaborasi dalam tim
4. Mengurangi risiko kerusakan project akibat upgrade Flutter
5. Mempermudah proses berpindah versi Flutter

### 2) Kekurangan

1. Membutuhkan ruang penyimpanan lebih besar
2. Developer harus terbiasa menggunakan perintah FVM
3. Jika tidak disiplin menggunakan FVM, developer bisa menjalankan Flutter global tanpa sadar

---

## 9. Manajemen Project Flutter Menggunakan FVM

Beberapa praktik yang disarankan.

### 1) Gunakan Versi Flutter Spesifik

Disarankan menggunakan versi tetap.

```
fvm use 3.41.4
```

### 2) Simpan File Konfigurasi FVM

File berikut harus disimpan di repository.

```
.fvmrc
```

### 3) Gunakan .gitignore

Folder berikut tidak perlu dimasukkan ke repository.

```
.fvm/flutter_sdk
```

### 4) Gunakan Perintah Flutter Melalui FVM

Biasakan menjalankan Flutter melalui FVM.

```
fvm flutter run
```

```
fvm flutter build
```

```
fvm flutter doctor
```

---

## 10. Kumpulan Perintah FVM

| Perintah            | Fungsi                     |
| ------------------- | -------------------------- |
| `fvm install VERSION` | menginstal Flutter         |
| `fvm use VERSION`     | menggunakan versi Flutter  |
| `fvm use stable`      | menggunakan channel stable |
| `fvm list`            | melihat versi Flutter      |
| `fvm remove VERSION`  | menghapus versi Flutter    |
| `fvm global VERSION`  | mengatur Flutter global    |
| `fvm doctor`          | mengecek konfigurasi       |
| `fvm cache clear`     | membersihkan cache         |
| `fvm flutter run`     | menjalankan aplikasi       |
| `fvm flutter build`   | build aplikasi             |
| `fvm flutter doctor`  | mengecek Flutter           |
| `fvm flutter pub get` | mengambil dependency       |

---

## 11. Troubleshooting Error FVM

Beberapa masalah yang sering terjadi ketika menggunakan FVM.

### 1) Flutter command tidak ditemukan

Penyebab biasanya PATH belum ditambahkan.

Solusi:

Pastikan direktori berikut sudah masuk PATH.

Linux:

```
$HOME/.pub-cache/bin
```

Windows:

```
C:\Users\USERNAME\AppData\Local\Pub\Cache\bin
```

### 2) Versi Flutter tidak sesuai

Hal ini terjadi ketika menjalankan perintah:

```
flutter run
```

Solusi:

Gunakan perintah:

```
fvm flutter run
```

### 3) Flutter SDK belum terinstal

Jika menjalankan:

```
fvm use stable
```

lalu muncul pesan Flutter belum terinstal.

Solusi:

```
fvm install stable
```

### 4) Error dependency setelah ganti versi Flutter

Solusi:

```
fvm flutter clean
```

```
fvm flutter pub get
```

---

## 12. Kesimpulan

Flutter Version Management (FVM) merupakan alat yang sangat penting dalam pengembangan aplikasi Flutter modern. Dengan menggunakan FVM, setiap project dapat memiliki versi Flutter yang spesifik sehingga stabilitas project tetap terjaga.

FVM sangat membantu ketika mengelola banyak project sekaligus maupun ketika bekerja dalam tim. Dengan manajemen versi yang baik, konflik dependency dan masalah kompatibilitas Flutter dapat diminimalkan sehingga proses pengembangan menjadi lebih stabil dan terstruktur.
