"""
=========================================================================
Nama : Wildhan Dzikrihantara
NIM : J0403251098
Kelas : TPL B1
=========================================================================
"""


# ==========================================================================
# Latihan 4 . Memahami Kode Program (Merge Sort)
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
        if left[i] < right[j]:
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
1. Apa yang dimaksud dengan base case?
2. Mengapa fungsi memanggil dirinya sendiri?
3. Apa tujuan fungsi merge()?

Jawaban:
1. Base case adalah kondisi di mana fungsi rekursif berhenti memanggil dirinya sendiri. Dalam kode ini, base case terjadi ketika panjang data kurang dari atau sama dengan 1, yang berarti data sudah dianggap terurut.
2. Fungsi memanggil dirinya sendiri untuk membagi masalah menjadi bagian yang lebih kecil. Dalam merge sort, data dibagi menjadi dua bagian hingga mencapai base case, kemudian hasilnya digabungkan kembali dalam urutan yang benar.
3. Fungsi merge() bertujuan untuk menggabungkan dua bagian data yang sudah terurut (left dan right) menjadi satu daftar yang terurut. Fungsi ini membandingkan elemen-elemen dari kedua bagian dan menyusunnya dalam urutan yang benar sebelum mengembalikan hasilnya.
"""
