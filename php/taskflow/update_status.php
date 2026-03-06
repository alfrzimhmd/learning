<?php
include __DIR__ . '/config.php';

if (isset($_GET['id'])) {
    $id = intval($_GET['id']);
    
    // Cek status saat ini
    $query_check = "SELECT status FROM tugas WHERE id = $id";
    $result = mysqli_query($koneksi, $query_check);
    
    if (mysqli_num_rows($result) > 0) {
        $row = mysqli_fetch_assoc($result);
        $new_status = ($row['status'] == 'Pending') ? 'Selesai' : 'Pending';
        
        // Update status
        $query_update = "UPDATE tugas SET status = '$new_status' WHERE id = $id";
        
        if (mysqli_query($koneksi, $query_update)) {
            header("Location: index.php?message=Status berhasil diubah&type=success");
        } else {
            header("Location: index.php?message=Gagal mengubah status&type=error");
        }
    } else {
        header("Location: index.php?message=Tugas tidak ditemukan&type=error");
    }
} else {
    header("Location: index.php?message=ID tidak valid&type=error");
}

exit();
?>