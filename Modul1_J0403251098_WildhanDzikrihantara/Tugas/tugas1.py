# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama  : Wildhan Dzikrihantara
# NIM   : J0403251098
# Kelas : B1
# ==========================================================

# -------------------------------
# Konstanta nama file
# -------------------------------
NAMA_FILE = "stok_barang.txt"


# -------------------------------
# Fungsi: Membaca data dari file
# -------------------------------
def baca_stok(nama_file):
    """
    Membaca data stok dari file teks.
    Format per baris: KodeBarang,NamaBarang,Stok

    Output:
    - stok_dict (dictionary)
      key   = kode_barang
      value = {"nama": nama_barang, "stok": stok_int}
    """
    stok_dict = {}

    # TODO: Buka file dan baca seluruh baris
    # Hint: with open(nama_file, "r", encoding="utf-8") as f:
    with open(nama_file, "r", encoding="utf-8") as f:
        for baris in f:

    # TODO: Untuk setiap baris:
    # - gunakan strip() untuk menghilangkan \n
            baris = baris.strip()
    # - split(",") untuk memisahkan kolom
            list_stok_per_baris = baris.split(",")
    # - simpan ke dictionary
            
            # [Handler] Jika banyaknya data perbaris tidak sama dengan 3, maka akan dilewati dan tidak terbaca
            if len(list_stok_per_baris) != 3:
                continue
            
            # Simpan value dari list list_stok_per_baris hasil split menjadi masing-masing variable value tunggal
            kode_barang, nama_barang, stok = list_stok_per_baris

            # Simpan data dalam dictionary (key, value)
            stok_dict[kode_barang] = {
                "nama_barang": nama_barang,
                "stok": int(stok),
            }

    return stok_dict

# -------------------------------
# Fungsi: Menyimpan data ke file
# -------------------------------
def simpan_stok(nama_file, stok_dict):
    """
    Menyimpan seluruh data stok ke file teks.
    Format per baris: KodeBarang,NamaBarang,Stok
    """
    # TODO: Tulis ulang seluruh isi file berdasarkan stok_dict
    # Hint: with open(nama_file, "w", encoding="utf-8") as f:
    with open(nama_file, "w", encoding="utf-8") as file:
        for kode_barang in sorted(stok_dict.keys()):
            nama_barang = stok_dict[kode_barang]["nama_barang"]
            stok = stok_dict[kode_barang]["stok"]
            file.write(f"{kode_barang},{nama_barang},{stok}\n")
        
        print("Data berhasil disimpan ke file")


# -------------------------------
# Fungsi: Menampilkan semua data
# -------------------------------
def tampilkan_semua(stok_dict):
    """
    Menampilkan semua barang di stok_dict.
    """
    # TODO: Jika kosong, tampilkan pesan stok kosong
    if not stok_dict:
        print("Stok kosong!")
        return
    # TODO: Tampilkan dengan format rapi: kode | nama | stok
    # Header
    print(f"\n{'='*14} Daftar Barang Kantin {'='*14}")
    print(f"{'KODE BARANG': <10} | {'NAMA BARANG': <20} | {'STOK': >5}")
    print("-" * 50)
    
    # Konten
    for kode_barang in sorted(stok_dict.keys()):
        nama_barang = stok_dict[kode_barang]["nama_barang"]
        stok = stok_dict[kode_barang]["stok"]
        print(
            f"{kode_barang[:8] + "..." if len(kode_barang) > 10 else kode_barang[:10]: <11} | {nama_barang[:17] + "..." if len(nama_barang) > 19 else nama_barang[:19]: <20} | {stok: >5}"
        )

# -------------------------------
# Fungsi: Cari barang berdasarkan kode
# -------------------------------
def cari_barang(stok_dict):
    """
    Mencari barang berdasarkan kode barang.
    """
    kode = input("Masukkan kode barang: ").strip().upper()

    # TODO: Cek apakah kode ada di dictionary
    if kode in stok_dict:
    
    # Jika ada: tampilkan detail barang
        nama_barang = stok_dict[kode]["nama_barang"]
        stok = stok_dict[kode]["stok"]
        
        print("\n==== PENCARIAN BARANG ====")
        print(f"KODE BARANG   : {kode}")
        print(f"NAMA BARANG   : {nama_barang}")
        print(f"STOK BARANG   : {stok}")
    # Jika tidak ada: tampilkan 'Barang tidak ditemukan'
    else:
        print("\nBarang tidak ditemukan")


