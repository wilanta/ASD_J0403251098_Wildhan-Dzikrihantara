""" 
===========================================
Praktikum 2: Konsep ADT dan file handling (STUDI KASUS)
Latihan 1: Membuat fungsi load data
===========================================
""" 

nama_file = "data_mahasiswa.txt"

# Membuat fungsi membacata data mahasiswa dengan parameter nama_file
def baca_data_mahasiswa(nama_file):
    data_dict = {} # inisialisasi data dictionary

    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip() # Menghilangkan \n
            parts = baris.split(",") # pecah data jadi satuan
            
            # Jika banyaknya data perbaris tidak sama dengan 3, maka skip
            if len(parts) != 3:
                continue
            
            nim, nama, nilai_str = parts

            # Simpan data dalam dictionary (key, value)
            data_dict[nim] = {
                "nama": nama,
                "nilai": int(nilai_str),
        }
            
        return data_dict

# Memanggil fungsi baca_data_mahasiswa
# opn_data = baca_data_mahasiswa(nama_file)
# print("Jumlah data terbaca:", len(opn_data))

""" 
===========================================
Praktikum 2: Konsep ADT dan file handling (STUDI KASUS)
Latihan 2: Membuat fungsi menampilkan data
===========================================
""" 
def tampilkan_data(data_dict):
    # Membuat header tabel
    print("\n==== Daftar Mahasiswa ====")
    print(f"{'NIM': <10} | {'Nama': <12} | {'Nilai': >5}")
    print("-" * 32)
    
    """
    Untuk tampilan yang rapi, atur f-string formating
        {'NIM': <10} artinya:
            tampilkan nim <= rata kiri dengan lebar 10 karater
        {'Nama': <12} artinya:
            tampilkan nama rata kiri, dengan lebar kolom 12 karakter
        {'Nilai': >5} artinya:
            tampilkan nilai => rata kanan, dengan lebar 5 karakter
    """
    
    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim: <10} | {nama: <12} | {nilai: >5}")

# Memanggil fungsi menampilkan data
# tampilkan_data(opn_data)

""" 
===========================================
Praktikum 2: Konsep ADT dan file handling (STUDI KASUS)
Latihan 3: Membuat fungsi cari data
===========================================
""" 
def cari_data(data_dict):
    # Mencari data mahasiswa berdasarkan NIM
    nim_cari = input("Masukan NIM yang ingin dicari : ").strip()
    
    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]
        
        print("\n=== DATA MAHASISWA ====")
        print(f"NIM             : {nim_cari}")
        print(f"Nama            : {nama}")
        print(f"Nilai           : {nilai}")
    else:
        print("\nData tidak ditemukan")
    
# cari_data(opn_data)

""" 
===========================================
Praktikum 2: Konsep ADT dan file handling (STUDI KASUS)
Latihan 4: Membuat fungsi menampilkan data
===========================================
""" 
def update_nilai(data_dict):
    nim = input("Masukan NIM Mahasiswa yang akan diupdate nilainya : ")
    
    if nim not in data_dict:
        print("NIM tidak ditemukan, update dibatalkan")
        return 
    
    try:
        nilai_baru = int(input("Masukan nilai baru (0-100) : "))
    except ValueError:
        print("Nilai harus berupa angka. Update dibatalkan")
        return
        
    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus dalam rentang 0-100. Update dibatalkan")
    
    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru
    
    print(f"Update berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")
        

# update_nilai(opn_data)
# print(opn_data)

""" 
===========================================
Praktikum 3: Konsep ADT dan file handling (STUDI KASUS)
Latihan 5: Membuat fungsi menyimpan data
===========================================
""" 
def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")
        
        print("Data berhasil disimpan ke file")

# simpan_data(nama_file, opn_data)

""" 
===========================================
Praktikum 3: Konsep ADT dan file handling (STUDI KASUS)
Latihan 6: Membuat menu
===========================================
""" 

def main():
    # Menjalankan fungsi 1 load data
    buka_data = baca_data_mahasiswa(nama_file)
    
    while True:
        print("\n ==== MENU ====")
        print("1. Tampilkan semua data")
        print("2. Cari data")
        print("3. Update nilai mahasiswa")
        print("4. Simpan data ke file")
        print("0. Keluar")
    
        match int(input("Pilihan : ")):
            case 1: 
                tampilkan_data(buka_data)
            case 2:
                cari_data(buka_data)
            case 3:
                update_nilai(buka_data)
            case 4:
                simpan_data(nama_file, buka_data)
            case 0:
                break
            case _:
                print("Pilihan tidak valid.")



if __name__ == "__main__":
    main()