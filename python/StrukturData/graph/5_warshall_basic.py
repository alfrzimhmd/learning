"""
ALGORITMA WARSHALL - MENCARI SHORTEST PATH
mencari jarak terpendek antara semua pasangan vertex dalam graf berbobot
"""

N = 5
INF = 1000  # Simbol tak hingga (tidak ada edge langsung)

def tampil(data, judul):
    """Mencetak matriks dengan format rapi"""
    print(f"\n{judul}:")
    print("    " + "  ".join([str(i+1) for i in range(N)]))
    for i in range(N):
        print(f"{i+1}  ", end="")
        for j in range(N):
            if data[i][j] >= INF:
                print(" ∞", end=" ")
            else:
                print(f"{data[i][j]:2d}", end=" ")
        print()
    print()

def warshall(Q, P, R):
    """
    Algoritma Warshall untuk shortest path
    Q: matriks beban (jarak)
    P: matriks jalur (koneksi)
    R: matriks rute (node perantara)
    """
    for k in range(N):
        for i in range(N):
            for j in range(N):
                # Update jalur (apakah ada path)
                P[i][j] = P[i][j] or (P[i][k] and P[k][j])
                
                # Update jarak terpendek
                if Q[i][k] + Q[k][j] < Q[i][j]:
                    Q[i][j] = Q[i][k] + Q[k][j]
                    # Catat node perantara
                    R[i][j] = (k + 1) if R[k][j] == 0 else R[k][j]

def main():
    # Matriks Beban (jarak antar node)
    Beban = [
        [INF, 1,   3,   INF, INF],
        [INF, INF, 1,   INF, 5],
        [3,   INF, INF, 2,   INF],
        [INF, INF, INF, INF, 1],
        [INF, INF, INF, INF, INF]
    ]
    
    # Matriks Jalur (koneksi langsung)
    Jalur = [
        [0, 1, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 0, 1, 0],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0]
    ]
    
    # Matriks Rute (penyimpan node perantara)
    Rute = [
        [INF, 0, 0, INF, INF],
        [INF, INF, 0, INF, 0],
        [0, INF, INF, 0, INF],
        [INF, INF, INF, INF, 0],
        [INF, INF, INF, INF, INF]
    ]
    
    print("="*50)
    print("ALGORITMA WARSHALL - SHORTEST PATH")
    print("="*50)
    print("Node: 1=A, 2=B, 3=C, 4=D, 5=E")
    
    print("\nSEBELUM ALGORITMA:")
    tampil(Beban, "Matriks Beban (Jarak Awal)")
    tampil(Jalur, "Matriks Jalur (Koneksi Langsung)")
    
    # Jalankan algoritma
    warshall(Beban, Jalur, Rute)
    
    print("\n" + "="*50)
    print("SETELAH ALGORITMA:")
    print("="*50)
    tampil(Beban, "Matriks Beban (Jarak Terpendek)")
    tampil(Jalur, "Matriks Jalur (Path Tersedia)")

if __name__ == "__main__":
    main()