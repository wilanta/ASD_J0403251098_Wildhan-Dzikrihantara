# ========================================
# Implementasi Dijkstra
# ========================================

import heapq

graph = {
    "A": {"B": 4, "C": 2},
    "B": {"D": 5},
    "C": {"D": 1},
    "D": {},
}


def dijkstra(graph, start):
    # Menyimpan jarak minimum dari node awal ke setiap node.
    distances = {node: float("inf") for node in graph}

    # Jarak node awal ke dirinya sendiri adalah 0.
    distances[start] = 0

    # Priority queue menyimpan pasangan (jarak, node).
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # Jika jarak yang diproses lebih besar dari catatan terbaru,
        # lewati karena sudah ada jalur yang lebih pendek.
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga dari node saat ini.
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


hasil = dijkstra(graph, "A")
print(hasil)
