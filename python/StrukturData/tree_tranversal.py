class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Traversal Inorder (Left, Root, Right)
def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end=' ')
        inorder(node.right)

# Traversal Preorder (Root, Left, Right)
def preorder(node):
    if node:
        print(node.value, end=' ')
        preorder(node.left)
        preorder(node.right)

# Traversal Postorder (Left, Right, Root)
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end=' ')

# Membuat tree sesuai struktur
'''
     A   
    / \
   B   C
  / \
 D   E
'''
root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')

# Menampilkan hasil traversal
print("Inorder:", end=' ')
inorder(root)
print("\nPreorder:", end=' ')
preorder(root)
print("\nPostorder:", end=' ')
postorder(root)
