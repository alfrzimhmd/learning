<?php
include __DIR__ . '/config.php';
?>
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TaskFlow - Manajemen Tugas Harian</title>
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
                    <a href="index.php" class="nav-link active">
                        <i class="fas fa-chart-line"></i> Dashboard
                    </a>
                    <a href="tambah.php" class="nav-link">
                        <i class="fas fa-plus-circle"></i> Tambah Tugas
                    </a>
                </nav>
            </div>
        </header>

        <!-- Notifikasi -->
        <?php
        if (isset($_GET['message'])) {
            $message = htmlspecialchars($_GET['message']);
            $type = isset($_GET['type']) ? $_GET['type'] : 'info';
            $icon = ($type == 'success') ? 'fa-check-circle' : 'fa-exclamation-circle';
            $type_class = ($type == 'success') ? 'success' : ($type == 'error' ? 'error' : 'info');
            
            echo "<div class='notification notification-$type_class' id='auto-notification'>
                    <div class='notification-content'>
                        <i class='fas $icon'></i>
                        <span>$message</span>
                    </div>
                    <button class='close-notif' onclick='closeNotification(this)'>&times;</button>
                  </div>";
        }
        ?>

        <!-- Dashboard Stats -->
        <section class="dashboard-section">
            <h2 class="section-title">
                <i class="fas fa-chart-pie"></i> Ringkasan Statistik
            </h2>
            <div class="stats-grid">
                <?php
                // Hitung statistik
                $query_total = "SELECT COUNT(*) as total FROM tugas";
                $result_total = mysqli_query($koneksi, $query_total);
                $row_total = mysqli_fetch_assoc($result_total);
                $total = $row_total ? $row_total['total'] : 0;
                
                $query_selesai = "SELECT COUNT(*) as selesai FROM tugas WHERE status = 'Selesai'";
                $result_selesai = mysqli_query($koneksi, $query_selesai);
                $row_selesai = mysqli_fetch_assoc($result_selesai);
                $selesai = $row_selesai ? $row_selesai['selesai'] : 0;
                
                $query_pending = "SELECT COUNT(*) as pending FROM tugas WHERE status = 'Pending'";
                $result_pending = mysqli_query($koneksi, $query_pending);
                $row_pending = mysqli_fetch_assoc($result_pending);
                $pending = $row_pending ? $row_pending['pending'] : 0;
                ?>
                
                <!-- Card 1: Total Tugas -->
                <div class="stat-card">
                    <div class="stat-content">
                        <div class="stat-icon">
                            <i class="fas fa-clipboard-list"></i>
                        </div>
                        <div class="stat-info">
                            <h3>Total Tugas</h3>
                            <p class="stat-number"><?php echo $total; ?></p>
                            <p class="stat-percent">100% dari total</p>
                        </div>
                    </div>
                    <div class="stat-progress">
                        <div class="progress-bar" style="width: <?php echo $total > 0 ? '100%' : '0%'; ?>"></div>
                    </div>
                </div>
                
                <!-- Card 2: Tugas Selesai -->
                <div class="stat-card">
                    <div class="stat-content">
                        <div class="stat-icon">
                            <i class="fas fa-check-circle"></i>
                        </div>
                        <div class="stat-info">
                            <h3>Tugas Selesai</h3>
                            <p class="stat-number"><?php echo $selesai; ?></p>
                            <p class="stat-percent">
                                <?php echo $total > 0 ? round(($selesai/$total)*100, 1) : '0'; ?>%
                            </p>
                        </div>
                    </div>
                    <div class="stat-progress">
                        <div class="progress-bar" style="width: <?php echo $total > 0 ? ($selesai/$total)*100 : 0; ?>%"></div>
                    </div>
                </div>
                
                <!-- Card 3: Tugas Pending -->
                <div class="stat-card">
                    <div class="stat-content">
                        <div class="stat-icon">
                            <i class="fas fa-clock"></i>
                        </div>
                        <div class="stat-info">
                            <h3>Tugas Pending</h3>
                            <p class="stat-number"><?php echo $pending; ?></p>
                            <p class="stat-percent">
                                <?php echo $total > 0 ? round(($pending/$total)*100, 1) : '0'; ?>%
                            </p>
                        </div>
                    </div>
                    <div class="stat-progress">
                        <div class="progress-bar" style="width: <?php echo $total > 0 ? ($pending/$total)*100 : 0; ?>%"></div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Quick Actions & Search -->
        <section class="action-section">
            <div class="search-container">
                <div class="search-box">
                    <i class="fas fa-search"></i>
                    <input type="text" id="search-input" placeholder="Cari tugas berdasarkan judul atau deskripsi...">
                    <button id="search-clear" class="btn-icon">
                        <i class="fas fa-times"></i>
                    </button>
                </div>
                <div class="quick-actions">
                    <a href="tambah.php" class="btn-action btn-primary">
                        <i class="fas fa-plus"></i> Tambah Tugas Baru
                    </a>
                    <button id="filter-all" class="btn-action btn-secondary active">
                        Semua (<?php echo $total; ?>)
                    </button>
                    <button id="filter-pending" class="btn-action btn-outline">
                        Pending (<?php echo $pending; ?>)
                    </button>
                    <button id="filter-completed" class="btn-action btn-outline">
                        Selesai (<?php echo $selesai; ?>)
                    </button>
                </div>
            </div>
        </section>

        <!-- Tasks Table -->
        <section class="tasks-section">
            <div class="section-header">
                <h2 class="section-title">
                    <i class="fas fa-list-check"></i> Daftar Tugas
                </h2>
                <div class="section-actions">
                    <button id="sort-deadline" class="btn-icon" title="Urutkan deadline">
                        <i class="fas fa-calendar-alt"></i>
                    </button>
                    <button id="sort-status" class="btn-icon" title="Urutkan status">
                        <i class="fas fa-sort-alpha-down"></i>
                    </button>
                </div>
            </div>
            
            <?php if ($total == 0): ?>
            <div class="empty-state">
                <div class="empty-icon">
                    <i class="fas fa-clipboard"></i>
                </div>
                <h3>Belum Ada Tugas</h3>
                <p>Mulai dengan menambahkan tugas pertama Anda</p>
                <a href="tambah.php" class="btn-action btn-primary btn-large">
                    <i class="fas fa-plus"></i> Buat Tugas Pertama
                </a>
            </div>
            <?php else: ?>
            
            <div class="table-responsive">
                <table class="tasks-table">
                    <thead>
                        <tr>
                            <th width="5%">#</th>
                            <th width="25%">Judul Tugas</th>
                            <th width="30%">Deskripsi</th>
                            <th width="15%">Deadline</th>
                            <th width="15%">Status</th>
                            <th width="10%">Aksi</th>
                        </tr>
                    </thead>
                    <tbody id="tasks-body">
                        <?php
                        $query = "SELECT * FROM tugas ORDER BY deadline ASC, status ASC";
                        $result = mysqli_query($koneksi, $query);
                        $no = 1;

                        while ($row = mysqli_fetch_assoc($result)) {
                            $status_class = ($row['status'] == 'Selesai') ? 'status-completed' : 'status-pending';
                            $status_text = ($row['status'] == 'Selesai') ? 'Selesai' : 'Pending';
                            $status_icon = ($row['status'] == 'Selesai') ? 'fa-check-circle' : 'fa-clock';
                            $deadline_formatted = !empty($row['deadline']) ? date('d M Y', strtotime($row['deadline'])) : 'Tanpa deadline';
                            
                            // Check if deadline is near (within 3 days)
                            $deadline_warning = '';
                            if (!empty($row['deadline']) && $row['status'] == 'Pending') {
                                $deadline_date = new DateTime($row['deadline']);
                                $today = new DateTime();
                                $diff = $today->diff($deadline_date)->days;
                                
                                if ($diff <= 3 && $diff >= 0) {
                                    $deadline_warning = 'deadline-near';
                                } elseif ($diff < 0) {
                                    $deadline_warning = 'deadline-overdue';
                                }
                            }
                            ?>
                            
                            <tr class="task-row <?php echo $status_class . ' ' . $deadline_warning; ?>">
                                <td class="task-number"><?php echo $no++; ?></td>
                                <td class="task-title">
                                    <div class="task-title-content">
                                        <i class="fas fa-clipboard"></i>
                                        <div>
                                            <strong><?php echo htmlspecialchars($row['judul']); ?></strong>
                                            <?php if($deadline_warning): ?>
                                            <span class="deadline-badge">
                                                <i class="fas fa-exclamation-triangle"></i>
                                                <?php echo $deadline_warning == 'deadline-overdue' ? 'Terlambat' : 'Segera'; ?>
                                            </span>
                                            <?php endif; ?>
                                        </div>
                                    </div>
                                </td>
                                <td class="task-description">
                                    <?php 
                                    $desc = htmlspecialchars($row['deskripsi']);
                                    echo !empty($desc) ? $desc : '<span class="text-muted">Tidak ada deskripsi</span>';
                                    ?>
                                </td>
                                <td class="task-deadline <?php echo $deadline_warning; ?>">
                                    <i class="fas fa-calendar-day"></i>
                                    <?php echo $deadline_formatted; ?>
                                </td>
                                <td class="task-status">
                                    <span class="status-badge <?php echo $status_class; ?>">
                                        <i class="fas <?php echo $status_icon; ?>"></i>
                                        <?php echo $status_text; ?>
                                    </span>
                                </td>
                                <td class="task-actions">
                                    <div class="action-buttons">
                                        <a href="update_status.php?id=<?php echo $row['id']; ?>" 
                                           class="btn-icon btn-status" 
                                           title="<?php echo $row['status'] == 'Pending' ? 'Tandai Selesai' : 'Tandai Pending'; ?>">
                                            <i class="fas fa-check"></i>
                                        </a>
                                        <a href="hapus.php?id=<?php echo $row['id']; ?>" 
                                           class="btn-icon btn-delete" 
                                           title="Hapus Tugas"
                                           onclick="return confirm('Apakah Anda yakin ingin menghapus tugas ini?')">
                                            <i class="fas fa-trash"></i>
                                        </a>
                                    </div>
                                </td>
                            </tr>
                        <?php } ?>
                    </tbody>
                </table>
            </div>
            
            <div class="table-footer">
                <div class="table-summary">
                    Menampilkan <strong><?php echo $total; ?></strong> tugas
                </div>
                <div class="table-legend">
                    <span class="legend-item">
                        <span class="legend-color pending"></span> Pending
                    </span>
                    <span class="legend-item">
                        <span class="legend-color completed"></span> Selesai
                    </span>
                    <span class="legend-item">
                        <span class="legend-color near"></span> Deadline Mendekati
                    </span>
                </div>
            </div>
            <?php endif; ?>
        </section>

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

    <!-- JavaScript -->
    <script>
        // Auto-hide notification
        function closeNotification(btn) {
            const notification = btn.parentElement;
            notification.style.opacity = '0';
            notification.style.transform = 'translateY(-20px)';
            setTimeout(() => {
                if (notification.parentNode) {
                    notification.remove();
                }
            }, 300);
        }
        
        // Auto-hide after 5 seconds
        const autoNotification = document.getElementById('auto-notification');
        if (autoNotification) {
            setTimeout(() => closeNotification(autoNotification.querySelector('.close-notif')), 5000);
        }
        
        // Search functionality
        document.addEventListener('DOMContentLoaded', function() {
            const searchInput = document.getElementById('search-input');
            const searchClear = document.getElementById('search-clear');
            const filterAll = document.getElementById('filter-all');
            const filterPending = document.getElementById('filter-pending');
            const filterCompleted = document.getElementById('filter-completed');
            const taskRows = document.querySelectorAll('.task-row');
            
            // Clear search
            if (searchClear) {
                searchClear.addEventListener('click', function() {
                    searchInput.value = '';
                    filterTasks();
                });
            }
            
            // Filter buttons
            const filterButtons = [filterAll, filterPending, filterCompleted];
            filterButtons.forEach(btn => {
                if (btn) {
                    btn.addEventListener('click', function() {
                        // Update active button
                        filterButtons.forEach(b => b.classList.remove('active'));
                        this.classList.add('active');
                        
                        // Apply filter
                        filterTasks();
                    });
                }
            });
            
            // Search input
            if (searchInput) {
                searchInput.addEventListener('keyup', filterTasks);
            }
            
            function filterTasks() {
                const searchTerm = searchInput.value.toLowerCase();
                const activeFilter = document.querySelector('.btn-action.active').id;
                
                taskRows.forEach(row => {
                    const title = row.querySelector('.task-title').textContent.toLowerCase();
                    const description = row.querySelector('.task-description').textContent.toLowerCase();
                    const statusClass = row.classList.contains('status-completed') ? 'completed' : 'pending';
                    
                    // Check search term
                    const matchesSearch = searchTerm === '' || 
                                         title.includes(searchTerm) || 
                                         description.includes(searchTerm);
                    
                    // Check filter
                    let matchesFilter = false;
                    if (activeFilter === 'filter-all') matchesFilter = true;
                    else if (activeFilter === 'filter-pending' && statusClass === 'pending') matchesFilter = true;
                    else if (activeFilter === 'filter-completed' && statusClass === 'completed') matchesFilter = true;
                    
                    // Show/hide row
                    row.style.display = (matchesSearch && matchesFilter) ? '' : 'none';
                });
            }
            
            // Sort functionality
            const sortDeadlineBtn = document.getElementById('sort-deadline');
            const sortStatusBtn = document.getElementById('sort-status');
            
            if (sortDeadlineBtn) {
                sortDeadlineBtn.addEventListener('click', function() {
                    alert('Fitur pengurutan akan diimplementasikan lebih lanjut');
                });
            }
            
            if (sortStatusBtn) {
                sortStatusBtn.addEventListener('click', function() {
                    alert('Fitur pengurutan akan diimplementasikan lebih lanjut');
                });
            }
        });
    </script>
</body>
</html>