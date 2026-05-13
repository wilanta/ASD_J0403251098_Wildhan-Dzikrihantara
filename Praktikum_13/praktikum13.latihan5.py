# Nama : Wildhan Dzikrihantara
# NIM : J0403251098
# Kelas : B1
# Praktikum 13 - Graph III: Spanning Tree

# Daftar edge: (bobot, node1, node2)
edges = [
    (5, "Bogor", "Jakarta"),
    (2, "Bogor", "Depok"),
    (3, "Depok", "Jakarta"),
    (6, "Jakarta", "Bandung"),
    (4, "Depok", "Bandung"),
]

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

# Jawaban Analisis:
# 1. Kasus apa yang dipilih?
# 2. Algoritma apa yang digunakan?
# 3. Edge mana saja yang dipilih dalam MST?
# 4. Berapa total bobot MST?
# 5. Mengapa edge tertentu tidak dipilih?

"""
1. jaringan jalan antar kota

2. kruskal

3. ('Bogor', 'Depok', 2), ('Depok', 'Jakarta', 3), ('Depok', 'Bandung', 4)

4. 9

5. Karena tidak efisien secara bobot, karena prinsip dari semua algoritma mst adalah menghubungkan semua node dan mencari node mana saja yang paling efisien dengan meniadakan cycle dan jika terdapat 2 jalur (edge) maka akan memilih edge dengan bobot yang terkecil
"""
