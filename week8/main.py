print("====== 1 ======")
def profil(nama, alamat, gender, umur,hobi):
    print(f"Nama: {nama}")
    print(f"Alamat: {alamat}")
    print(f"Gender: {gender}")
    print(f"Umur: {umur}")
    print(f"Hobi: {hobi}")

profil("Ilham Arifin", "Depok", "Laki-laki", 19, "Bermain game & Belajar")


print()
print("====== 2 ======")
def kelulusan(nilai):
    if nilai < 60:
        print(f"{nilai}: Anda masih gagal")
    elif nilai >= 61 and nilai <= 70:
        print(f"{nilai}: Nilai anda Baik")
    elif nilai >= 71 and nilai <= 80:
        print(f"{nilai}: Nilai anda sangat baik") 
    elif nilai >= 81 and nilai <= 100:
        print(f"{nilai}: Nilai anda istimewa")
    else:
        print("Nilai anda tidak valid")
    
kelulusan(81)


print()
print("====== 3 ======")
def ganjil_genap(angka):
    for i in range(1, angka,2):
        print(i)

ganjil_genap(10)