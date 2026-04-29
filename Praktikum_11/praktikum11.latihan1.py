# ===========================================
# Nama : WIldhan Dzikrihantara
# NIM : J0403251098
# ===========================================

from collections import deque

graph = {
    "Rumah": ["Sekolah", "Toko"],
    "Sekolah": ["Perpustakaan"],
    "Toko": ["Pasar"],
    "Perpustakaan": [],
    "Pasar": [],
}


def bfs(graph, start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


print("BFS dari Rumah:")
bfs(graph, "Rumah")

# ----------------------------------
"""
1. Node mana yang dikunjungi pertama dikunjungi?
=> Node yang dikunjungi pertama adalah "Rumah" karena BFS memulai dari node awal yang diberikan.

2. Mengapa BFS cocok untuk mencari jalur terdekat?
=> BFS cocok untuk mencari jalur terdekat karena BFS mengeksplorasi semua node pada tingkat yang sama sebelum melanjutkan ke tingkat berikutnya. Dengan cara ini, BFS akan menemukan jalur terpendek dalam hal jumlah edge yang dilalui.

3. Apa perbedaan urutan BFS jika struktur graph diubah?
=> Urutan BFS akan berubah jika struktur graph diubah karena BFS mengikuti urutan node yang terhubung. Jika ada perubahan dalam hubungan antar node, maka urutan kunjungan akan berbeda sesuai dengan struktur baru graph tersebut.
"""
