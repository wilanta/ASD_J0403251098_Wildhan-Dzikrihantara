"""
===============================
Latihan 2

Wildhan Dzikrihantara
J0403251098
===============================
"""

class Node:
    def	__init__(self,	data):
        self.data	=	data
        self.next	=	None

class CircularSinglyLinkedList:
    def	__init__(self):
        self.head	=	None
        self.tail	=	None # Tambahkan pointer tail
    
    # Function insert node dengan banyak value atau single value
    def insert_node(self, data):
        # Inisialisasi dan assign value dengan mengecek banyak value terlebih dahulu agar tipenya tepat
        data_set = None
        
        if len(data) == 1:
            data_set = data
        elif len(data) > 1:
            data_set = data.split(",")
                
        # Insert values ke nodes
        if data_set is not None:
            for data_insert in data_set:
                new_node = Node(data_insert)
                if	not	self.head:	# Jika linked list kosong
                    self.head =	new_node
                    self.tail =	new_node
                    self.tail.next = self.head # Circular link ke dirinya sendiri
                else:
                    self.tail.next	=	new_node # Sambungkan tail ke node baru
                    self.tail	=	new_node # Update tail ke node baru
                    self.tail.next	=	self.head # Circular link kembali ke 
        else:
            new_node = Node(data_set)
            if	not	self.head:	# Jika linked list kosong
                self.head =	new_node
                self.tail =	new_node
                self.tail.next = self.head # Circular link ke dirinya sendiri
            else:
                self.tail.next	=	new_node # Sambungkan tail ke node baru
                self.tail	=	new_node # Update tail ke node baru
                self.tail.next	=	self.head # Circular link kembali ke 
        
    def search_key(self, key):
        if self.head.data is None:
            print("Circular Linked List kosong, tidak ada elemen yang bisa dicari")
            return

        temp = self.head
        while True:
            if temp.data == key:
                print(f"Elemen {key} ditemukan dalam Circular Linked List")
                return
            temp = temp.next
            if temp == self.head:
                break

        print(f"Elemen {key} tidak ditemukan dalam Circular Linked List")


    
    def	display(self):
        if	not	self.head:
            print("List	is	empty")
            return

        temp = self.head
        print(temp.data, end=" -> ")
        temp = temp.next
        while temp != self.head:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("...	(back	to	head)")

# Penerapan Latihan 2
cll	= CircularSinglyLinkedList()

# Insert value/values
insert_values = input("Masukan elemen ke dalam Circular Linked List (pisahkan setiap elemen dengan koma ',') : ")
cll.insert_node(insert_values)

# Search key
search_val = input("\nMasukan elemen yang ingin dicari : ")
cll.search_key(search_val)