"""
IMPLEMENTASI DFS (Depth First Search) dan BFS (Breadth First Search)
Pada Graf Menggunakan Adjacency Matrix
"""

class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v):
        if u < self.size and v < self.size:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1  # Graf tidak berarah

    def add_vertex_data(self, vertex, data):
        if vertex < self.size:
            self.vertex_data[vertex] = data

    def print_graph(self):
        print("\n" + "="*50)
        print("ADJACENCY MATRIX:")
        print("="*50)
        print("   ", end="")
        for v in self.vertex_data:
            print(f" {v}", end=" ")
        print()
        for i, row in enumerate(self.adj_matrix):
            print(f"{self.vertex_data[i]}  {row}")

    def dfs_util(self, v, visited):
        """Helper function untuk DFS (rekursif)"""
        visited[v] = True
        print(self.vertex_data[v], end=' ')
        
        for i in range(self.size):
            if self.adj_matrix[v][i] == 1 and not visited[i]:
                self.dfs_util(i, visited)

    def dfs(self, start_vertex_data):
        """Depth First Search - mencari dengan kedalaman terlebih dahulu"""
        visited = [False] * self.size
        if start_vertex_data in self.vertex_data:
            start_vertex = self.vertex_data.index(start_vertex_data)
            print(f"DFS dari {start_vertex_data}: ", end="")
            self.dfs_util(start_vertex, visited)
            print()
        else:
            print(f"Vertex {start_vertex_data} tidak ditemukan!")

    def bfs(self, start_vertex_data):
        """Breadth First Search - mencari dengan melebar terlebih dahulu"""
        visited = [False] * self.size
        if start_vertex_data in self.vertex_data:
            start_vertex = self.vertex_data.index(start_vertex_data)
            queue = [start_vertex]
            visited[start_vertex] = True
            
            print(f"BFS dari {start_vertex_data}: ", end="")
            while queue:
                current_vertex = queue.pop(0)
                print(self.vertex_data[current_vertex], end=' ')
                
                for i in range(self.size):
                    if self.adj_matrix[current_vertex][i] == 1 and not visited[i]:
                        queue.append(i)
                        visited[i] = True
            print()
        else:
            print(f"Vertex {start_vertex_data} tidak ditemukan!")

# Membangun graf
print("MEMBUAT GRAF DENGAN 7 VERTEX")
print("="*50)

g = Graph(7)

# Menambahkan vertex
vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
for i, v in enumerate(vertices):
    g.add_vertex_data(i, v)

# Menambahkan edge (berdasarkan diagram)
edges = [
    (3, 0), (0, 2), (0, 3), (0, 4),  # D-A, A-C, A-D, A-E
    (4, 2), (2, 5), (2, 1), (2, 6),  # E-C, C-F, C-B, C-G
    (1, 5)                            # B-F
]

for u, v in edges:
    g.add_edge(u, v)

g.print_graph()

# Demonstrasi DFS dan BFS
print("\n" + "="*50)
print("TRAVERSAL ALGORITHMS:")
print("="*50)

g.dfs('D')
g.bfs('D')

print("\n" + "="*50)
print("PERBEDAAN DFS vs BFS:")
print("="*50)
print("DFS (Depth First):  Menelusuri sedalam mungkin terlebih dahulu")
print("BFS (Breadth First): Menelusuri melebar per level terlebih dahulu")