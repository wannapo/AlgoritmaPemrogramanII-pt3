#nama: Rifqi Atha Ramadhan
#NIM: 241011450102
#Tugas Algoritma dan pemrograman 2 Mentari Pertemuan 3

def hitung_jumlah_baris(nama_file):
    jumlah = 0
    try:
        with open(nama_file, "r") as file:
            for baris in file:
                jumlah += 1
        print("Jumlah baris dalam file:", jumlah)
    except FileNotFoundError:
        print("File tidak ditemukan.")


def tulis_daftar_nama(nama_file):
    nama = input("Masukkan daftar nama (pisahkan dengan koma): ")
    
    with open(nama_file, "w") as file:
        file.write(nama)
    
    print("Daftar nama berhasil disimpan.")


def tambah_catatan(nama_file):
    catatan = input("Masukkan catatan baru: ")
    
    with open(nama_file, "a") as file:
        file.write(catatan + "\n")
    
    print("Catatan berhasil ditambahkan.")


def tampilkan_catatan(nama_file):
    print("\nIsi catatan:")
    
    try:
        with open(nama_file, "r") as file:
            for baris in file:
                print(baris.strip())
    except FileNotFoundError:
        print("File catatan belum ada.")


def cari_nama(nama_file):
    kata = input("Masukkan nama yang ingin dicari: ")
    
    try:
        with open(nama_file, "r") as file:
            ditemukan = False
            for baris in file:
                if kata.lower() in baris.lower():
                    print("Data ditemukan:", baris.strip())
                    ditemukan = True
            
            if not ditemukan:
                print("Nama tidak ditemukan.")
    
    except FileNotFoundError:
        print("File tidak ditemukan.")


while True:
    print("\n=== MENU PROGRAM FILE I/O ===")
    print("1. Hitung jumlah baris file")
    print("2. Simpan daftar nama ke file")
    print("3. Tambah catatan")
    print("4. Tampilkan semua catatan")
    print("5. Cari nama dalam file")
    print("6. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        hitung_jumlah_baris("data.txt")

    elif pilihan == "2":
        tulis_daftar_nama("nama.txt")

    elif pilihan == "3":
        tambah_catatan("catatan.txt")

    elif pilihan == "4":
        tampilkan_catatan("catatan.txt")

    elif pilihan == "5":
        cari_nama("nama.txt")

    elif pilihan == "6":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid.")