# --> keterangan <--s
# 1. mulai
# 2. input nama pembeli 
# 3. input nomor hp pembeli 
# 4. input menu pesanan (makanan atau minuman)
# 5. jika pesan makanan, tampilkan menu makanan
#     jikam pesan minuman, tampilkan menu minuman
# 6. input pesanan 
# 7. input jumlah pesanan 
# 8. hitung total harga berdasarkan pesanan dan jumlah pesanan 
# 9. output nama pembeli, no hp pembeli, menu yang dipesan, jumlah pesanan dan harga yang harus dibayar
# 10. selesai

nama_pembeli = input("Masukkan Nama Pembeli: ")
no_hp_pembeli = input("Masukkan No HP Pembeli: ")
pesan_menu = input("Pesan Menu Apa? (makanan atau minuman): ")

menu_makanan = {
    "nasi goreng": 15000,
    "mie goreng": 12000,
    "ayam goreng": 18000
}

menu_minuman = {
    "aneka jus": 15000,
    "soft drink": 10000,
    "sweet ice tea": 5000,
}

if pesan_menu == "makanan":
    print("menu makanan:")
    for item, harga in menu_makanan.items():
        print(f"{item} - Rp.{harga}")
elif pesan_menu == "minuman":
    print("menu minuman:")
    for item, harga in menu_minuman.items():
        print(f"{item} - Rp.{harga}")
else:
    print("pilihan tidak ada")

pesanan = input("masukan pesanan: ")
jumlah_pesanan = int(input("masukan jumlah pesanan: "))


if pesan_menu == "makanan" and pesanan in menu_makanan:
    total_harga = menu_makanan[pesanan] * jumlah_pesanan
elif pesan_menu == "minuman" and pesanan in menu_minuman:
    total_harga = menu_minuman[pesanan] * jumlah_pesanan
else:
    print("pesanan tidak ada")


print(f"nama pembeli: {nama_pembeli}")
print(f"no pembeli: {no_hp_pembeli}")
print(f"menu yang dipesan: {pesanan}")
print(f"jumlah pesanan: {jumlah_pesanan}")
print(f"total harga pesanan: Rp.{total_harga}")