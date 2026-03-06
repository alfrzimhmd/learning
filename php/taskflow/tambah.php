<?php
include __DIR__ . '/config.php';
?>
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tambah Tugas Baru - TaskFlow</title>
    <link rel="stylesheet" href="assets/css/style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <div class="container">
        <!-- Header & Navigasi -->
        <header>
            <div class="header-content">
                <div class="logo">
                    <i class="fas fa-tasks"></i>
                    <div class="logo-text">
                        <h1>TaskFlow</h1>
                        <p class="tagline">Manajemen Tugas Harian yang Efisien</p>
                    </div>
                </div>
                <nav>
                    <a href="index.php" class="nav-link">
                        <i class="fas fa-arrow-left"></i> Kembali
                    </a>
                    <a href="tambah.php" class="nav-link active">
                        <i class="fas fa-plus-circle"></i> Tambah Tugas
                    </a>
                </nav>
            </div>
        </header>

        <!-- Form Container -->
        <div class="form-container">
            <div class="form-card">
                <div class="form-header">
                    <h2>
                        <i class="fas fa-plus-circle"></i>
                        Tambah Tugas Baru
                    </h2>
                    <p>Isi formulir di bawah untuk menambahkan tugas baru ke dalam sistem</p>
                </div>
                
                <?php
                // Proses form jika ada data POST
                if ($_SERVER['REQUEST_METHOD'] == 'POST') {
                    $judul = mysqli_real_escape_string($koneksi, $_POST['judul']);
                    $deskripsi = mysqli_real_escape_string($koneksi, $_POST['deskripsi']);
                    $deadline = !empty($_POST['deadline']) ? $_POST['deadline'] : null;
                    
                    // Validasi
                    $errors = [];
                    
                    if (empty($judul)) {
                        $errors[] = "Judul tugas wajib diisi";
                    } elseif (strlen($judul) > 255) {
                        $errors[] = "Judul terlalu panjang (maksimal 255 karakter)";
                    }
                    
                    if (empty($errors)) {
                        $query = "INSERT INTO tugas (judul, deskripsi, deadline, status) 
                                  VALUES ('$judul', '$deskripsi', " . ($deadline ? "'$deadline'" : "NULL") . ", 'Pending')";
                        
                        if (mysqli_query($koneksi, $query)) {
                            echo "<div class='form-alert success'>
                                    <div class='form-alert-content'>
                                        <i class='fas fa-check-circle'></i>
                                        <span>Tugas berhasil ditambahkan!</span>
                                    </div>
                                    <a href='index.php' class='btn-link'>Lihat Daftar Tugas</a>
                                  </div>";
                            // Reset form values
                            $judul = $deskripsi = $deadline = '';
                        } else {
                            echo "<div class='form-alert error'>
                                    <div class='form-alert-content'>
                                        <i class='fas fa-exclamation-circle'></i>
                                        <span>Gagal menambahkan tugas: " . mysqli_error($koneksi) . "</span>
                                    </div>
                                  </div>";
                        }
                    } else {
                        echo "<div class='form-alert error'>
                                <div class='form-alert-content'>
                                    <i class='fas fa-exclamation-circle'></i>
                                    <span>" . implode('<br>', $errors) . "</span>
                                </div>
                              </div>";
                    }
                }
                ?>

                <form method="POST" action="" id="formTambahTugas" novalidate>
                    <div class="form-group">
                        <label for="judul" class="form-label">
                            <i class="fas fa-heading"></i>
                            Judul Tugas
                            <span class="required">*</span>
                        </label>
                        <input type="text" 
                               id="judul" 
                               name="judul" 
                               class="form-control" 
                               placeholder="Masukkan judul tugas"
                               value="<?php echo isset($judul) ? htmlspecialchars($judul) : ''; ?>"
                               required
                               maxlength="255">
                        <small id="judul-error" class="error-text"></small>
                        <small class="form-hint">Judul harus jelas dan deskriptif</small>
                    </div>

                    <div class="form-group">
                        <label for="deskripsi" class="form-label">
                            <i class="fas fa-align-left"></i>
                            Deskripsi Tugas
                        </label>
                        <textarea id="deskripsi" 
                                  name="deskripsi" 
                                  class="form-control" 
                                  placeholder="Deskripsi detail tugas (opsional)"
                                  rows="4"><?php echo isset($deskripsi) ? htmlspecialchars($deskripsi) : ''; ?></textarea>
                        <small class="form-hint">Jelaskan detail tugas untuk memudahkan pemahaman</small>
                    </div>

                    <div class="form-group">
                        <label for="deadline" class="form-label">
                            <i class="fas fa-calendar-day"></i>
                            Deadline
                        </label>
                        <input type="date" 
                               id="deadline" 
                               name="deadline" 
                               class="form-control"
                               value="<?php echo isset($deadline) ? $deadline : date('Y-m-d', strtotime('+3 days')); ?>"
                               min="<?php echo date('Y-m-d'); ?>">
                        <small class="form-hint">Pilih tanggal deadline untuk tugas ini</small>
                    </div>

                    <div class="form-actions">
                        <button type="submit" class="btn-submit">
                            <i class="fas fa-save"></i> Simpan Tugas
                        </button>
                        <a href="index.php" class="btn-cancel">
                            <i class="fas fa-times"></i> Batal
                        </a>
                    </div>
                </form>
            </div>
        </div>

        <!-- Footer -->
        <footer>
            <div class="footer-content">
                <div class="footer-logo">
                    <i class="fas fa-tasks"></i>
                    <span>TaskFlow</span>
                </div>
                <p class="footer-text">
                    Proyek Akhir Pemrograman dan Desain Web &copy; 2025
                </p>
            </div>
        </footer>
    </div>

    <!-- JavaScript Validasi -->
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Set default deadline ke 3 hari dari sekarang
            const defaultDeadline = new Date();
            defaultDeadline.setDate(defaultDeadline.getDate() + 3);
            const deadlineInput = document.getElementById('deadline');
            
            if (deadlineInput && !deadlineInput.value) {
                deadlineInput.value = defaultDeadline.toISOString().split('T')[0];
            }
            
            // Validasi form
            const form = document.getElementById('formTambahTugas');
            const judulInput = document.getElementById('judul');
            const judulError = document.getElementById('judul-error');
            
            function validateJudul() {
                const value = judulInput.value.trim();
                
                if (value === '') {
                    judulError.textContent = 'Judul tugas wajib diisi';
                    judulInput.style.borderColor = 'var(--danger)';
                    return false;
                } else if (value.length > 255) {
                    judulError.textContent = 'Judul terlalu panjang (maksimal 255 karakter)';
                    judulInput.style.borderColor = 'var(--danger)';
                    return false;
                } else {
                    judulError.textContent = '';
                    judulInput.style.borderColor = 'var(--success)';
                    return true;
                }
            }
            
            form.addEventListener('submit', function(event) {
                if (!validateJudul()) {
                    event.preventDefault();
                    alert('Harap perbaiki kesalahan sebelum mengirim form.');
                    judulInput.focus();
                }
            });
            
            // Real-time validation
            if (judulInput) {
                judulInput.addEventListener('input', validateJudul);
                judulInput.addEventListener('blur', validateJudul);
            }
            
            // Auto-resize textarea
            const textarea = document.getElementById('deskripsi');
            if (textarea) {
                textarea.addEventListener('input', function() {
                    this.style.height = 'auto';
                    this.style.height = (this.scrollHeight) + 'px';
                });
            }
        });
    </script>
</body>
</html>