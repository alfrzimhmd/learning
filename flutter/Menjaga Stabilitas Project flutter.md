# Menjaga Stabilitas Project Flutter (Lintas OS & Tim Development)

Dalam pengembangan aplikasi Flutter, sering terjadi masalah ketika project dijalankan di **sistem operasi berbeda** (Linux, Windows, macOS) atau oleh **anggota tim yang memiliki konfigurasi environment berbeda**.

Contoh masalah yang sering muncul:

* Perbedaan versi Flutter
* Dependency plugin berubah
* Versi Gradle tidak cocok
* Versi Kotlin tidak kompatibel
* Perbedaan NDK atau Android SDK
* Perbedaan line ending antara Windows dan Linux

Masalah-masalah tersebut dapat menyebabkan:

* Build gagal
* Error dependency
* Perilaku aplikasi berbeda
* Hasil build APK/AAB tidak konsisten

Untuk menghindari hal tersebut, developer perlu membuat **environment yang dapat direproduksi (Reproducible Build Environment)**.
Artinya: project dapat dijalankan di komputer manapun dengan **hasil yang sama dan stabil**.

Berikut adalah beberapa komponen penting yang sebaiknya **dikunci versinya (version locking)**.

---

# 1. Mengunci Versi Flutter SDK

Versi Flutter sangat berpengaruh terhadap kompatibilitas plugin, sistem build, dan SDK Android.

Cara terbaik untuk mengelola versi Flutter adalah menggunakan **Flutter Version Manager (FVM)**.

FVM memungkinkan setiap project menggunakan **versi Flutter yang berbeda tanpa konflik**.

Contoh penggunaan:

```
fvm install 3.19.6
fvm use 3.19.6
```

Ketika perintah tersebut dijalankan, akan dibuat konfigurasi berikut di dalam project:

```
.fvm/
   ├── flutter_sdk
   └── fvm_config.json
```

Isi file `fvm_config.json`:

```json
{
  "flutterSdkVersion": "3.19.6"
}
```

Jika developer lain menggunakan FVM, mereka cukup menjalankan:

```
fvm install
```

Maka FVM akan otomatis menginstall versi Flutter yang sesuai dengan project.

Keuntungan:

* Setiap project menggunakan Flutter yang konsisten
* Menghindari konflik ketika upgrade Flutter
* Mendukung pengembangan lintas OS

---

# 2. Mengunci Dependency Dart / Flutter

Semua dependency yang digunakan dalam project Flutter didefinisikan di file:

```
pubspec.yaml
```

Contoh:

```
dependencies:
  http: ^1.2.0
```

Namun versi yang benar-benar digunakan disimpan di file:

```
pubspec.lock
```

File ini **sangat penting** karena berisi versi dependency yang tepat.

Ketika developer lain menjalankan:

```
flutter pub get
```

Flutter akan menginstall dependency sesuai dengan `pubspec.lock`.

Karena itu **file ini harus selalu di-commit ke repository**.

Keuntungan:

* Dependency plugin selalu konsisten
* Menghindari perubahan versi plugin secara otomatis

---

# 3. Mengunci Versi Gradle

Gradle digunakan sebagai sistem build Android.

Versi Gradle dikunci pada file berikut:

```
android/gradle/wrapper/gradle-wrapper.properties
```

Contoh isi:

```
distributionUrl=https://services.gradle.org/distributions/gradle-8.3-all.zip
```

Ketika project dijalankan di komputer lain, Gradle akan **mengunduh versi yang sama secara otomatis**.

Keuntungan:

* Build Android menjadi konsisten
* Menghindari error akibat perbedaan Gradle

---

# 4. Mengunci Android Gradle Plugin

Android Gradle Plugin menentukan cara project Android dibangun.

Lokasinya di:

```
android/build.gradle
```

Contoh konfigurasi:

```
classpath 'com.android.tools.build:gradle:8.2.2'
```

Versi ini harus dikunci agar kompatibel dengan:

* Gradle
* Android SDK
* Kotlin

Jika tidak dikunci, build dapat gagal karena konflik versi.

---

# 5. Mengunci Versi Kotlin

Kotlin digunakan dalam bagian native Android.

Versinya biasanya ditentukan di:

