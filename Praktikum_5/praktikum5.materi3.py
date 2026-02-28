"""
=========================================================================
Nama : WIldhan Dzikrihantara
NIM : J0403251098
Kelas : TPL B1
=========================================================================
"""

# ==========================================================
# Contoh Rekursi 3: Menjumlahkan Elemen List
# ==========================================================


def jumlah_list(data, index=0):
    # Base case: jika index sudah mencapai panjang list
    if index == len(data):
        return 0
    # Recursive case: elemen sekarang + jumlah elemen setelahnya
    return data[index] + jumlah_list(data, index + 1)


print(jumlah_list([2, 4, 6, 8]))  # Output: 20
# Alur program
# jumlah_list([2, 4, 6, 8], 0)
# = 2 + jumlah_list([2, 4, 6, 8], 1)
# = 2 + (4 + jumlah_list([2, 4, 6, 8], 2))
# = 2 + (4 + (6 + jumlah_list([2, 4, 6, 8], 3)))
# = 2 + (4 + (6 + (8 + jumlah_list([2, 4, 6, 8], 4))))
# = 2 + (4 + (6 + (8 + 0)))
# = 2 + (4 + (6 + 8))
# = 2 + (4 + 14)
# = 2 + 18
# = 20
