# ================================================================================
# Nama      : Wildhan Dzikrihantara
# NIM       : J0403251098
# Kelas     : TPL B1
# ================================================================================

# ================================================================================
# Implementasi Dasar : Node pada Linked List
# ================================================================================

# Membuat class Node (merupakan unit dasar dari Linked List)
class Node:
    def __init__(self, data): # Constructor
        self.data = data # Untuk menyimpan value
        self.next = None # pointer ke node berikutnya (awal -> None/Null)
         
# 1) Membuat node satu per satu
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

# 2) Menghubungkan Node : A -> B -> C -> None
nodeA.next = nodeB
nodeB.next = nodeC

# 3) Menentukan node pertama (head)
head = nodeA

# 4) Traversal : menelusuri dari head sampai tail/rear (none)
current = head
while current is not None:
    print(current.data) # menampilkan data ke node saat ini
    current = current.next # pindah ke node berikutnya
    
"""
=======================================================================================
Implementasi Dasar : Linked List + Insert Awal (Stack)
=======================================================================================
"""

class LinkedList: # class implementasi stack
    def __init__(self):
        self.head = None # awalnya kosong
        
        
    def insert_awal(self, data): # Push dalam stack
        # 1) Buat node baru
        nodeBaru = Node(data) # panggil class node
        
        # 2) node baru menunjuk ke head lama
        nodeBaru.next = self.head
        
        # 3) head pindah ke node baru
        self.head = nodeBaru
        
    def hapus_awal(self): # Pop dalam stack
        data_terhapus = self.head.data # peek dalam stak (melihat data yang paling depan/melihat head)
        
        # Menggeser head ke node berikutnya
        self.head = self.head.next
        print("Node yang dihapus : ", data_terhapus)
        
    def tampilkan_node(self): # Implementasi traversal
        current = self.head
        while current is not None:
            print(current.data) # menampilkan data ke node saat ini
            current = current.next # pindah ke node berikutnya
    
print("====== List Baru ======")
ll = LinkedList() # instantiasi objek ke class Linked List
ll.insert_awal("X") 
ll.insert_awal("Y") 
ll.insert_awal("Z") 
ll.hapus_awal()
ll.tampilkan_node()

"""
Pada Stack:
    Menumpuk/membahkan node -> push
    Menghapus node -> pop
"""