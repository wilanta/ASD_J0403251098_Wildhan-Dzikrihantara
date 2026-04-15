# =========================================================
# Latihan 3 : Membuat Traversal Preorder
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


# Membuat tree
root = Node("A")

# Membuat child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

# Menampilkan isi kode
print("Hasil tranversal preorder:")
preorder(root)

# Penjelasan ---------------------------------------------
"""
Penjelasan terkait Traversal Preorder

Traversal adalah cara untuk mengunjungi semua node dalam tree.

Preorder adalah salah satu jenis traversal dengan urutan:
1. Root (akar)
2. Left (subtree kiri)
3. Right (subtree kanan)

def preorder(node):
Fungsi ini menggunakan konsep rekursif, yaitu fungsi memanggil dirinya sendiri.

if node is not None:
Digunakan untuk mengecek apakah node ada (tidak kosong). Jika None, maka tidak diproses.

print(node.data):
Menampilkan data dari node saat ini (root terlebih dahulu).

preorder(node.left):
Memanggil fungsi preorder ke child kiri.

preorder(node.right):
Memanggil fungsi preorder ke child kanan.

Alur traversal pada tree di atas:
        A
       / \
      B   C
     / \
    D   E

Urutan preorder:
A → B → D → E → C

Traversal preorder selalu mengunjungi node sekarang dulu, lalu ke kiri, lalu ke kanan.
"""
