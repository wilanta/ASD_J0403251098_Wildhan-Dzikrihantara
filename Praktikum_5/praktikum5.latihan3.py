"""
=========================================================================
Nama : WIldhan Dzikrihantara
NIM : J0403251098
Kelas : TPL B1
=========================================================================
"""


# ==========================================================
# Latihan 3: Mencari Nilai Maksimum
# ==========================================================
def cari_maks(data, index=0):
    # Base case
    if index == len(data) - 1:
        return data[index]

    # Recursive case
    maks_sisa = cari_maks(data, index + 1)

    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa


angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))

# Alur program:
# cari_maks([3, 7, 2, 9, 5], index: 0)
# -> cari_maks([3, 7, 2, 9, 5], index: 1)
# -> cari_maks([3, 7, 2, 9, 5], index: 2)
# -> cari_maks([3, 7, 2, 9, 5], index: 3)
# -> cari_maks([3, 7, 2, 9, 5], index: 4) -> 5 <index(4) == len(data)-1 (5-1=4)> [base case]
# -> kembali ke index 3: maks_sisa = 5, data[3] = 9 -> return 9
# -> kembali ke index 2: maks_sisa = 9, data[2] = 2 -> return 9
# -> kembali ke index 1: maks_sisa = 9, data[1] = 7 -> return 9
# -> kembali ke index 0: maks_sisa = 9, data[0] = 3 -> return 9
# Output: Nilai maksimum: 9
