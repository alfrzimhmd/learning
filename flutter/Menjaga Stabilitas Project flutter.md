# Menjaga Stabilitas Project Flutter (Lintas OS & Tim Development)

Dalam pengembangan aplikasi Flutter, sebuah project tidak selalu dijalankan hanya pada satu komputer atau satu sistem operasi saja. Project sering kali dijalankan oleh beberapa developer dalam satu tim, bahkan pada sistem operasi yang berbeda seperti **Linux, Windows, atau macOS**.

Perbedaan environment development ini sering menjadi penyebab munculnya berbagai masalah ketika project dijalankan pada komputer yang berbeda. Sebuah project yang dapat berjalan dengan baik pada satu komputer belum tentu dapat langsung berjalan dengan baik pada komputer developer lain.

Beberapa contoh masalah yang sering terjadi antara lain:

- Perbedaan versi Flutter SDK
- Dependency plugin yang berubah
- Versi Gradle yang tidak kompatibel
- Versi Kotlin yang berbeda
- Android SDK yang tidak sama
- Perbedaan Android NDK
- Perbedaan line ending antara Windows dan Linux
- Perbedaan konfigurasi build Android

Masalah-masalah tersebut dapat menyebabkan berbagai dampak seperti:

- Build project gagal
- Error dependency plugin
- Error saat menjalankan aplikasi
- Perilaku aplikasi berbeda pada setiap komputer
- Hasil build APK atau AAB tidak konsisten

Untuk menghindari permasalahan tersebut, developer perlu memastikan bahwa environment development dapat **direproduksi secara konsisten**.

Konsep ini dikenal dengan istilah **Reproducible Build Environment**.

Reproducible Build Environment berarti:

> Project dapat dijalankan di komputer manapun dengan konfigurasi yang sama sehingga menghasilkan build yang konsisten.

Agar hal tersebut dapat tercapai, beberapa komponen dalam project Flutter perlu **dikunci versinya (version locking)** sehingga setiap developer menggunakan versi yang sama.

Berikut adalah beberapa komponen penting yang perlu diperhatikan untuk menjaga stabilitas project Flutter.

---

## 1. Mengunci Versi Flutter SDK  
Flutter SDK merupakan komponen utama dalam pengembangan aplikasi Flutter. Versi Flutter yang digunakan akan mempengaruhi berbagai aspek seperti:  
- kompatibilitas plugin
- sistem build Android
- kompatibilitas dengan Dart SDK
- kompatibilitas dengan Gradle dan Android SDK  
Jika developer menggunakan versi Flutter yang berbeda, sering kali muncul masalah seperti:
- plugin tidak kompatibel
- build error
- perbedaan perilaku aplikasi  
Untuk mengatasi masalah tersebut, sangat disarankan menggunakan **Flutter Version Manager (FVM)**.  
FVM adalah tool yang digunakan untuk mengelola berbagai versi Flutter SDK pada satu komputer. Dengan FVM, setiap project dapat menggunakan versi Flutter yang berbeda tanpa menyebabkan konflik.  
Contoh penggunaan FVM:
```bash
fvm install 3.19.6
fvm use 3.19.6
```  
Perintah pertama akan menginstall Flutter versi tertentu, sedangkan perintah kedua akan mengatur agar project menggunakan versi tersebut. Setelah perintah tersebut dijalankan, akan dibuat folder konfigurasi berikut di dalam project:  
```
.fvm/
   ├── flutter_sdk
   └── fvm_config.json
```  
Isi file fvm_config.json biasanya seperti berikut:  
```
{
  "flutterSdkVersion": "3.19.6"
}
```  
File ini berfungsi untuk menyimpan informasi versi Flutter yang digunakan oleh project. Jika developer lain melakukan clone repository dan menggunakan FVM, mereka cukup menjalankan:  
```
fvm install
```
FVM akan otomatis menginstall versi Flutter yang sesuai dengan konfigurasi project.  
Keuntungan menggunakan FVM:  
- Setiap project menggunakan versi Flutter yang konsisten
- Menghindari konflik ketika upgrade Flutter
- Mempermudah pengembangan lintas OS
- Mempermudah setup project untuk developer baru
---

