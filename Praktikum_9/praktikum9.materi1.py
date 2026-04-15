# =========================================================
# Latihan 1 : Membuat Node Tree
# =========================================================


# class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data  # menyimpan nilai node
        self.left = None  # child kiri
        self.right = None  # child kanan


# Membuat Root
root = Node("A")

# Mencetak isi node
print("Data pada root : ", root.data)
print("Child kiri root : ", root.left.data)
print("Child kanan root", root.right.data)

# Penjelasan ---------------------------------------------
"""
Penjelasan terkait Node Tree

Menggunakan struktur data linked list.

class Node:
Setiap node akan memiliki data (untuk menyimpan nilai yang dimasukan dari parameter), left (untuk child kiri dari data), dan right (untuk child kanan dari data). Karena itu node hanya menyimpan 1 nilai dan hanya dapat memiliki 2 child saja.
"""
