"""
BIG O NOTATION: O(n³) - KUBIK
Waktu eksekusi proporsional dengan n³.
Contoh: Floyd-Warshall (shortest path), triple nested loop.
"""

def floyd_warshall(graph):
    """
    Mencari shortest path antara semua pasangan node.
    Kompleksitas: O(V³) dimana V adalah jumlah vertex.
    """
    n = len(graph)
    # Salin graph agar tidak mengubah original
    dist = [row[:] for row in graph]
    
    # Triple nested loop = O(n³)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

# Contoh penggunaan
INF = float('inf')
graph = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]

print("="*50)
print("CONTOH O(n³) - FLOYD-WARSHALL")
print("="*50)
print("Graph awal (jarak antar node):")
for i, row in enumerate(graph):
    print(f"Node {i}: {row}")

print("\nShortest path antara semua node:")
result = floyd_warshall(graph)
for i, row in enumerate(result):
    # Mengganti INF dengan 'inf' untuk tampilan rapi
    formatted = ['inf' if x == INF else x for x in row]
    print(f"Node {i}: {formatted}")

# Demonstrasi pertumbuhan O(n³)
print("\n" + "="*50)
print("PERTUMBUHAN WAKTU O(n³):")
print("="*50)

def demo_n_cubed(n):
    """Triple nested loop sederhana untuk demonstrasi"""
    counter = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                counter += 1
    return counter

for n in [10, 20, 30, 40, 50]:
    operasi = demo_n_cubed(n)
    print(f"n = {n:2d} -> n³ = {n**3:6d} -> operasi = {operasi:6d}")

print("\n n=1000 -> 1 MILYAR operasi!")