## 2. Mengunci Dependency Dart / Flutter  
Setiap project Flutter menggunakan berbagai dependency atau package dari ekosistem Dart. Dependency tersebut didefinisikan di file:
```
pubspec.yaml
```
Contoh:
```
dependencies:
  http: ^1.2.0
  provider: ^6.0.5
```
Tanda ^ berarti Flutter dapat menggunakan versi terbaru yang masih kompatibel. Namun versi dependency yang benar-benar digunakan oleh project disimpan di file:  
```
pubspec.lock
```
File ini sangat penting karena berisi versi dependency yang tepat dan pasti.  
Contoh isi pubspec.lock:
```
http 1.2.0
provider 6.0.5
```
Ketika developer lain menjalankan:
```
flutter pub get
```
Flutter akan menginstall dependency sesuai dengan versi yang terdapat pada `pubspec.lock.` Oleh karena itu, file pubspec.lock harus selalu di-commit ke repository.  
Keuntungan mengunci dependency:  
- Dependency plugin selalu konsisten
- Menghindari perubahan versi plugin secara otomatis
- Mengurangi kemungkinan munculnya bug akibat update dependency
---

## 3. Mengunci Versi Gradle  
Gradle adalah sistem build yang digunakan oleh Android untuk mengcompile aplikasi. Versi Gradle yang digunakan oleh project dikunci pada file berikut:  
```
android/gradle/wrapper/gradle-wrapper.properties
```
Contoh isi file tersebut:
```
distributionUrl=https://services.gradle.org/distributions/gradle-8.3-all.zip
```
Ketika project dijalankan di komputer lain, Gradle Wrapper akan otomatis mengunduh versi Gradle yang sama sesuai dengan konfigurasi tersebut. Dengan menggunakan Gradle Wrapper, developer tidak perlu menginstall Gradle secara manual di komputer mereka.  
Keuntungan:  
- Build Android menjadi konsisten
- Menghindari konflik versi Gradle
- Setup project menjadi lebih mudah
---

## 4. Mengunci Android Gradle Plugin  
Android Gradle Plugin (AGP) adalah plugin yang digunakan oleh Gradle untuk membangun aplikasi Android. Versi plugin ini biasanya ditentukan pada file:
```
android/build.gradle
```
Contoh konfigurasi:
```
classpath 'com.android.tools.build:gradle:8.2.2'
```
Versi Android Gradle Plugin harus kompatibel dengan:  
- versi Gradle
- versi Android SDK
- versi Kotlin  
Jika versi tersebut tidak cocok, build Android dapat gagal. Oleh karena itu versi Android Gradle Plugin sebaiknya tidak diubah sembarangan.
---

## 5. Mengunci Versi Kotlin  
Kotlin digunakan pada bagian native Android dalam project Flutter. Versi Kotlin biasanya ditentukan pada file berikut:
```
android/build.gradle
```
Contoh:
```
ext.kotlin_version = '1.9.22'
```
Jika developer menggunakan versi Kotlin yang berbeda, dapat muncul error seperti: 
```
Kotlin version mismatch
```
atau
```
Unsupported Kotlin version
```
Dengan mengunci versi Kotlin pada project, seluruh developer akan menggunakan versi Kotlin yang sama saat build.  

---

## 6. Mengunci Android SDK Version  
Versi Android SDK yang digunakan untuk compile aplikasi ditentukan pada file:  
```
android/app/build.gradle
```
Contoh konfigurasi:
```
compileSdkVersion 34
minSdkVersion 21
targetSdkVersion 34
```
Penjelasan:
- compileSdkVersion
  versi Android SDK yang digunakan untuk compile aplikasi.  
- minSdkVersion
  versi Android minimum yang dapat menjalankan aplikasi.  
