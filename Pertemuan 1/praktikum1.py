""" 
===========================================
Praktikum 1: Konsep ADT dan file handling
Latihan dasar 1A: Membaca seluruh isi file
===========================================
""" 

# Membuka file dalam satu string
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read() # Membaca seluruh isi file dalam satu string
    print(isi_file)
    
    print("== Hasil Read ==")
    print("Tipe data: ", type(isi_file))
    print("Jumlah karakter, ", len(isi_file))
    print("Jumlah baris", isi_file.count("\n") + 1)

# Membuka file perbaris
print("\n== Membaca file per baris ==")
jumlah_baris = 0
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip()
        print("Baris ke-", jumlah_baris)
        print("Isinya:", baris)
        
""" 
===========================================
Praktikum 1: Konsep ADT dan file handling
Latihan dasar 2: Parsing baris menjadi kolom data
===========================================
""" 
# Membuka file perbaris
print("\n== Membaca file per baris ==")
jumlah_baris = 0
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip()
        nim, nama, nilai = baris.split(",") # parsing data berdasarkan karakter
        print("NIM: ", nim, "| Nama: ", nama, "| Nilai: ", nilai)

""" 
===========================================
Praktikum 1: Konsep ADT dan file handling
Latihan dasar 3: Membaca file dan menyimpan ke list
===========================================
""" 
# Membuka file perbaris
data_list = []
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip()
        
        # simpan sebagai list [nim, nama, nilai]
        data_list.append([nim, nama, int(nilai)])
        
print("\n=== Data Mahasiswa dalam List ==")
print(data_list)

print("\n=== Jumlah record dalam List ==")
print(len(data_list))

print("\n=== Menampilkan record tertentu ==")
print("Contoh record: ", data_list[0])

""" 
===========================================
Praktikum 1: Konsep ADT dan file handling
Latihan dasar 4: Membaca file dan menyimpan ke dict
===========================================
""" 
# Membuka file perbaris
data_dict = {}
jumlah_baris = 0

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris += 1
        baris = baris.strip()
        
        nim, nama, nilai = baris.split(",")

        data_dict[nim] = {
            "nama": nama,
            "nilai": int(nilai),
        }

print("\n=== Data Mahasiswa dalam Dict ===")
print(data_dict)