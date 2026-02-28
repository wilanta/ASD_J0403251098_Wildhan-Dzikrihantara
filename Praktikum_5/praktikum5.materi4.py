"""
=========================================================================
Nama : WIldhan Dzikrihantara
NIM : J0403251098
Kelas : TPL B1
=========================================================================
"""


# ==========================================================
# Contoh Backtracking 1: Kombinasi Biner (n)
# ==========================================================
def biner(n, hasil=""):
    # Base case: jika panjang string sudah n, cetak hasil
    if len(hasil) == n:
        print(hasil)
        return

    # Choose + Explore: tambah '0'
    biner(n, hasil + "0")

    # Choose + Explore: tambah '1'
    biner(n, hasil + "1")


biner(3)
# Alur program:
# biner(3, "")
# = biner(3, "0") + biner(3, "1")
# = (biner(3, "00") + biner(3, "01")) + (biner(3, "10") + biner(3, "11"))
# = ((biner(3, "000") + biner(3, "001")) + (biner(3, "010") + biner(3, "011"))) + ((biner(3, "100") + biner(3, "101")) + (biner(3, "110") + biner(3, "111")))
# = (("000" + "001") + ("010" + "011")) + (("100" + "101") + ("110" + "111"))
# Output:   000
#           001
#           010
#           011
#           100
#           101
#           110
#           111
