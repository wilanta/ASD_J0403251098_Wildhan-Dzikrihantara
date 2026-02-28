"""
=========================================================================
Nama : Wildhan Dzikrihantara
NIM : J0403251098
Kelas : TPL B1
=========================================================================
"""

# ==========================================
# Studi Kasus: Sistem Antrian Layanan Akademik
# Implementasi Queue ->
# Stack ==> Front -> C -> B -> A -> Rear
# Queue ==> Front -> A -> B -> C -> Rear
# Enqueue: Memindahkan pointer rear
# Dequeue: Memindahkan pointer front
# ==========================================


# 1) Mendefinisikan Node (Unit dasr linked list)
class Node:
    def __init__(self, nim, nama):
        self.nim = nim  # menyimpan NIM mahasiswa
        self.nama = nama  # menyimpan Nama mahasiswa
        self.next = None


# 2) Mendefiniskan queue
class queueAkademik:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        # Ketika queue kosong maka front = rear = none
        return self.front is None

    # Menambahkan data baru ke bagian belakang (rear) => menambahkan antrian mahasiswa yang akan mengajukan layanan akademik
    def enqueue(self, nim, nama):
        nodeBaru = Node(nim, nama)

        # Jika data baru masuk dari queue yang kosong maka data baru = rear
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return

        # Jika queue tidak kosong, maka data baru diletakan setelah rear kemudian dijadikan sebagai rear
        self.rear.next = nodeBaru
        self.rear = nodeBaru

    # menghapus node data paling depan (memberikan layanan akademik)
    def dequeue(self):

        if self.is_empty():
            print("Antrean kosong, Tidak ada mahasiswa yang dilayani")
            return None

        # lihat data bagian front, simpan di variable data yang akan diinput (dilayani)
        node_dilayani = self.front

        # geser pointer front ke next front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return node_dilayani

    def tampilan(self):
        print("Daftar Antrean Mahasiswa (front -> rear) : ")
        current = self.front
        no = 1
        while current is not None:
            print(f"{no}, {current.nim}, {current.nama}")
            current = current.next
            no += 1


def main():
    # instansiasi
    q = queueAkademik()

    while True:
        print("========= Sistem Antrean =========")
        print("1. Tambah Mahasiswa")
        print("2. Layani Mahasiswa")
        print("3. Lihat Mahasiswa")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4) :").strip()

        if pilihan == "1":
            nim = input("Masukan NIM : ").strip()
            nama = input("Masukan Nama : ").strip()

            q.enqueue(nim, nama)
            print("mahasiswa berhasil ditambahkan")
        elif pilihan == "2":
            dilayani = q.dequeue()
            print(f"Masukan dilayani : {dilayani.nim} - {dilayani.nama}")
        elif pilihan == "3":
            q.tampilan()
        elif pilihan == "4":
            print("program selesai")
            break
        else:
            print("Piihan tidak valid, silakan coba 1-4")


if __name__ == "__main__":
    main()
