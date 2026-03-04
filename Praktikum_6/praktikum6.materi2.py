"""
=========================================================================
Nama : Wildhan Dzikrihantara
NIM : J0403251098
Kelas : TPL B1
=========================================================================
"""

# ==========================================================================
# Insertion sort dengan tracing
# ==========================================================================


def insertion_sort(data):
    # Melihat data awal
    print(f"Data awal: {data}")
    print("=" * 50)

    # loop mulai dari data ke-2 (index array ke-1)
    for i in range(1, len(data)):
        key = data[i]  # simpan data ke-i sebagai key
        j = i - 1  # index elemen terakhir di bagian kiri

        print(f"iterasi ke-{i}")
        print(f"Nilai key = {key}")
        print(f"Bagian Kiri (terurut) : {data[:i]}")
        print(f"Bagian Kanan (belum terurut) : {data[i:]}")

        # Geser
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        # sisipkan key ke posisi yang benar
        data[j + 1] = key

        print(f"Setelah disisipkan : {data}")
        print("-" * 50)
    return data


angka = [7, 8, 5, 2, 4, 6]
print("Hasil sorting : ", insertion_sort(angka))
