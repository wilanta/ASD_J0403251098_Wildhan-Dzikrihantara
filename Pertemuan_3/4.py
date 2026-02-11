"""
===============================
Latihan 4

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
       
    # Function insert node dengan banyak value atau single value
    def insert_node(self, data):
        # Inisialisasi dan assign value dengan mengecek banyak value terlebih dahulu agar tipenya tepat
        data_set = None
       
        # Mengecek banyaknya key/value agar bisa disesuaikan untuk dimasukan ke nodes
        if len(data) == 1:
            data_set = data
        elif len(data) > 1:
            data_set = data.split(",")
        else:
            return
               
        # Insert values ke nodes
        if data_set is not None:
            for data_insert in data_set:
                new_node = Node(data_insert)
                if  not self.head:  # Jika linked list kosong
                    self.head = new_node
                    self.tail = new_node
                else:
                    self.tail.next  =   new_node # Sambungkan tail ke node baru
                    self.tail   =   new_node # Update tail ke node baru
        else:
            new_node = Node(data_set)
            if  not self.head:  # Jika linked list kosong
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next  =   new_node # Sambungkan tail ke node baru
                self.tail   =   new_node # Update tail ke node baru
   
    # Menampilkan nodes
    def display(self):
        result = ""
        temp = self.head
        while temp:
            result += str(temp.data) + " -> "
            temp = temp.next
        result += "null"
        
        # Jika kosong maka return string "kosong"
        if result == "null":
            return "kosong"
        
        return result
       
    # Fungsi untuk menyatukan
    def concat(self, other_list):
        # Jika list 1 kosong maka return list 2
        if not self.head:
            self.head = other_list.head
            self.tail = other_list.tail
            return self

        # Jika list 2 kosong maka tidak perlu apa-apa
        if not other_list.head:
            return self

        # Sambungkan tail list 1 ke head list 2
        self.tail.next = other_list.head
        self.tail = other_list.tail

        return self

# Latihan 3
ll1 = LinkedList()
ll2 = LinkedList()

# Insert node list 1
insert_values = input("Masukan elemen untuk Linked List 1 (pisahkan setiap elemen dengan koma ',') : ")
ll1.insert_node(insert_values)

# Insert node list 2
insert_values = input("Masukan elemen untuk Linked List 2 (pisahkan setiap elemen dengan koma ',') : ")
ll2.insert_node(insert_values)

# Menampilkan Hasil
result_list1 = ll1.display()
result_list2 = ll2.display()
result_concat = ll1.concat(ll2).display()

list1 = f"Linked List 1 : {result_list1}"
list2 = f"Linked List 2 : {result_list2}"
concat = f"Linked List setelah digabungkan : {result_concat}"
print(f"\n{list1}\n{list2}\n{concat}")