```
android/build.gradle
```

Contoh:

```
ext.kotlin_version = '1.9.22'
```

Jika versi Kotlin berbeda antara developer, bisa muncul error seperti:

```
Kotlin version mismatch
```

Dengan mengunci versi Kotlin, project akan lebih stabil.

---

# 6. Mengunci Android SDK Version

Versi Android SDK yang digunakan untuk compile aplikasi ditentukan di:

```
android/app/build.gradle
```

Contoh:

```
compileSdkVersion 34
minSdkVersion 21
targetSdkVersion 34
```

Penjelasan:

* compileSdkVersion → SDK yang digunakan untuk compile
* minSdkVersion → minimal Android yang didukung
* targetSdkVersion → target Android yang dioptimalkan

Jika SDK belum tersedia di komputer developer lain, Android Studio biasanya akan meminta untuk menginstallnya.

---

# 7. Mengunci Versi Android NDK

NDK diperlukan jika project menggunakan plugin native atau library C/C++.

Versi NDK dapat dikunci di:

```
android/app/build.gradle
```

Contoh:

```
ndkVersion "26.1.10909125"
```

Jika NDK tersebut belum ada di komputer developer lain, Android Studio biasanya akan menginstallnya secara otomatis.

Ini penting untuk menghindari error build pada plugin native.

---

# 8. Mengunci Versi CMake

Beberapa plugin Flutter menggunakan CMake untuk build native code.

Versi CMake dapat ditentukan pada konfigurasi Android project.

Contoh:

```
cmakeVersion "3.22.1"
```

Dengan mengunci versi ini, build native akan lebih konsisten di semua sistem operasi.

---

# 9. Menjaga Konsistensi Code Style

Untuk menjaga konsistensi kode antar developer, Flutter menggunakan file:

```
analysis_options.yaml
```

Contoh:

```
include: package:flutter_lints/flutter.yaml
```

File ini menentukan aturan lint seperti:

* style penulisan kode
* warning
* error coding

Dengan konfigurasi yang sama, seluruh tim akan mengikuti standar kode yang sama.

---

# 10. Menghindari Masalah Line Ending (Windows vs Linux)

Windows menggunakan line ending **CRLF**, sedangkan Linux dan macOS menggunakan **LF**.

Perbedaan ini dapat menyebabkan perubahan file yang tidak perlu di Git.

Untuk menghindarinya, tambahkan file berikut di root project:

```
.gitattributes
```

Isi contoh:

```
* text=auto
*.dart text eol=lf
```

Keuntungan:

* Menghindari konflik line ending
* Perubahan file di Git lebih bersih

---

# 11. Menggunakan Script Setup Project

Beberapa tim membuat script untuk mempermudah setup project bagi developer baru.

Contoh:

```
scripts/setup.sh
```

Isi contoh:

```
fvm install
fvm flutter pub get
```

Developer cukup menjalankan:

```
./scripts/setup.sh
```

Script ini akan menyiapkan environment project secara otomatis.

---

# 12. Menggunakan CI/CD untuk Build Konsisten

Continuous Integration (CI) membantu memastikan project selalu bisa dibuild dengan environment yang sama.

Contoh CI yang sering digunakan:

* GitHub Actions
* GitLab CI
* Bitrise

CI biasanya akan:

* Menginstall Flutter versi tertentu
* Menginstall dependency
* Menjalankan build
* Menjalankan testing

Dengan CI, setiap perubahan pada repository akan diuji secara otomatis.

---

# Kesimpulan

Agar project Flutter stabil ketika dijalankan di berbagai sistem operasi atau oleh anggota tim yang berbeda, beberapa komponen penting harus dikunci versinya.

Komponen yang sebaiknya dikunci:

* Flutter SDK
* Dart dependencies
* Gradle
* Android Gradle Plugin
* Kotlin
* Android SDK
* Android NDK
* CMake
* Code style
* Line ending Git

Dengan konfigurasi tersebut, project akan memiliki **Reproducible Build Environment**, yaitu:

* Project dapat dijalankan di komputer manapun
* Environment development konsisten
* Hasil build tetap sama
* Risiko error karena perbedaan konfigurasi menjadi sangat kecil
