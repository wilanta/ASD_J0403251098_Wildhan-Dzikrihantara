# =========================================================
# Latihan 4 : Membuat Traversal inorder
# =========================================================


# class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data  # menyimpan nilai node
        self.left = None  # child kiri
        self.right = None  # child kanan


# Membuat fungsi inorder: left -> root -> right
def inorder(node):
    if node is not None:
        inorder(node.left)  # 1. Kiri
        print(node.data, end=" ")  # 2. Root
        inorder(node.right)  # 3. Kanan


# Membuat tree
root = Node("A")

# Membuat child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

# Menampilkan isi kode
print("Hasil tranversal inorder:")
inorder(root)

# Penjelasan ---------------------------------------------
"""
Penjelasan terkait Traversal Inorder

Inorder adalah salah satu jenis traversal dengan urutan:
1. Left (subtree kiri)
2. Root (akar)
3. Right (subtree kanan)

def inorder(node):
Fungsi ini menggunakan konsep rekursif (fungsi memanggil dirinya sendiri).

if node is not None:
Digunakan untuk mengecek apakah node ada (tidak kosong). Jika None, maka tidak diproses.

inorder(node.left):
Memanggil fungsi inorder ke child kiri terlebih dahulu.

print(node.data):
Menampilkan data node setelah subtree kiri selesai diproses.

inorder(node.right):
Memanggil fungsi inorder ke child kanan.

Alur traversal pada tree di atas:
        A
       / \
      B   C
     / \
    D   E

Urutan inorder:
D → B → E → A → C

Kesimpulan:
Traversal inorder selalu mengunjungi subtree kiri dulu, kemudian node sekarang, lalu subtree kanan.
"""