- targetSdkVersion
  versi Android yang menjadi target optimasi aplikasi.  
Jika SDK tersebut belum tersedia di komputer developer lain, Android Studio biasanya akan meminta untuk menginstall SDK yang dibutuhkan.
---

## 7. Mengunci Versi Android NDK  
NDK (Native Development Kit) digunakan jika project menggunakan library native berbasis C atau C++.  
Beberapa plugin Flutter seperti:
- camera
- ffmpeg
- tensorflow
- plugin berbasis native  
memerlukan NDK saat proses build. Versi NDK dapat dikunci di file berikut:
```
android/app/build.gradle
```
Contoh:
```
ndkVersion "26.1.10909125"
```
Dengan mengunci versi NDK, proses build native akan lebih konsisten di semua komputer developer.  

---

## 8. Mengunci Versi CMake  
Beberapa plugin Flutter menggunakan CMake untuk membangun kode native. Versi CMake dapat ditentukan dalam konfigurasi project Android.  
Contoh:
```
cmakeVersion "3.22.1"
```
Jika versi CMake berbeda antar komputer developer, proses build native dapat gagal. Mengunci versi CMake membantu menjaga konsistensi build native.

---
## 9. Menjaga Konsistensi Code Style  
Dalam pengembangan tim, penting untuk menjaga konsistensi penulisan kode. Flutter menyediakan file konfigurasi lint:  
```
analysis_options.yaml
```
Contoh isi:
```
include: package:flutter_lints/flutter.yaml
```
File ini mengatur berbagai aturan seperti:
- style penulisan kode
- warning coding
- aturan analisis statis
- best practice Dart  
Dengan menggunakan aturan lint yang sama, seluruh developer akan mengikuti standar kode yang konsisten. Hal ini membuat kode lebih mudah dibaca dan dipelihara.
---

## 10. Menghindari Masalah Line Ending (Windows vs Linux)  
Sistem operasi yang berbeda menggunakan format line ending yang berbeda.  
Windows menggunakan:
```
CRLF
```  
Sedangkan Linux dan macOS menggunakan:
```
LF
```
Perbedaan ini dapat menyebabkan Git mendeteksi perubahan file yang sebenarnya tidak berubah. Untuk menghindari masalah tersebut, sebaiknya tambahkan file berikut pada root project:
```
.gitattributes
```
Contoh isi:
```
* text=auto
*.dart text eol=lf
```  
Dengan konfigurasi ini, Git akan menyesuaikan line ending secara otomatis.  
Keuntungan:
- Menghindari konflik line ending
- Perubahan file di Git menjadi lebih bersih

---
## 11. Menggunakan Script Setup Project
Dalam project tim, biasanya developer baru perlu menjalankan beberapa perintah untuk menyiapkan environment project. Untuk mempermudah proses ini, beberapa tim membuat script setup project.  
Contoh struktur folder:
```
scripts/
   setup.sh
```
Contoh isi script:
```
fvm install
fvm flutter pub get
```
Developer cukup menjalankan:
```
./scripts/setup.sh
```
Script tersebut akan:
- menginstall Flutter yang diperlukan
- menginstall dependency project
- menyiapkan environment development    
Dengan cara ini proses setup project menjadi lebih cepat dan konsisten.

---
## 12. Menggunakan CI/CD untuk Build Konsisten  
Continuous Integration (CI) digunakan untuk memastikan bahwa project selalu dapat dibuild dengan environment yang konsisten.  
Beberapa platform CI yang sering digunakan antara lain:
- GitHub Actions
- GitLab CI
- Bitrise
- Codemagic  
CI biasanya melakukan beberapa langkah otomatis seperti:
- menginstall Flutter
- menginstall dependency
- menjalankan analisis kode
- menjalankan testing
- melakukan build aplikasi  
Dengan CI, setiap perubahan pada repository akan diuji secara otomatis sehingga masalah dapat terdeteksi lebih awal.
---

