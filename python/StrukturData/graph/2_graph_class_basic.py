"""
IMPLEMENTASI GRAF DENGAN CLASS (TIDAK BERARAH / UNDIRECTED GRAPH)
"""

class Graph:
    def __init__(self, size):
        """Inisialisasi graf dengan jumlah vertex tertentu"""
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [""] * size

    def add_edge(self, u, v):
        """Menambahkan edge antara vertex u dan v (tidak berarah)"""
        if u < self.size and v < self.size:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1  # Simetris untuk graf tidak berarah
            print(f"Edge ditambahkan: {self.vertex_data[u]} - {self.vertex_data[v]}")
        else:
            print(f"Error: Vertex {u} atau {v} di luar batas")

    def add_vertex_data(self, vertex, data):
        """Memberi label/nama pada vertex"""
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data
        else:
            print(f"Error: Vertex {vertex} di luar batas")

    def print_graph(self):
        """Mencetak adjacency matrix dan data vertex"""
        print("\n" + "="*50)
        print("ADJACENCY MATRIX:")
        print("="*50)
        # Header
        print("   ", end="")
        for v in self.vertex_data:
            print(f" {v}", end=" ")
        print()
        
        # Matrix
        for i, row in enumerate(self.adj_matrix):
            print(f"{self.vertex_data[i]}  {row}")
        
        print("\n" + "="*50)
        print("VERTEX DATA:")
        print("="*50)
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex}: {data}")

# Contoh penggunaan
print("MEMBUAT GRAF DENGAN 4 VERTEX")
print("="*50)

g = Graph(4)

# Memberi nama vertex
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')

# Menambahkan edge
g.add_edge(0, 1)  # A-B
g.add_edge(0, 2)  # A-C
g.add_edge(0, 3)  # A-D
g.add_edge(1, 2)  # B-C

g.print_graph()