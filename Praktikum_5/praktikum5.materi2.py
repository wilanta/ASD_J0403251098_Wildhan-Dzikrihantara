"""
=========================================================================
Nama : WIldhan Dzikrihantara
NIM : J0403251098
Kelas : TPL B1
=========================================================================
"""

"""
input 3
masuk 1 -2 -3
keluar
"""


def hitung(n):
    if n == 0:
        print("selesai")
        return

    print("Masuk : ", n)  # fase stacking
    hitung(n - 1)  # fase pemanggilan rekursif
    print("Keluar", n)  # fase unwinding


print("============ Program Tracking ==========")
hitung(5)
