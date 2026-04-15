# =========================================================
# Latihan 6 : Membuat stuktur organisasi perusahaan
# =========================================================


# class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data  # menyimpan nilai node
        self.left = None  # child kiri
        self.right = None  # child kanan


# Fungsi preorder: root -> right -> left
def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)


# Membuat tree struktur organisasi
root = Node("Direktur")

# Child level 1
root.left = Node("Manajer A")
root.right = Node("Manajer B")

# Child level 2
root.left.left = Node("Staff1")
root.left.right = Node("Staff2")

root.right.right = Node("Staff3")

# Menjalankan tranversal preorder
print("Struktur organisasi (preorder): ")
preorder(root)

# Penjelasan ---------------------------------------------
# =========================================================
# Latihan 6 : Membuat stuktur organisasi perusahaan
# =========================================================


# class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data  # menyimpan nilai node
        self.left = None  # child kiri
        self.right = None  # child kanan


# Fungsi preorder: root -> left -> right
def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)


# Membuat tree struktur organisasi
root = Node("Direktur")

# Child level 1
root.left = Node("Manajer A")
root.right = Node("Manajer B")

# Child level 2
root.left.left = Node("Staff1")
root.left.right = Node("Staff2")

root.right.right = Node("Staff3")

# Menjalankan tranversal preorder
print("Struktur organisasi (preorder): ")
preorder(root)

# Penjelasan ---------------------------------------------
"""
Penjelasan terkait Struktur Organisasi dengan Tree

Tree dapat digunakan untuk merepresentasikan struktur organisasi karena memiliki hubungan hierarki (atas ke bawah).

Setiap node merepresentasikan jabatan:
- Root (akar) = posisi tertinggi (Direktur)
- Child = bawahan dari node tersebut

Struktur tree di atas:
            Direktur
           /         \
     Manajer A     Manajer B
      /     \            \
   Staff1  Staff2      Staff3

def preorder(node):
Traversal yang digunakan adalah preorder dengan urutan:
1. Root (node saat ini)
2. Left (subtree kiri)
3. Right (subtree kanan)

Fungsi ini menggunakan rekursi untuk mengunjungi semua node.

print(node.data):
Menampilkan jabatan terlebih dahulu (atas ke bawah).

preorder(node.left):
Mengunjungi bawahan di sisi kiri.

preorder(node.right):
Mengunjungi bawahan di sisi kanan.

Urutan hasil preorder:
Direktur → Manajer A → Staff1 → Staff2 → Manajer B → Staff3

Tree sangat cocok untuk merepresentasikan struktur organisasi karena menggambarkan hubungan atasan dan bawahan secara jelas.
Traversal preorder membantu menampilkan struktur dari atas ke bawah secara berurutan.
"""
