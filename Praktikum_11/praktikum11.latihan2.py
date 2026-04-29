# ===========================================
# Nama : WIldhan Dzikrihantara
# NIM : J0403251098
# ===========================================

graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": [], "F": []}


def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


visited = set()

print("DFS dari A:")
dfs(graph, "A", visited)

# ----------------------------------

"""
1. Mengapa DFS masuk ke node terdalam terlebih dahulu?
=> DFS masuk ke node terdalam terlebih dahulu karena DFS menggunakan pendekatan rekursif atau stack untuk mengeksplorasi node. Ketika DFS menemukan sebuah node, ia akan langsung melanjutkan ke salah satu neighbor-nya tanpa menyelesaikan eksplorasi neighbor lainnya terlebih dahulu. Hal ini menyebabkan DFS masuk ke node terdalam sebelum kembali ke node sebelumnya untuk mengeksplorasi neighbor lainnya.

2. Apa yang terjadi jika urutan neighbor diubah?
=> Jika urutan neighbor diubah, maka urutan kunjungan DFS juga akan berubah. DFS akan mengikuti urutan neighbor yang diberikan dalam graph, sehingga jika urutan neighbor diubah, maka DFS akan mengeksplorasi node-node tersebut dalam urutan yang berbeda, menghasilkan urutan kunjungan yang berbeda pula.

3. Bandingkan hasil DFS dengan BFS pada graph yang sama.
=> Hasil DFS dan BFS pada graph yang sama akan berbeda karena kedua algoritma tersebut memiliki pendekatan yang berbeda dalam mengeksplorasi node. DFS akan mengeksplorasi node terdalam terlebih dahulu, sedangkan BFS akan mengeksplorasi semua node pada tingkat yang sama sebelum melanjutkan ke tingkat berikutnya. Oleh karena itu, urutan kunjungan node dalam DFS dan BFS akan berbeda, meskipun mereka bekerja pada graph yang sama.
"""
