# Program Pengelolaan Peminjaman Alat Laboratorium
lab_tools = {
    "Mikroskop": {"stok": 5, "dipinjam": 0},
    "Tabung Reaksi": {"stok": 10, "dipinjam": 0},
    "Bunsen Burner": {"stok": 3, "dipinjam": 0},
    "Pipet": {"stok": 7, "dipinjam": 0},
    "Gelas Ukur": {"stok": 4, "dipinjam": 0}
}

def tampilkan_alat():
    print("\nDaftar Alat Laboratorium:")
    for alat, info in lab_tools.items():
        print(f"{alat} - Stok: {info['stok']} | Dipinjam: {info['dipinjam']}")

def pinjam_alat():
    tampilkan_alat()
    alat = input("Masukkan nama alat yang ingin dipinjam: ")
    if alat in lab_tools:
        if lab_tools[alat]['stok'] > 0:
            lab_tools[alat]['stok'] -= 1
            lab_tools[alat]['dipinjam'] += 1
            print(f"{alat} berhasil dipinjam!")
        else:
            print(f"Maaf, {alat} tidak tersedia (stok habis).")
    else:
        print("Alat tidak ditemukan di laboratorium.")

def kembalikan_alat():
    tampilkan_alat()
    alat = input("Masukkan nama alat yang ingin dikembalikan: ")
    if alat in lab_tools:
        if lab_tools[alat]['dipinjam'] > 0:
            lab_tools[alat]['stok'] += 1
            lab_tools[alat]['dipinjam'] -= 1
            print(f"{alat} berhasil dikembalikan!")
        else:
            print(f"Tidak ada {alat} yang sedang dipinjam.")
    else:
        print("Alat tidak ditemukan di laboratorium.")

def cek_stok():
    tampilkan_alat()

def menu():
    while True:
        print("\n--- Sistem Peminjaman Alat Laboratorium ---")
        print("1. Pinjam Alat")
        print("2. Kembalikan Alat")
        print("3. Cek Stok Alat")
        print("4. Keluar")
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            pinjam_alat()
        elif pilihan == "2":
            kembalikan_alat()
        elif pilihan == "3":
            cek_stok()
        elif pilihan == "4":
            print("Terima kasih! Sampai jumpa.")
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")

# Menjalankan program
menu()
