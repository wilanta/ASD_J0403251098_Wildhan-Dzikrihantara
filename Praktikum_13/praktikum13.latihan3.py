# Nama : Wildhan Dzikrihantara
# NIM : J0403251098
# Kelas : B1
# Praktikum 13 - Graph III: Spanning Tree

import heapq

# Berbeda dengan kruskal yang memakai list, prim menggunakan dict
graph = {
    "A": {"B": 4, "C": 2, "D": 5},
    "B": {"A": 4, "D": 3},
    "C": {"A": 2, "D": 1},
    "D": {"A": 5, "B": 3, "C": 1},
}


def prim(graph, start):
    visited = set([start])

    edges = []

    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_weight = 0

    while edges:
        weight, u, v = heapq.heappop(edges)

        if v not in visited:
            visited.add(v)

            mst.append((u, v, weight))
            total_weight += weight

            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
    return mst, total_weight


mst, total = prim(graph, "A")

print("MINIMUM SPANNING TREE:")

for edge in mst:
    print(edge)

print("Total bobot =", total)

# Jawaban Analisis:
# 1. Node awal apa yang digunakan?
# 2. Edge mana yang dipilih pertama kali?
# 3. Bagaimana Prim menentukan edge berikutnya?
# 4. Berapa total bobot MST yang dihasilkan?
# 5. Apa perbedaan pendekatan Prim dan Kruskal?

"""
1. A

2. A-C

3. Dengan menggunakan min-heap untuk menyimpan edge yang tersedia, Prim selalu memilih edge dengan bobot terkecil yang menghubungkan node yang sudah dikunjungi dengan node yang belum dikunjungi.

4. 6

5. Prim menghasilkan mst dengan memulai dari satu node dan menambahkan edge terkecil yang menghubungkan node-node sedangkan kruskal menghasilkan mst dengan mengurutkan seluruh edge terlebih dahulu lalu membuat mst dengan menambahkan edge yang paling kecil diantara node-node yang terhubung
"""
