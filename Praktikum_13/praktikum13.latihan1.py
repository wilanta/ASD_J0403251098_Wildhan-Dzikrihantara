# Nama : Wildhan Dzikrihantara
# NIM : J0403251098
# Kelas : B1
# Praktikum 13 - Graph III: Spanning Tree

# Daftar edge graph
edges = [("A", "B"), ("A", "C"), ("A", "D"), ("C", "D"), ("B", "D")]
# Contoh spanning tree
spanning_tree = [("A", "C"), ("C", "D"), ("D", "B")]

print("Edge pada graph:")

for edge in edges:
    print(edge)

print("\nSpanning Tree:")

for edge in spanning_tree:
    print(edge)
print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

# Jawaban Analisis:
# 1. Apa perbedaan graph awal dan spanning tree?
# 2. Mengapa spanning tree tidak boleh memiliki cycle?
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit

"""
1. Pada graph awal masih terdapat node-node yang membentuk suatu cycle yang mana tidak efisien secara bobot (edge), sedangkan pada spanning tree node-node tetap tersambung tapi lebih efisien tanpa cycle dan memiliki bobot yang paling minimal (kecil).

2. Karena prinsipnya dari MST (spanning tree) adalah menyambungkan seluruh node dengan bobot seminimal mungkin.

3. Karena proses untuk mencapai spanning tree (kruskal & prim) menghilangkan edge yang terlalu besar secara bobot dan memastikan agar tidak ada sebuah loop.
"""
