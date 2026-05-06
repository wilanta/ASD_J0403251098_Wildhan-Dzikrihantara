# ========================================
# Implementasi Bellman-Ford
# ========================================

graph = {
    "A": {"B": 5, "C": 4},
    "B": {},
    "C": {"B": -2},
}


def bellman_ford(graph, start):
    # Menyimpan jarak minimum dari node awal ke setiap node.
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1.
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                # Update jarak jika node saat ini sudah dapat dicapai
                # dan ditemukan jalur yang lebih pendek ke neighbor.
                if (
                    distances[node] != float("inf")
                    and distances[node] + weight < distances[neighbor]
                ):
                    distances[neighbor] = distances[node] + weight

    return distances


hasil = bellman_ford(graph, "A")
print(hasil)
