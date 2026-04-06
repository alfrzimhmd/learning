"""
ALGORITMA WARSHALL LENGKAP - MENAMPILKAN RUTE
Menampilkan jalur terpendek beserta node-node yang dilalui
"""

N = 5
INF = 1000

def tampil(data, judul):
    """Mencetak matriks dengan format rapi"""
    print(f"\n{judul}:")
    print("    " + "  ".join([f"V{i+1}" for i in range(N)]))
    for i in range(N):
        print(f"V{i+1}  ", end="")
        for j in range(N):
            if data[i][j] >= INF:
                print("  ∞", end=" ")
            else:
                print(f"{data[i][j]:3d}", end=" ")
        print()
    print()

def warshall(Q, P, R):
    """Algoritma Warshall untuk shortest path dan rute"""
    for k in range(N):
        for i in range(N):
            for j in range(N):
                # Update ketersediaan jalur
                P[i][j] = P[i][j] or (P[i][k] and P[k][j])
                
                # Update jarak terpendek
                if Q[i][k] + Q[k][j] < Q[i][j]:
                    Q[i][j] = Q[i][k] + Q[k][j]
                    
                    # Simpan node perantara untuk rute
                    if R[k][j] == 0:
                        R[i][j] = k + 1  # 1-based index
                    else:
                        R[i][j] = R[k][j]

def tampilkan_rute(awal, akhir, Rute, Beban):
    """
    Menampilkan rute terpendek dari node awal ke node akhir
    """
    a = awal - 1  # Konversi ke 0-based index
    b = akhir - 1
    
    if Beban[a][b] >= INF:
        print(f"\n❌ Tidak ada rute dari V{awal} ke V{akhir}")
        return
    
    # Rekonstruksi rute
    stack = []
    current = b
    
    while Rute[a][current] != 0:
        stack.append(Rute[a][current])
        current = Rute[a][current] - 1
    
    # Buat rute dalam format yang rapi
    rute = [f"V{awal}"]
    for node in stack[::-1]:
        rute.append(f"V{node}")
    rute.append(f"V{akhir}")
    
    print(f"\n{'='*50}")
    print(f"RUTE TERPENDEK DARI V{awal} KE V{akhir}:")
    print(f"{'='*50}")
    print(f"Jalur: {' → '.join(rute)}")
    print(f"Total beban: {Beban[a][b]}")
    print(f"{'='*50}")

# Data graf
Beban = [
    [INF, 1,   3,   INF, INF],
    [INF, INF, 1,   INF, 5],
    [3,   INF, INF, 2,   INF],
    [INF, INF, INF, INF, 1],
    [INF, INF, INF, INF, INF]
]

Jalur = [
    [0, 1, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0]
]

Rute = [
    [INF, 0, 0, INF, INF],
    [INF, INF, 0, INF, 0],
    [0, INF, INF, 0, INF],
    [INF, INF, INF, INF, 0],
    [INF, INF, INF, INF, INF]
]

print("="*50)
print("ALGORITMA WARSHALL - SHORTEST PATH DENGAN RUTE")
print("="*50)
print("Vertex: V1=A, V2=B, V3=C, V4=D, V5=E")
print("\nGraf awal (berarah):")
print("  V1 → V2 (1), V1 → V3 (3)")
print("  V2 → V3 (1), V2 → V5 (5)")
print("  V3 → V1 (3), V3 → V4 (2)")
print("  V4 → V5 (1)")

# Jalankan algoritma
warshall(Beban, Jalur, Rute)

# Tampilkan hasil
print("\n" + "="*50)
print("HASIL ALGORITMA WARSHALL:")
print("="*50)
tampil(Beban, "Jarak Terpendek Antar Vertex")
tampil(Rute, "Node Perantara (0 = langsung)")

# Tampilkan beberapa rute
tampilkan_rute(1, 5, Rute, Beban)  # V1 ke V5
tampilkan_rute(2, 4, Rute, Beban)  # V2 ke V4
tampilkan_rute(3, 5, Rute, Beban)  # V3 ke V5
tampilkan_rute(1, 4, Rute, Beban)  # V1 ke V4