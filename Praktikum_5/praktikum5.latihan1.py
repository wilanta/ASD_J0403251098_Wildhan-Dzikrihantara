"""
=========================================================================
Nama : WIldhan Dzikrihantara
NIM : J0403251098
Kelas : TPL B1
=========================================================================
"""


# ==========================================================
# Latihan 1: Rekursi Pangkat
# ==========================================================
def pangkat(a, n):
    # Base case
    if n == 0:
        return 1

    # Recursive case
    return a * pangkat(a, n - 1)


print(pangkat(2, 4))  # Output: 16
# Alur program:
# pangkat(2, 4) -> 2 * pangkat(2, 3)
# pangkat(2, 3) -> 2 * pangkat(2, 2)
# pangkat(2, 2) -> 2 * pangkat(2, 1)
# pangkat(2, 1) -> 2 * pangkat(2, 0)
# pangkat(2, 0) -> 1 [base case]

#  Perhitungan:
# pangkat(2, 1) -> 2 * 1 = 2
# pangkat(2, 2) -> 2 * 2 = 4
# pangkat(2, 3) -> 2 * 4 = 8
# pangkat(2, 4) -> 2 * 8 = 16 [base case]
