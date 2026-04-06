"""
REPRESENTASI GRAF DENGAN ADJACENCY MATRIX
Graph: struktur data yang terdiri dari vertex (node) dan edge (hubungan)
Adjacency Matrix: matriks persegi untuk menyimpan hubungan antar vertex
"""

vertexData = ['A', 'B', 'C', 'D']

adjacency_matrix = [
    [0, 1, 1, 1],  # A terhubung ke B, C, D
    [1, 0, 1, 0],  # B terhubung ke A, C
    [1, 1, 0, 0],  # C terhubung ke A, B
    [1, 0, 0, 0]   # D terhubung ke A
]

def print_adjacency_matrix(matrix):
    """Mencetak matriks ketetanggaan"""
    print("Adjacency Matrix (0=tidak terhubung, 1=terhubung):")
    print("   " + "  ".join(vertexData))
    for i, row in enumerate(matrix):
        print(f"{vertexData[i]}  {row}")

def print_connections(matrix, vertices):
    """Mencetak daftar koneksi setiap vertex"""
    print("\nKoneksi untuk setiap vertex:")
    for i in range(len(vertices)):
        connections = [vertices[j] for j in range(len(vertices)) if matrix[i][j]]
        print(f"{vertices[i]}: {' '.join(connections) if connections else 'tidak ada koneksi'}")

# Menjalankan fungsi
print_adjacency_matrix(adjacency_matrix)
print_connections(adjacency_matrix, vertexData)

# Visualisasi graf
print("\n" + "="*50)
print("VISUALISASI GRAF:")
print("="*50)
print("    A --- B")
print("    | \\    |")
print("    |  \\   |")
print("    |   \\  |")
print("    D    C |")
print("    |     |")
print("    +------+")