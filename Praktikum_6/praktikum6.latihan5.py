"""
=========================================================================
Nama : Wildhan Dzikrihantara
NIM : J0403251098
Kelas : TPL B1
=========================================================================
"""


# ==========================================================================
# Latihan 5 . Melengkapi Fungsi Merge
# ==========================================================================
def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)


def merge(left, right):
    result = []
    i = 0
    j = 0

    # Membandingkan elemen kiri dan kanan
    while i < len(left) and j < len(right):
        if (
            left[i] > right[j]
        ):  # Kondisi untuk descending, untuk ascending gunakan left[i] < right[j]
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Menambahkan sisa elemen jika ada
    result.extend(left[i:])
    result.extend(right[j:])

    return result


"""
Soal:
1. Lengkapi kondisi agar menjadi ascending.
2. Jelaskan fungsi result.extend().

Jawaban:
1. done
2. Fungsi result.extend() digunakan untuk menambahkan semua elemen dari iterable (dalam hal ini, sisa elemen dari left atau right) ke dalam list result. Ini memastikan bahwa setelah membandingkan elemen-elemen dari kedua bagian, semua elemen yang tersisa (yang sudah terurut) juga dimasukkan ke dalam hasil akhir.
"""
