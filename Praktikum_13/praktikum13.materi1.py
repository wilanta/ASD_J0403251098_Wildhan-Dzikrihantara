# ==========================================================
# Implementasi Kruskal
# ==========================================================

# Daftar edge: (bobot, node1, node2)
edges = [(3, "B", "D"), (1, "C", "D"), (2, "A", "C"), (5, "A", "D"), (4, "A", "B")]

"""
Step kruskal untuk MST Start
"""


# [Step 1] Mengurutkan edge berdasarkan bobot, untuk Kruskal harus dishort terlebih dahulu
edges.sort()
print(f"Hasil sort:{edges}\n")

# [Step 2] Buat var penampungan untuk hasil MST
mst = []
total_weight = 0

# [Step 3] Untuk menampung node yang sudah dipilih (menggunakan set)
connected = set()

# [Step 4] memeriksa apa edge membentuk cycle dan jika tidak tambahkan ke mst (terus diulang sampai semua edge/node ter-MST)
for weight, u, v in edges:
    # Jika edge tidak membentuk cycle sederhana
    if u not in connected or v not in connected:
        # jika edge tidak membentuk cycle/salah satu atau kedunya node dalam edge tidak berada di connector maka akan ditambahkan untuk membentuk graph MST
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)

print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

print("Total bobot =", total_weight)

print(connected)
