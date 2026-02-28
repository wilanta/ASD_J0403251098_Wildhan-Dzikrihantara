"""
=========================================================================
Nama : WIldhan Dzikrihantara
NIM : J0403251098
Kelas : TPL B1
=========================================================================
"""


# ==========================================================
# Latihan 4: Kombinasi Huruf
# ==========================================================
def kombinasi(n, hasil=""):
    if len(hasil) == n:
        print(hasil)
        return

    kombinasi(n, hasil + "A")
    kombinasi(n, hasil + "B")


kombinasi(2)

# Alur program:
# kombinasi(2, hasil: "")
# -> kombinasi(2, hasil: "A")
# -> kombinasi(2, hasil: "AA") -> print "AA" [base case]
# -> kembali ke hasil: "A": kombinasi(2, hasil: "AB") -> print "AB" [base case]
# -> kembali ke hasil: "": kombinasi(2, hasil: "B")
# -> kombinasi(2, hasil: "BA") -> print "BA" [base case]
# -> kembali ke hasil: "B": kombinasi(2, hasil: "BB") -> print "BB" [base case]

# Output:
# AA
# AB
# BA
# BB

# Bagaimana jumlah kombinasi yang dihasilkan?
"""
Jumlah kombinasi = 2^n (karena setiap posisi bisa diisi dengan 2 pilihan: A atau B)
"""
