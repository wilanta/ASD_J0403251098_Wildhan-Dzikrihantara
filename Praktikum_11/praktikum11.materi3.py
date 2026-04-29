# ========================================
# Implementasi DST
# ========================================

# struktur data untuk membuat antrean, kita gunakan dari lib collection bawaan python
from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"],
}


def dfs(graph, node, visited):
    # fungsi untuk melakukan penelusuran graph menggunakan DST
    # graph : dict yang menyimpan graph
    # node : menyimpan node yang sedang dikunjungi
    # visited : menyimpan node yang sudah dikunjungi

    # tandai node saat ini sebagai node yg sudah dikunjugi
    visited.add(node)

    # tampilkan node saat ini
    print(node, end=" ")

    # periksa semua tetangga dari node saat ini
    for neighbor in graph[node]:
        # jika tetangga belum dikunjungi
        if neighbor not in visited:
            # lakukan dfs secara rekursif ke tetangga tersebut
            dfs(graph, neighbor, visited)


# set visited
visited = set()

# Menjalankan dfs dari A
dfs(graph, "A", visited)
