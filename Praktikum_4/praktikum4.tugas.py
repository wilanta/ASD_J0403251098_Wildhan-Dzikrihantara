"""
=========================================================================
Nama : Wildhan Dzikrihantara
NIM : J0403251098
Kelas : TPL B1
=========================================================================
"""


# ==========================================================
# Tugas Hands-On: Sistem Antrian Bengkel Motor
# ==========================================================
class Node:
    def __init__(self, no, nama, servis):
        self.no = no
        self.nama = nama
        self.servis = servis
        self.next = None


class QueueBengkel:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, no, nama, servis):
        # TODO: Tambahkan data ke antrian
        nodeBaru = Node(no, nama, servis)

        # Jika data baru masuk dari queue yang kosong maka data baru = rear
        if self.front is None:
            self.front = nodeBaru
            self.rear = nodeBaru
            return

        # Jika queue tidak kosong, maka data baru diletakan setelah rear kemudian dijadikan sebagai rear
        self.rear.next = nodeBaru
        self.rear = nodeBaru

    def dequeue(self):
        # TODO: Layani pelanggan terdepan
        if self.front is None:
            print("Antrean kosong, Tidak ada motor yang dilayani")
            return None

        # lihat data bagian front, simpan di variable data yang akan diinput (dilayani)
        node_dilayani = self.front

        # geser pointer front ke next front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return node_dilayani

    def tampilkan(self):
        # TODO: Tampilkan seluruh antrian
        print("Daftar Antrean Service Motor (front -> rear) : ")
        current = self.front

        while current is not None:
            print(f"{current.no}, {current.nama}, {current.servis}")
            current = current.next


def main():
    q = QueueBengkel()

    while True:
        print("\n=== Sistem Antrian Bengkel ===")
        print("1. Tambah Pelanggan")
        print("2. Layani Pelanggan")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            no = input("No Antrian : ")
            nama = input("Nama : ")
            servis = input("Servis : ")
            q.enqueue(no, nama, servis)
        elif pilih == "2":
            dilayani = q.dequeue()
            print(f"Antrian {dilayani.no} atas nama {dilayani.nama} dilayani!")
        elif pilih == "3":
            q.tampilkan()
        elif pilih == "4":
            break
        else:
            print("Pilihan tidak valid")


if __name__ == "__main__":
    main()
