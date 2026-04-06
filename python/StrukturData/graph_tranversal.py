from collections import deque

# Mapping dari huruf ke indeks dan sebaliknya
nodes = ['A', 'B', 'C', 'D']
node_index = {nodes[i]: i for i in range(len(nodes))}

# Adjacency List
adj_list = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

# Adjacency Matrix (4x4)
adj_matrix = [
    # A  B  C  D
    [0, 1, 1, 0],  # A
    [1, 0, 0, 1],  # B
    [1, 0, 0, 1],  # C
    [0, 1, 1, 0]   # D
]

# DFS dengan adjacency list
def dfs_list(node, visited):
    if node not in visited:
        visited.add(node)
        print(node, end=' ')
        for neighbor in adj_list[node]:
            dfs_list(neighbor, visited)

# BFS dengan adjacency list
def bfs_list(start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            print(node, end=' ')
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# DFS dengan adjacency matrix
def dfs_matrix(index, visited):
    if index not in visited:
        visited.add(index)
        print(nodes[index], end=' ')
        for i, connected in enumerate(adj_matrix[index]):
            if connected == 1:
                dfs_matrix(i, visited)

# BFS dengan adjacency matrix
def bfs_matrix(start_index):
    visited = set()
    queue = deque([start_index])
    while queue:
        current = queue.popleft()
        if current not in visited:
            visited.add(current)
            print(nodes[current], end=' ')
            for i, connected in enumerate(adj_matrix[current]):
                if connected == 1 and i not in visited:
                    queue.append(i)

# ====== Program Utama =======
print("Pilih representasi graf:")
print("1. Adjacency List")
print("2. Adjacency Matrix")
choice = input("Masukkan pilihan (1/2): ")

print()

if choice == '1':
    print("DFS (Adjacency List) dari A:", end=' ')
    dfs_list('A', set())
    print("\nBFS (Adjacency List) dari A:", end=' ')
    bfs_list('A')

elif choice == '2':
    print("DFS (Adjacency Matrix) dari A:", end=' ')
    dfs_matrix(node_index['A'], set())
    print("\nBFS (Adjacency Matrix) dari A:", end=' ')
    bfs_matrix(node_index['A'])

else:
    print("Pilihan tidak valid.")