# -------------------------------
# Fungsi: Tambah barang baru
# -------------------------------
def tambah_barang(stok_dict):
    """
    Menambah barang baru ke stok_dict.
    """
    kode = input("Masukkan kode barang baru: ").strip().upper()
    nama = input("Masukkan nama barang: ").strip()

    # TODO: Validasi kode tidak boleh duplikat
    if kode in stok_dict.keys():
    # Jika sudah ada: tampilkan 'Kode sudah digunakan' dan return
        print("Kode sudah digunakan")
        return
    
    # TODO: Input stok awal (integer)
    # Hint: stok_awal = int(input(...))
    try:
        stok_awal = int(input("Masukan stok awal: "))
    except ValueError:       
        # Jika user terus-menerus memasukan value dengan tipe data yang salah, maka akan user ditanyakan terus-menerus juga
        value_type_validator = True
        while value_type_validator:
            print("\nStok harus berupa angka!")
            stok_awal = input("Masukan stok awal: ")
            
            # Jika stok_awal berupa digit maka jadikan stok_awal menjadi integer dan hentikan looping
            if stok_awal.isdigit():
                stok_awal = int(stok_awal)
                value_type_validator = False
                    
    # TODO: Simpan ke dictionary
    stok_dict[kode.upper()] = {
        "nama_barang": nama.title(),
        "stok": stok_awal,
    }

# -------------------------------
# Fungsi: Update stok barang
# -------------------------------
def update_stok(stok_dict):
    """
    Mengubah stok barang (tambah atau kurangi).
    Stok tidak boleh menjadi negatif.
    """
    kode = input("Masukkan kode barang yang ingin diupdate: ").strip().upper()

    # TODO: Cek apakah kode ada di dictionary
    # Jika tidak ada: tampilkan pesan dan return
    if kode not in stok_dict:
        print("Kode barang tidak ditemukan!")
        return

    print("Pilih jenis update:")
    print("1. Tambah stok")
    print("2. Kurangi stok")

    pilihan = input("Masukkan pilihan (1/2): ").strip()

    # TODO: Input jumlah perubahan stok
    # Hint: jumlah = int(input("Masukkan jumlah: "))
    try:
        jumlah = int(input("Masukan jumlah: "))
    except ValueError:
        print("Jumlah harus berupa angka!")
        
        # Jika user terus-menerus memasukan value dengan tipe data yang salah, maka akan user ditanyakan terus-menerus juga
        value_type_validator = True
        while value_type_validator:
            jumlah = input("Masukan stok awal: ")
            
            # Jika jumlah berupa digit maka jadikan jumlah menjadi integer dan hentikan looping
            if jumlah.isdigit():
                jumlah = int(jumlah)
                value_type_validator = False

    # TODO:
    # - Jika pilihan 1: stok = stok + jumlah
    # - Jika pilihan 2: stok = stok - jumlah
    # - Jika hasil < 0: batalkan dan tampilkan error
    match pilihan:
        case "1":
            stok_dict[kode]["stok"] += jumlah
        case "2":
            # Jika jumlah > stok, maka akan ditolak
            if jumlah > stok_dict[kode]["stok"]:
                print("Jumlah perubahan tidak boleh melebihi stok!")
                return
            else:
                stok_dict[kode]["stok"] -= jumlah
        case _:
            print("Pilihan tidak valid! ")
            return

# -------------------------------
# Program Utama
# -------------------------------
def main():
    # Membaca data dari file saat program mulai
    stok_barang = baca_stok(NAMA_FILE)

    while True:
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampilkan_semua(stok_barang)

        elif pilihan == "2":
            cari_barang(stok_barang)

        elif pilihan == "3":
            tambah_barang(stok_barang)

        elif pilihan == "4":
            update_stok(stok_barang)

        elif pilihan == "5":
            simpan_stok(NAMA_FILE, stok_barang)
            print("Data berhasil disimpan.")

        elif pilihan == "0":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


# Menjalankan program utama
if __name__ == "__main__":
    main()
