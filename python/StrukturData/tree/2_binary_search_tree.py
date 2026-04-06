"""
BINARY SEARCH TREE (BST) - POHON PENCARIAN BINER
BST: Binary tree dengan aturan:
- Nilai node kiri < nilai node parent
- Nilai node kanan > nilai node parent
"""

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        """Menambahkan node baru ke BST"""
        def _insert(node, key):
            if not node:
                return Node(key)
            if key < node.key:
                node.left = _insert(node.left, key)
            else:
                node.right = _insert(node.right, key)
            return node
        
        self.root = _insert(self.root, key)
        print(f"Insert {key} → OK")
    
    def search(self, key):
        """Mencari nilai dalam BST"""
        def _search(node, key):
            if not node:
                return False
            if node.key == key:
                return True
            elif key < node.key:
                return _search(node.left, key)
            else:
                return _search(node.right, key)
        
        found = _search(self.root, key)
        print(f"Mencari {key}: {'DITEMUKAN ✓' if found else 'TIDAK DITEMUKAN ✗'}")
        return found
    
    def inorder(self, node):
        """Inorder traversal (menghasilkan data terurut)"""
        if node:
            self.inorder(node.left)
            print(node.key, end=" ")
            self.inorder(node.right)
    
    def min_value(self):
        """Mencari nilai minimum dalam BST"""
        current = self.root
        while current and current.left:
            current = current.left
        return current.key if current else None
    
    def max_value(self):
        """Mencari nilai maksimum dalam BST"""
        current = self.root
        while current and current.right:
            current = current.right
        return current.key if current else None

# Contoh penggunaan
print("="*50)
print("BINARY SEARCH TREE (BST)")
print("="*50)

tree = BST()

# Insert data
data = [50, 30, 70, 20, 40, 60, 80, 25, 35, 65]
print("\nPROSES INSERT:")
for k in data:
    tree.insert(k)

print("\n" + "="*50)
print("STRUKTUR BST YANG TERBENTUK:")
print("="*50)
print("          50")
print("        /    \\")
print("      30      70")
print("     /  \\    /  \\")
print("    20  40  60  80")
print("     \\   \\   \\")
print("     25  35  65")

print("\nINORDER TRAVERSAL (Data Terurut):")
tree.inorder(tree.root)

print("\n\n" + "="*50)
print("OPERASI BST:")
print("="*50)
print(f"Nilai minimum: {tree.min_value()}")
print(f"Nilai maksimum: {tree.max_value()}")

print("\nPENCARIAN:")
tree.search(40)
tree.search(100)
tree.search(25)

print("\n" + "="*50)
print("KOMPLEKSITAS BST:")
print("="*50)
print("Search/Average: O(log n)")
print("Search/Worst:   O(n) (jika tidak seimbang)")
print("Insert/Delete:  O(log n) rata-rata")