## Glosarium Istilah Penting  
Bagian ini berisi beberapa istilah teknis yang sering digunakan dalam pengembangan aplikasi Flutter, khususnya yang berkaitan dengan sistem build Android dan pengelolaan environment development.  
Glosarium ini bertujuan untuk membantu memahami komponen-komponen penting yang disebutkan dalam materi sebelumnya.

### 1. Flutter SDK  
Flutter SDK adalah kumpulan tools yang digunakan untuk mengembangkan aplikasi menggunakan framework Flutter.
Flutter SDK berisi berbagai komponen penting seperti:
- Flutter framework
- Dart SDK
- Flutter CLI tools
- engine Flutter
- library bawaan Flutter

Flutter SDK digunakan untuk:
- membuat project Flutter
- menjalankan aplikasi
- melakukan build APK / AAB
- menjalankan testing

Contoh perintah yang menggunakan Flutter SDK:
```
flutter create
flutter run
flutter build apk
```
Ketika menggunakan **FVM**, setiap project dapat menggunakan Flutter SDK dengan versi yang berbeda.  

### 2. Dart SDK  
Dart SDK adalah kumpulan tools yang digunakan untuk menjalankan dan mengcompile bahasa pemrograman Dart. Flutter sendiri menggunakan bahasa pemrograman **Dart**, sehingga Dart SDK merupakan bagian penting dari Flutter SDK.  
Dart SDK menyediakan beberapa fitur seperti: 
- compiler Dart
- runtime Dart
- package manager (`pub`)
- tools analisis kode  
Biasanya Dart SDK sudah termasuk di dalam Flutter SDK sehingga developer tidak perlu menginstallnya secara terpisah.

### 3. Android SDK  
Android SDK (Software Development Kit) adalah kumpulan tools dan library yang digunakan untuk mengembangkan aplikasi Android.  
Android SDK berisi berbagai komponen seperti:
- Android platform libraries
- build tools
- emulator Android
- debugging tools  
Flutter menggunakan Android SDK ketika melakukan build aplikasi Android. Beberapa konfigurasi Android SDK dalam project Flutter antara lain:
- `compileSdkVersion`
- `targetSdkVersion`
- `minSdkVersion`  
Jika Android SDK yang dibutuhkan belum tersedia di komputer developer, Android Studio biasanya akan meminta untuk menginstallnya.

### 4. Android NDK  
Android NDK (Native Development Kit) adalah tool yang digunakan untuk mengembangkan atau menjalankan kode **native C atau C++** pada aplikasi Android.  
NDK biasanya digunakan oleh plugin yang membutuhkan performa tinggi atau akses ke library native.  
Contoh plugin Flutter yang sering menggunakan NDK:
- plugin kamera
- plugin machine learning
- plugin multimedia
- plugin berbasis C/C++  
Versi NDK dapat dikunci di konfigurasi project untuk menjaga konsistensi build.  

### 5. Gradle  
Gradle adalah sistem build yang digunakan oleh Android untuk mengcompile dan membangun aplikasi.  
Gradle bertanggung jawab untuk berbagai proses seperti:
- mengcompile kode
- mengelola dependency
- menggenerate file APK atau AAB
- menjalankan task build  
Dalam project Flutter, Gradle digunakan pada bagian **Android module**.  
Konfigurasi Gradle biasanya terdapat pada folder:
```
android/gradle/
```

### 6. Gradle Wrapper  
Gradle Wrapper adalah mekanisme yang memungkinkan project menggunakan versi Gradle tertentu tanpa harus menginstall Gradle secara manual.
Konfigurasi Gradle Wrapper berada pada file:
```
android/gradle/wrapper/gradle-wrapper.properties
```
Ketika project dijalankan, Gradle Wrapper akan otomatis mengunduh versi Gradle yang sesuai dengan konfigurasi project.  
Hal ini memastikan seluruh developer menggunakan versi Gradle yang sama.  

