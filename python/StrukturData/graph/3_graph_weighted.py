"""
IMPLEMENTASI GRAF BERBOBOT (WEIGHTED GRAPH) - BERARAH
Setiap edge memiliki bobot (weight) yang merepresentasikan jarak/biaya
"""

class Graph:
    def __init__(self, size):
        """Inisialisasi graf dengan None untuk edge yang tidak ada"""
        self.adj_matrix = [[None for _ in range(size)] for _ in range(size)]
        self.size = size
        self.vertex_data = [""] * size

    def add_edge(self, u, v, weight):
        """Menambahkan edge berarah dari u ke v dengan bobot tertentu"""
        if u < self.size and v < self.size:
            self.adj_matrix[u][v] = weight
            print(f"Edge ditambahkan: {self.vertex_data[u]} → {self.vertex_data[v]} (bobot: {weight})")
            
            # Untuk graf tidak berarah, aktifkan baris di bawah:
            # self.adj_matrix[v][u] = weight
        else:
            print(f"Error: Vertex {u} atau {v} di luar batas")

    def add_vertex_data(self, vertex, data):
        """Memberi label/nama pada vertex"""
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data
        else:
            print(f"Error: Vertex {vertex} di luar batas")

    def print_graph(self):
        """Mencetak adjacency matrix berbobot"""
        print("\n" + "="*50)
        print("ADJACENCY MATRIX (WEIGHTED):")
        print("="*50)
        
        # Header
        print("   ", end="")
        for v in self.vertex_data:
            print(f" {v}", end=" ")
        print()
        
        # Matrix
        for i, row in enumerate(self.adj_matrix):
            print(f"{self.vertex_data[i]} ", end="")
            for val in row:
                if val is None:
                    print(" ∞", end=" ")
                else:
                    print(f" {val}", end=" ")
            print()
        
        print("\n" + "="*50)
        print("VERTEX DATA:")
        print("="*50)
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex}: {data}")

# Contoh penggunaan
print("MEMBUAT GRAF BERBOBOT (BERARAH)")
print("="*50)

g = Graph(4)

g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')

g.add_edge(0, 1, 3)  # A → B (bobot 3)
g.add_edge(0, 2, 2)  # A → C (bobot 2)
g.add_edge(3, 0, 4)  # D → A (bobot 4)
g.add_edge(2, 1, 1)  # C → B (bobot 1)

g.print_graph()

print("\n" + "="*50)
print("KETERANGAN:")
print("="*50)
print("∞ = tidak ada edge langsung (tak terhingga)")
print("Angka = bobot edge (jarak/biaya)")