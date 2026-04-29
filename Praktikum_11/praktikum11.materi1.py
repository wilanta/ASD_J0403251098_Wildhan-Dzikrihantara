# ========================================
# Implementasi dasar graph BST
# ========================================

# struktur data untuk membuat antrean, kita gunakan dari lib collection bawaan python
from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"],
}

# # cara akses
# for node in graph:
#     print(node, " -> ", graph[node])


def bfs(graph, start):
    # Fungsi untuk melakukan penelusuran graph dengan BFS
    # graph : dict yang menyimpan struktur dari graph
    # start : node awal penelusuran

    # Queue digunakan untuk menyimpan node yang akan diproses
    queue = deque()

    # Variable untuk menyimpan node yg sudah diproses/dibaca
    visited = set()

    # Masukan node awal ke queue
    queue.append(start)

    # Tandai node awal sebagai node yang sudah dikunjungi
    visited.add(start)

    while queue:
        # Mengambil node paling depan queue
        node = queue.popleft()

        print(node, end=" ")

        # Periksa semua tetangga dari node yang diambil
        for neighbor in graph[node]:
            # jika neighbor belum dikunjungi
            if neighbor not in visited:
                # tandai sebagai sudah dikunjungi
                visited.add(neighbor)
                # tambahkan ke tetangga ke queue untuk diproses nanti
                queue.append(neighbor)


# menjalankan BFS dari node A
bfs(graph, "A")