### 7. Android Gradle Plugin (AGP)  
Android Gradle Plugin (AGP) adalah plugin yang digunakan oleh Gradle untuk membangun aplikasi Android.  
Plugin ini menyediakan berbagai fitur seperti:
- proses build aplikasi Android
- pengelolaan resource Android
- pengaturan dependency Android
- optimasi build  
Versi AGP harus kompatibel dengan:
- Gradle
- Android SDK
- Kotlin  
Jika versi tersebut tidak kompatibel, build Android dapat gagal.  

### 8. Kotlin  
Kotlin adalah bahasa pemrograman yang digunakan untuk mengembangkan aplikasi Android modern.  
Walaupun Flutter menggunakan Dart untuk menulis kode aplikasi, bagian native Android pada project Flutter masih menggunakan Kotlin atau Java.  
Contoh file Kotlin pada project Flutter:
```
android/app/src/main/kotlin/MainActivity.kt
```
Versi Kotlin biasanya dikonfigurasi pada file:
```
android/build.gradle
```

### 9. CMake  
CMake adalah tool yang digunakan untuk mengatur proses build pada project yang menggunakan kode **native C atau C++**. Dalam project Flutter, CMake biasanya digunakan oleh plugin yang membutuhkan kompilasi kode native.  
Contohnya:
- plugin multimedia
- plugin machine learning
- plugin native library  
CMake membantu mengatur bagaimana kode native dikompilasi menjadi library yang dapat digunakan oleh aplikasi Android.

### 10. Dependency  
Dependency adalah library atau package tambahan yang digunakan oleh project untuk menambahkan fitur tertentu tanpa harus menulis kode dari awal.  
Contoh dependency dalam Flutter:
- `http`
- `provider`
- `shared_preferences`
- `firebase_core`  
Dependency biasanya didefinisikan dalam file:
```
pubspec.yaml
```
Versi dependency yang digunakan oleh project disimpan dalam file:
```
pubspec.lock
```

### 11. Reproducible Build Environment  
Reproducible Build Environment adalah konsep dimana sebuah project dapat dibangun (build) dengan hasil yang sama pada berbagai komputer atau environment development.  
Artinya:  
- semua developer menggunakan konfigurasi yang sama
- dependency yang digunakan sama
- versi tool yang digunakan sama
- hasil build aplikasi tetap konsisten  
Konsep ini sangat penting dalam pengembangan software tim untuk menghindari masalah build yang tidak konsisten.

### 12. Continuous Integration (CI)  
Continuous Integration (CI) adalah praktik pengembangan software dimana setiap perubahan kode pada repository akan otomatis diuji dan dibuild oleh sistem otomatis.
CI biasanya melakukan beberapa langkah seperti:  
- menginstall environment development
- menginstall dependency
- menjalankan testing
- melakukan build aplikasi  
Contoh platform CI yang sering digunakan dalam project Flutter:
- GitHub Actions
- GitLab CI
- Bitrise
- Codemagic  
CI membantu memastikan bahwa project selalu berada dalam kondisi yang stabil.
---
## Kesimpulan  
Stabilitas project Flutter sangat bergantung pada konsistensi environment development yang digunakan oleh setiap developer.  
Untuk menjaga stabilitas project, beberapa komponen penting sebaiknya dikunci versinya, antara lain:
- Flutter SDK
- Dart dependency
- Gradle
- Android Gradle Plugin
- Kotlin
- Android SDK
- Android NDK
- CMake
- Code style
- Line ending Git  
Dengan menerapkan konfigurasi tersebut, project akan memiliki Reproducible Build Environment, yaitu:
- Project dapat dijalankan di komputer manapun
- Environment development menjadi konsisten
- Hasil build aplikasi tetap sama
- Risiko error akibat perbedaan konfigurasi menjadi sangat kecil

Pendekatan ini sangat penting terutama dalam pengembangan aplikasi Flutter yang melibatkan banyak developer atau dijalankan pada berbagai sistem operasi.
