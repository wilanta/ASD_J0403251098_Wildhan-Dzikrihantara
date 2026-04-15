# =========================================================
# Latihan 2 : Membuat binary tree sederhana
# =========================================================


# class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data  # menyimpan nilai node
        self.left = None  # child kiri
        self.right = None  # child kanan


# Membuat sebuah node root
root = Node("A")

# Membuat child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

# Menampilkan isi kode
print("Data pada root : ", root.data)
print("Data child kiri root :", root.left.data)
print("Data child kanan root : ", root.right.data)
print("Data child kiri dari B : ", root.left.left.data)
print("Data child kanan dari B : ", root.left.right.data)

# lanjutkan programnya untuk keseluruhan tree -> tambahkan child di sisi kanan C: F dan G
root.right.left = Node("F")
root.right.right = Node("G")

print("Data child kiri dari C : ", root.right.left.data)
print("Data child kanan dari C : ", root.right.right.data)

# Penjelasan --------------------------------------------
"""
Penjelasan Binary tree sederhana

Dalam program ini, dimasukan nilai "A" sebagai object yang mana akan menjadi root dalam program ini.

Kemudian dimasukan nilai "B" sebagai left child dari root "A" dan nilai "C" sebagai right child dari root "A".

Node "B" memiliki child "D" sebagai left child dan child "E" sebagai right child 

Siblings Node "B" yaitu Node "C" memiliki child "F" sebagai left child dan child "G" sebagai right child 

Untuk tampilan dalam bentuk treenya seperti ini
    A               root; parent dari B dan C
   /  \
  B    C            inner; parent dari D dan E untuk B | F dan G untuk C; child dari A
 / \  / \
D  E  F  G          Leaf; Child dari parent B dan C
"""
