"""
BINARY TREE (POHON BINER) DAN TRAVERSAL
Binary Tree: struktur data hierarkis di mana setiap node maksimal memiliki 2 child
"""

class Node:
    """Node untuk Binary Tree"""
    def __init__(self, data):
        self.data = data
        self.kiri = None   # Left child
        self.kanan = None  # Right child

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def preorder(self, node):
        """Preorder Traversal: Root → Kiri → Kanan"""
        if node:
            print(node.data, end=' ')
            self.preorder(node.kiri)
            self.preorder(node.kanan)
    
    def inorder(self, node):
        """Inorder Traversal: Kiri → Root → Kanan"""
        if node:
            self.inorder(node.kiri)
            print(node.data, end=' ')
            self.inorder(node.kanan)
    
    def postorder(self, node):
        """Postorder Traversal: Kiri → Kanan → Root"""
        if node:
            self.postorder(node.kiri)
            self.postorder(node.kanan)
            print(node.data, end=' ')
    
    def level_order(self, node):
        """Level Order Traversal (BFS untuk tree)"""
        if not node:
            return
        queue = [node]
        while queue:
            current = queue.pop(0)
            print(current.data, end=' ')
            if current.kiri:
                queue.append(current.kiri)
            if current.kanan:
                queue.append(current.kanan)

# Membangun tree
# Struktur tree:
#         A
#        / \
#       B   C
#      / \   \
#     D   E   F
#        /
#       G

tree = BinaryTree()
tree.root = Node('A')
tree.root.kiri = Node('B')
tree.root.kanan = Node('C')
tree.root.kiri.kiri = Node('D')
tree.root.kiri.kanan = Node('E')
tree.root.kanan.kanan = Node('F')
tree.root.kiri.kanan.kiri = Node('G')  

print("="*50)
print("BINARY TREE TRAVERSAL")
print("="*50)
print("Struktur Tree:")
print("        A")
print("       / \\")
print("      B   C")
print("     / \\   \\")
print("    D   E   F")
print("       /")
print("      G")
print()

print("1. Preorder Traversal (Root → Kiri → Kanan):")
tree.preorder(tree.root)
print("\n   Kegunaan: Membuat salinan tree, prefix expression")

print("\n\n2. Inorder Traversal (Kiri → Root → Kanan):")
tree.inorder(tree.root)
print("\n   Kegunaan: Mendapatkan data terurut (pada BST)")

print("\n\n3. Postorder Traversal (Kiri → Kanan → Root):")
tree.postorder(tree.root)
print("\n   Kegunaan: Menghapus tree, postfix expression")

print("\n\n4. Level Order Traversal (BFS):")
tree.level_order(tree.root)
print("\n   Kegunaan: Mencari node terdekat, tree level")
print()