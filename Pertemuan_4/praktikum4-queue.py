# ================================================================================
# Nama      : Wildhan Dzikrihantara
# NIM       : J0403251098
# Kelas     : TPL B1
# ================================================================================

# ================================================================================
# Implementasi Dasar : Queue Berbasis Linked List
# ================================================================================

# Membuat class Node (merupakan unit dasar dari Linked List)
class Node:
    def __init__(self, data): # Constructor
        self.data = data # Untuk menyimpan value
        self.next = None # pointer ke node berikutnya (awal -> None/Null)
        
# Queue dengan 2 pointer : front dan rear
class QueueLL:
    def __init__(self):
        self.front = None # Node paling depan
        self.rear = None # Node paling belakang
        
    def enqueue(self, data):
        nodeBaru = Node(data)
        
        # Jika queue kosong, 
        if self.front is None:
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        
        # Jika queue tidak kosong
        
        # Rear lama menunjuk ke node baru
        self.rear.next = nodeBaru
        
        # Rear pindah ke node baru
        self.rear = nodeBaru
        
    # Menghapus data dari depan
    def dequeue(self):
        # 1) Ambil data paling depan
        data_terhapus = self.front.data
        
        # 2) Geser front ke node berikutnya
        self.front = self.front.next
        
        # 3) Jika setelah geser front menjadi None, maka queue kosong, rear juga harus none
        if self.front is None:
            self.rear = None
        
        return data_terhapus
        
    def tampilkan(self):
        # Menampilkan isi queue dari front ke rear
        current = self.front
        print("Front", end=" -> ")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None - Rear di terakhir")

# Instantiasi objek class QueueLL
q = QueueLL()

q.enqueue("A")
q.enqueue("B")
q.enqueue("C")

q.dequeue()

q.tampilkan()