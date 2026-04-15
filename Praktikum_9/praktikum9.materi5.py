# =========================================================
# Latihan 4 : Membuat Traversal postorder
# =========================================================


# class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data  # menyimpan nilai node
        self.left = None  # child kiri
        self.right = None  # child kanan


# Membuat fungsi postorder: left -> right -> root
def postorder(node):
    if node is not None:
        postorder(node.left)  # 1. Kiri
        postorder(node.right)  # 2. Kanan
        print(node.data, end=" ")  # 3. Root


# Membuat tree
root = Node("A")

# Membuat child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

# Menampilkan isi kode
print("Hasil tranversal postorder:")
postorder(root)

# Penjelasan ---------------------------------------------
"""
Penjelasan terkait Traversal Postorder

Postorder adalah salah satu jenis traversal dengan urutan:
1. Left (subtree kiri)
2. Right (subtree kanan)
3. Root (akar)

def postorder(node):
Fungsi ini menggunakan konsep rekursif (fungsi memanggil dirinya sendiri).

if node is not None:
Digunakan untuk mengecek apakah node ada (tidak kosong). Jika None, maka tidak diproses.

postorder(node.left):
Memanggil fungsi postorder ke child kiri terlebih dahulu.

postorder(node.right):
Memanggil fungsi postorder ke child kanan setelah kiri selesai.

print(node.data):
Menampilkan data node terakhir (setelah kiri dan kanan selesai diproses).

Alur traversal pada tree di atas:
        A
       / \
      B   C
     / \
    D   E

Urutan postorder:
D → E → B → C → A

Traversal postorder selalu mengunjungi subtree kiri, kemudian subtree kanan, dan terakhir node itu sendiri.
"""
