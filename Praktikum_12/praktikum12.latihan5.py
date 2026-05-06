# Nama : Wildhan Dzikrihantara
# NIM :  J0403251098
# Kelas : B1
# Praktikum 12 - Graph II: Shortest Path

import heapq

# Graph lokasi kampus.
# Bobot menunjukkan waktu tempuh dalam menit.
graph = {
    "Bogor": {"Jakarta": 5, "Depok": 2},
    "Depok": {"Jakarta": 2, "Bandung": 6},
    "Jakarta": {"Bandung": 7},
    "Bandung": {},
}


# Algoritma Dijkstra untuk mencari jarak terpendek dari node awal ke semua node lainnya.
def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    # Selama masih ada node yang belum diproses, ambil node dengan jarak terpendek.
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


hasil = dijkstra(graph, "Bogor")

print("Jarak dari Bogor ke semua kota:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")

"""
Pertanyaan Analitis :
1. Node awal yang digunakan apa?
2. Node mana yang memiliki jarak paling kecil dari node awal?
3. Node mana yang memiliki jarak paling besar dari node awal?
4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.
"""


"""
Jawaban :
1. Node awal yang digunakan adalah "Bogor".
2. Node yang memiliki jarak paling kecil dari node awal "Bogor" adalah "Depok" dengan jarak 2 menit.
3. Node yang memiliki jarak paling besar dari node awal "Bogor" adalah "Bandung" dengan jarak 7 menit.
4. Algoritma Dijkstra bekerja dengan memulai dari node awal (dalam kasus ini "Bogor") dan menginisialisasi jarak ke semua node lain sebagai tak hingga, kecuali node awal yang diinisialisasi dengan jarak 0. Algoritma kemudian menggunakan antrian prioritas untuk memproses node dengan jarak terpendek terlebih dahulu. Setiap kali sebuah node diproses, algoritma memperbarui jarak ke tetangganya jika ditemukan jalur yang lebih pendek melalui node tersebut. Proses ini berlanjut hingga semua node telah diproses, menghasilkan jarak terpendek dari node awal ke semua node lainnya dalam graph.
"""
