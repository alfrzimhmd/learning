<?php
include __DIR__ . '/config.php';

if (isset($_GET['id'])) {
    $id = intval($_GET['id']);
    
    // Konfirmasi penghapusan (sudah ada di JavaScript di index.php)
    $query = "DELETE FROM tugas WHERE id = $id";
    
    if (mysqli_query($koneksi, $query)) {
        header("Location: index.php?message=Tugas berhasil dihapus&type=success");
    } else {
        header("Location: index.php?message=Gagal menghapus tugas&type=error");
    }
} else {
    header("Location: index.php?message=ID tidak valid&type=error");
}

exit();
?>