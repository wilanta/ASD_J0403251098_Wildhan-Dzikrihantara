# =========================================================
# Nama : Wildhan Dzikrihantara
# NIM : J0403251098
# =========================================================

# =========================================================
# Latihan 1 : Membuat Node Tree
# =========================================================


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# ALur fungsi insert pada BST


def insert(root, data):
    """
    Alur fungsi insert pada BST
    1. Jika root kosong, buat node baru dengan data dan kembalikan node tersebut.
    2. Jika data yang akan dimasukkan lebih kecil dari data root, rekursif ke subtree kiri.
    3. Jika data yang akan dimasukkan lebih besar dari data root, rekursif ke subtree kanan.
    4. Kembalikan root setelah penempatan data.
    """

    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root:
        root.right = insert(root.right, data)

    return root


# Mengisi data BST
root = None
data_list = [50, 30, 70, 20, 40, 50, 80]

for data in data_list:
    root = insert(root, data)

print("BST berhasil dibuat")


# =========================================================
# Latihan 2 : Traversal Inorder
# =========================================================
def inorder(node):
    """
    Alur fungsi inorder pada BST
    1. Kunjungi subtree kiri terlebih dahulu (rekursif).
    2. Setelah itu, proses node root (tampilkan data).
    3. Terakhir, kunjungi subtree kanan (rekursif).

    Traversal inorder menghasilkan data dalam urutan menaik (sorted order) untuk BST.
    """
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)


print("Hasil Inorder: ")
inorder(root)


# =========================================================
# Latihan 3 : Search di BST
# =========================================================
def search(root, key):
    """
    Alur fungsi search pada BST
    1. Jika root kosong, kembalikan False (data tidak ditemukan).
    2. Jika data root sama dengan key yang dicari, kembalikan True (data ditemukan).
    3. Jika key lebih kecil dari data root, rekursif ke subtree kiri.
    4. Jika key lebih besar dari data root, rekursif ke subtree kanan.
    5. Kembalikan hasil pencarian dari subtree yang sesuai.
    """

    if root is None:
        return False

    if root.data == key:
        return True
    elif key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)


# Uji Pencarian
key = 40
if search(root, key):
    print("Data ditemukan!")
else:
    print("Data tidak ditemukan")
