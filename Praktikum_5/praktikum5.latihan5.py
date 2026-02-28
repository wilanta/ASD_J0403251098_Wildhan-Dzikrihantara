"""
=========================================================================
Nama : WIldhan Dzikrihantara
NIM : J0403251098
Kelas : TPL B1
=========================================================================
"""


# ==========================================================
# Studi Kasus: Generator PIN
# ==========================================================
def buat_pin(panjang, hasil=""):
    if len(hasil) == panjang:  # base case: jika panjang PIN sudah tercapai
        print("PIN:", hasil)  # menampilkan PIN yang sudah terbentuk
        return

    for angka in ["0", "1", "2"]:  # iterasi untuk setiap angka yang mungkin (0, 1, 2)
        buat_pin(
            panjang, hasil + angka
        )  # rekursi dengan menambahkan angka ke hasil saat ini


buat_pin(3)

# Bagaimana cara mencegah angka yang sama muncul berulang?
"""
Bisa dengan menambahkan kondisi untuk memeriksa apakah angka yang akan ditambahkan sudah ada dalam hasil saat ini sebelum melakukan rekursi.
"""
