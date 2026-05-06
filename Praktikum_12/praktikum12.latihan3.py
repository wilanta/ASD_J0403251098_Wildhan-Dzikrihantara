# Nama : Wildhan Dzikrihantara
# NIM :  J0403251098
# Kelas : B1
# Praktikum 12 - Graph II: Shortest Path

# ========================================
# Latihan 3: Implementasi Bellman-Ford
# ========================================

# Weighted graph dengan bobot negatif.
graph = {
    "A": {"B": 5, "C": 4},
    "B": {},
    "C": {"B": -2},
}


def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Bellman-Ford.
    """
    # Semua jarak awal dibuat tak hingga.
    distances = {node: float("inf") for node in graph}

    # Jarak dari start ke start adalah 0.
    distances[start] = 0

    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1.
    for _ in range(len(graph) - 1):
        # Periksa semua edge.
        for node in graph:
            for neighbor, weight in graph[node].items():
                # Jika node saat ini sudah diketahui dan ditemukan jarak
                # yang lebih kecil ke neighbor, maka update jarak.
                if (
                    distances[node] != float("inf")
                    and distances[node] + weight < distances[neighbor]
                ):
                    distances[neighbor] = distances[node] + weight

    return distances


hasil = bellman_ford(graph, "A")

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

"""
Pertanyaan Analisis:
1. Berapa bobot langsung dari A ke B?
2. Berapa total bobot jalur A -> C -> B?
3. Jalur mana yang menghasilkan jarak lebih kecil menuju B?
4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
5. Apa yang dimaksud dengan proses relaksasi edge?
6. Apa perbedaan utama Bellman-Ford dan Dijkstra?
"""

"""
Jawaban :
1. Bobot langsung dari A ke B adalah 5.

2. Total bobot jalur A -> C -> B adalah 2, karena bobot A -> C = 4
   dan bobot C -> B = -2, sehingga 4 + (-2) = 2.

3. Jalur yang menghasilkan jarak lebih kecil menuju B adalah A -> C -> B.
   Jalur ini memiliki total bobot 2, lebih kecil daripada jalur langsung
   A -> B yang bobotnya 5.

4. Bellman-Ford dapat digunakan pada graph dengan bobot negatif karena
   algoritma ini melakukan relaksasi semua edge secara berulang. Dengan
   proses tersebut, jarak minimum tetap dapat diperbarui meskipun ada
   edge yang bernilai negatif.

5. Relaksasi edge adalah proses mengecek sebuah edge dan memperbarui
   jarak ke node tujuan jika ditemukan jalur baru dengan total bobot
   yang lebih kecil.

6. Perbedaan utama Bellman-Ford dan Dijkstra adalah Bellman-Ford dapat
   menangani bobot negatif, sedangkan Dijkstra tidak cocok untuk bobot
   negatif. Dijkstra biasanya lebih cepat, sedangkan Bellman-Ford lebih
   fleksibel untuk kasus graph tertentu.
"""
