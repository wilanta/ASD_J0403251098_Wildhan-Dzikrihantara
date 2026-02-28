"""
=========================================================================
Nama : WIldhan Dzikrihantara
NIM : J0403251098
Kelas : TPL B1
=========================================================================
"""

"""
Materi rekursif : menjumlahkan elemen list
"""

def jumlah_list(data, index=0):
    if index == len(data):
        return 0
    # recursive case
    return data[index] + jumlah_list(data, index=0)

print("========== Program Jumlah Data List ============")
print(jumlah_list([1,2,3]))
