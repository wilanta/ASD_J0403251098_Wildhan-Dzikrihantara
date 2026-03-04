"""
=========================================================================
Nama : Wildhan Dzikrihantara
NIM : J0403251098
Kelas : TPL B1
=========================================================================
"""


# ==========================================================================
# Latihan 2 . Melengkapi Potongan Kode
# ==========================================================================
def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while (
            j >= 0 and data[j] < key
        ):  # kondisi untuk descending, dan untuk ascending ubah menjadi data[j] > key
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

    return data


"""
Soal:
1. Lengkapi kondisi agar menjadi sorting ascending.
2. Ubah agar menjadi descending

Jawaban:
1. done
2. done
"""

print(insertion_sort([5, 2, 9, 1, 5, 6]))
