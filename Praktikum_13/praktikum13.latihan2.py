# Nama : Wildhan Dzikrihantara
# NIM : J0403251098
# Kelas : B1
# Praktikum 13 - Graph III: Spanning Tree

# ==========================================================
# Implementasi Kruskal
# ==========================================================

# Daftar edge: (bobot, node1, node2)
edges = [(1, "C", "D"), (2, "A", "C"), (3, "B", "D"), (4, "A", "B"), (5, "A", "D")]


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

# Jawaban Analisis:
# 1. Edge mana yang dipilih pertama kali?
# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
# 3. Berapa total bobot MST yang dihasilkan?
# 4. Mengapa edge tertentu tidak dipilih?

"""
1. C

2. Dalam Algoritma kruskal, proses pemilihan edge dilakukan secara terurut dari urutan bobot terkecil sampai semua node terhubung

3. 6

4. Karena setiap algoritma untuk MST, untuk setiap edge yang menghubungkan node-node yang dipilih adalah edge yang paling kecil diantara edges tersebut
"""
