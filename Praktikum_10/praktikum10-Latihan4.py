# =========================================================
# Nama : Wildhan Dzikrihantara
# NIM : J0403251098
# =========================================================

# ==========================================================
# Latihan 6: Rotasi Kanan pada BST Tidak Seimbang
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
def rotate_right(x):
    """
    Alur fungsi rotate_right pada BST
    1. Identifikasi node x yang akan dirotasi (root dari subtree yang tidak seimbang).
    2. Simpan node y (child kiri x) dan subtree T2 (child kanan y) untuk sementara.
    3. Lakukan rotasi dengan menjadikan y sebagai root baru, x sebagai child kanan y, dan T2 sebagai child kiri x.
    4. Kembalikan node y sebagai root baru dari subtree yang sudah dirotasi.
    """

    y = x.left  # child kiri jadi root baru
    T2 = y.right  # subtree kanan y disimpan

    # Proses rotasi
    y.right = x  # x jadi child kanan
    x.left = T2  # subtree dipindahkan

    return y


# -----------------------------
# Program utama
# -----------------------------
# Membuat tree yang tidak seimbang:
# 30 -> 20 -> 10
root = Node(30)
root.left = Node(20)
root.left.left = Node(10)

print("Preorder sebelum rotasi kiri:")
preorder(root)

print("\n\nStruktur sebelum rotasi kiri:")
tampil_struktur(root)

# Melakukan rotasi kiri pada root
root = rotate_right(root)

print("\nPreorder sesudah rotasi kiri:")
preorder(root)

print("\n\nStruktur sesudah rotasi kiri:")
tampil_struktur(root)
