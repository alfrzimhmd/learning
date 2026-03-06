<?php
$host = "localhost";
$user = "root"; // sesuaikan dengan username MySQL Anda
$pass = "root236"; // sesuaikan dengan password MySQL Anda
$db   = "db_praktikum";

$koneksi = mysqli_connect($host, $user, $pass, $db);

// Cek koneksi
if (!$koneksi) {
    die("Koneksi gagal: " . mysqli_connect_error());
}
?>