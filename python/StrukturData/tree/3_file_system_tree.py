"""
TREE SEBAGAI REPRESENTASI FILE SYSTEM
Simulasi struktur folder dan file menggunakan tree
"""

class FileNode:
    def __init__(self, name, is_folder):
        self.name = name
        self.is_folder = is_folder
        self.children = []
        self.size = 0 if is_folder else 1  # Simulasi ukuran file
    
    def add_child(self, node):
        """Menambahkan child node (hanya untuk folder)"""
        if self.is_folder:
            self.children.append(node)
            print(f"  📁 {self.name} → Menambahkan: {node.name}")
        else:
            print(f"Error: {self.name} adalah file, tidak bisa memiliki children")
    
    def print_tree(self, level=0, prefix=""):
        """Mencetak struktur tree dengan indentasi"""
        if level == 0:
            print("📁 " + self.name)
        else:
            print("  " * (level-1) + prefix + "📁 " + self.name if self.is_folder else prefix + "📄 " + self.name)
        
        for i, child in enumerate(self.children):
            is_last = (i == len(self.children) - 1)
            new_prefix = "  " * level + ("└── " if is_last else "├── ")
            child.print_tree(level + 1, new_prefix)
    
    def get_total_files(self):
        """Menghitung total file dalam tree"""
        if not self.is_folder:
            return 1
        return sum(child.get_total_files() for child in self.children)
    
    def get_total_size(self):
        """Menghitung total ukuran (simulasi)"""
        if not self.is_folder:
            return self.size
        return sum(child.get_total_size() for child in self.children)

# Membangun struktur folder
print("="*50)
print("MEMBANGUN STRUKTUR FILE SYSTEM")
print("="*50)

root = FileNode("root", True)

# Membuat folder
folder1 = FileNode("Documents", True)
folder2 = FileNode("Downloads", True)
folder3 = FileNode("Projects", True)
folder4 = FileNode("Images", True)
folder5 = FileNode("Python", True)

# Membuat file
file1 = FileNode("resume.pdf", False)
file2 = FileNode("notes.txt", False)
file3 = FileNode("setup.exe", False)
file4 = FileNode("photo.jpg", False)
file5 = FileNode("script.py", False)
file6 = FileNode("data.csv", False)
file7 = FileNode("logo.png", False)
file8 = FileNode("main.py", False)
file9 = FileNode("utils.py", False)

print("\nPROSES PEMBUATAN STRUKTUR:")
print("-"*40)

# Menyusun struktur
root.add_child(folder1)      # root/Documents
root.add_child(folder2)      # root/Downloads
root.add_child(folder3)      # root/Projects

folder1.add_child(file1)     # Documents/resume.pdf
folder1.add_child(file2)     # Documents/notes.txt
folder1.add_child(folder4)   # Documents/Images

folder4.add_child(file4)     # Images/photo.jpg
folder4.add_child(file7)     # Images/logo.png

folder2.add_child(file3)     # Downloads/setup.exe

folder3.add_child(folder5)   # Projects/Python
folder3.add_child(file6)     # Projects/data.csv

folder5.add_child(file8)     # Python/main.py
folder5.add_child(file9)     # Python/utils.py

# Menampilkan struktur
print("\n" + "="*50)
print("STRUKTUR FILE SYSTEM:")
print("="*50)
root.print_tree()

# Informasi statistik
print("\n" + "="*50)
print("STATISTIK:")
print("="*50)
print(f"Total file: {root.get_total_files()} file")
print(f"Total ukuran (simulasi): {root.get_total_size()} unit")

print("\n" + "="*50)
print("KEUNTUNGAN MENGGUNAKAN TREE UNTUK FILE SYSTEM:")
print("="*50)
print("1. Representasi hierarki yang natural")
print("2. Mudah melakukan traversal (navigasi folder)")
print("3. Efisien untuk operasi seperti mencari file")
print("4. Mendukung operasi rekursif (copy, delete, move)")