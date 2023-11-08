# --> keterangan <--s
# 1. mulai
# 2. input nama kendaraan, jenis bensin dan kota kota_tujuan
# 3. tentukan harga per liter dan jarak tempuh berdasarkan jenis jenis bensin
# 4. tentukan jarak kota tujuan berdasarkan kota tujuan
# 5. hitung pemakanian bensin 
# 6. hitung total harga dari bensin 
# 7. output nama kendaraan, jenis bensin, kota tujuan, pemakaian bensin dan total harga 
# 8. selesai

nama_kendaraan = input("Nama Kendaraan (contoh: mobil, motor): ")
jenis_bensin = input("Jenis Bensin (pertalite, pertamax, pertamax turbo): ")
kota_tujuan = input("Kota yang Dituju (jakarta, bekasi, depok, tangerang, bogor): ")


harga_per_liter = 0
jarak_tempuh = 0
if jenis_bensin == "pertalite" or jenis_bensin == "1":
    harga_per_liter = 10000
    jarak_tempuh = 12
elif jenis_bensin == "pertamax" or jenis_bensin == "2":
    harga_per_liter = 14000
    jarak_tempuh = 13
elif jenis_bensin == "pertamax turbo" or jenis_bensin == "3":
    harga_per_liter = 17000
    jarak_tempuh = 13.5
else:
    print("jenis bensin tidak ada")
    

jarak_kota_tujuan = 0
if kota_tujuan == "jakarta":
    jarak_kota_tujuan = 20
elif kota_tujuan == "bekasi":
    jarak_kota_tujuan = 35.7
elif kota_tujuan == "depok":
    jarak_kota_tujuan = 5
elif kota_tujuan == "tangerang":
    jarak_kota_tujuan = 99
elif kota_tujuan == "bogor":
    jarak_kota_tujuan = 120.6
else:
    print("kota tujuan tidak ada")


pemakaian_bensin = jarak_kota_tujuan / jarak_tempuh
total_harga = pemakaian_bensin * harga_per_liter

print(f"nama kendaraan: {nama_kendaraan}")
print(f"jenis bensin yang digunakan: {jenis_bensin}")
print(f"kota yang dituju: {kota_tujuan}")
print(f"pemakaian bensin: {pemakaian_bensin} liter")
print(f"total harga yang dikeluarkan Rp.{total_harga}")