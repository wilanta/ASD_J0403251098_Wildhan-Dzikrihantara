# =========================================================
# Nama : Wildhan Dzikrihantara
# NIM : J0403251098
# =========================================================

# ==========================================================
# Latihan 5: Rotasi Kiri pada BST Tidak Seimbang
# ==========================================================

# Class Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Fungsi preorder untuk melihat isi tree
def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


# Fungsi untuk menampilkan struktur tree
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print(" " * level + f"{posisi}: {root.data}")
        tampil_struktur(root.left, level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")


# Fungsi rotasi kiri
def rotate_left(x):
    """
    Alur fungsi rotate_left pada BST
    1. Identifikasi node x yang akan dirotasi (root dari subtree yang tidak seimbang).
    2. Simpan node y (child kanan x) dan subtree T2 (child kiri y) untuk sementara.
    3. Lakukan rotasi dengan menjadikan y sebagai root baru, x sebagai child kiri y, dan T2 sebagai child kanan x.
    4. Kembalikan node y sebagai root baru dari subtree yang sudah dirotasi.
    """

    # x adalah root lama
    y = x.right  # y adalah child kanan x
    T2 = y.left  # subtree kiri milik y disimpan sementara

    # Proses rotasi
    y.left = x  # x menjadi child kiri dari y
    x.right = T2  # child kanan x diganti dengan T2

    # y menjadi root baru
    return y


# -----------------------------
# Program utama
# -----------------------------
# Membuat tree yang tidak seimbang:
# 10 -> 20 -> 30
root = Node(10)
root.right = Node(20)
root.right.right = Node(30)

print("Preorder sebelum rotasi kiri:")
preorder(root)

print("\n\nStruktur sebelum rotasi kiri:")
tampil_struktur(root)

# Melakukan rotasi kiri pada root
root = rotate_left(root)

print("\nPreorder sesudah rotasi kiri:")
preorder(root)

print("\n\nStruktur sesudah rotasi kiri:")
tampil_struktur(root)
