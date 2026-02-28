"""
=========================================================================
Nama : WIldhan Dzikrihantara
NIM : J0403251098
Kelas : TPL B1
=========================================================================
"""

# ==========================================================
# Latihan 2: Tracing Rekursi
# ==========================================================


def countdown(n):
    if n == 0:
        print("Selesai")
        return

    print("Masuk:", n)
    countdown(n - 1)
    print("Keluar:", n)


countdown(3)
# Alur program:
# countdown(3) -> Masuk: 3 -> countdown(2) -> Masuk: 2 -> countdown(1) -> Masuk: 1 -> countdown(0) -> Selesai

# Mengapa output 'Keluar' muncul terbalik?
"""
Output 'Keluar' muncul terbalik karena setelah mencapai base case (n == 0), program mulai kembali ke langkah sebelumnya (n == 1, n == 2, n == 3) dan mencetak 'Keluar' untuk setiap langkah tersebut. Jadi, urutan 'Keluar' adalah kebalikan dari urutan 'Masuk'.
"""
