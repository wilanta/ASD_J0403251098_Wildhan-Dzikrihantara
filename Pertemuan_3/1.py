"""
===============================
Latihan 1

Wildhan Dzikrihantara
J0403251098
===============================
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None # Tambahkan pointer tail
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head: # Jika linked list kosong
            self.head = new_node
            self.tail = new_node # Tail juga menunjuk ke node pertama
        else:
            self.tail.next = new_node # Sambungkan tail ke node baru
            self.tail = new_node # Update tail ke node baru
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")
        
    # Fungsi delete_node menghapus node berdasarkan value node tersebut
    def	delete_node(self, key):
        temp	=	self.head
        if temp and temp.data == key:
            self.head =	temp.next
            temp = None
            return
        prev = None
        while temp and temp.data !=	key:
            prev = temp
            temp = temp.next
        if temp is	None:
            return
        prev.next = temp.next
        temp = None
        
# Contoh Penggunaan
ll = LinkedList()
ll.insert_at_end(3)
ll.insert_at_end(5)
ll.insert_at_end(13)
ll.insert_at_end(2)
print("Sebelum didelete")
ll.display() # output : 3 -> 5 -> 13 -> 2 -> null
ll.delete_node(2) # Contoh Penggunaan delete_node, 2 dihapus dari linked
ll.delete_node(3) # Contoh Penggunaan delete_node, 3 dihapus dari 
print("Sesudah key 2 dan 3 didelete")
ll.display() # output : 5 -> 13 -> null