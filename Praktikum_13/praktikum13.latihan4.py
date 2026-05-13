# Nama : Wildhan Dzikrihantara
# NIM : J0403251098
# Kelas : B1
# Praktikum 13 - Graph III: Spanning Tree

# Daftar edge: (bobot, node1, node2)
edges = [
    (4, "GedungA", "GedungB"),
    (2, "GedungA", "GedungC"),
    (3, "GedungB", "GedungD"),
    (1, "GedungC", "GedungD"),
    (5, "GedungA", "GedungD"),
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
# 1. Algoritma apa yang digunakan?
# 2. Edge mana saja yang dipilih?
# 3. Berapa total biaya minimum?
# 4. Mengapa MST cocok digunakan pada kasus ini?

"""
1. Kruskal

2. {'GedungC', 'GedungD', 'GedungB', 'GedungA'}

3. 6

4. Karena dalam kasus ini kita mencari mana hubungan jaringan kabel (edge) yang memiliki biaya (bobot) yang paling kecil dan juga menghilangkan ketidakefisienan seperti ada jaringan kabel yang loop sehingga dalam hal ini mst sangat berguna untuk menuntaskan permasalahan tersebut.
"""
