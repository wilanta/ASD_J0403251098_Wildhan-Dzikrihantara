"""
=========================================================================
Nama : Wildhan Dzikrihantara
NIM : J0403251098
Kelas : TPL B1
=========================================================================
"""


# ==========================================================================
# Latihan 1 . Memahami Kode Program (Insertion Sort)
# ==========================================================================
def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

    return data


"""
Soal:
1. Mengapa perulangan dimulai dari indeks 1?
2. Apa fungsi variabel key?
3. Mengapa digunakan while, bukan for?
4. Operasi apa yang terjadi di dalam while?

Jawaban:
1. Perulangan dimulai dari indeks 1 karena pada indeks 0 dianggap sudah terurut. Insertion sort bekerja dengan membandingkan elemen saat ini (key) dengan elemen-elemen sebelumnya, sehingga dimulai dari indeks 1 untuk memastikan bahwa ada elemen sebelumnya yang dapat dibandingkan.
2. Variabel key digunakan untuk menyimpan nilai elemen saat ini yang sedang diproses. Key akan dibandingkan dengan elemen-elemen sebelumnya untuk menentukan posisi yang tepat dalam urutan yang sudah terurut.
3. Digunakan while karena kita perlu terus membandingkan key dengan elemen-elemen sebelumnya hingga menemukan posisi yang tepat untuk key. For loop tidak cocok dalam kasus ini karena kita tidak tahu berapa banyak elemen sebelumnya yang perlu dibandingkan, sedangkan while loop memungkinkan kita untuk terus membandingkan sampai kondisi tertentu terpenuhi.
4. Di dalam while, terjadi operasi pergeseran elemen-elemen yang lebih besar dari key ke posisi berikutnya (data[j + 1] = data[j]). Ini dilakukan untuk membuat ruang bagi key agar dapat ditempatkan pada posisi yang benar dalam urutan yang sudah terurut. Setelah pergeseran selesai, key akan ditempatkan pada posisi yang tepat (data[j + 1] = key).
"""
