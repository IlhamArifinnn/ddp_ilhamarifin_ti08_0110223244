hasil_akhir = [
    {'nama': 'Reza', 'nilai': 70},
    {'nama': 'Ciut', 'nilai': 63},
    {'nama': 'Dian', 'nilai': 80},
    {'nama': 'Badu', 'nilai': 40}
]
def lulus_aja(skor):
    siswa_lulus = []
    for siswa in skor:
        if siswa['nilai'] > 65:
            siswa_lulus.append(siswa['nama'])
    return siswa_lulus
print(lulus_aja(hasil_akhir))


print()
print('======= 1 =======')
buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
def kebalikan (nama_buah):
    keranjang = []
    for isi in range(len(nama_buah)):
        nama = isi + 1
        keranjang.append(nama_buah[-(nama)])
    return keranjang
print(kebalikan(buah))


print()
print('====== 2 =======')
buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
def copy(nama_buah):
    keranjang = []
    for item in nama_buah:
        keranjang.append(item)
        keranjang.append(item)
    return keranjang
print(copy(buah))


print()
print('====== 3 =======')
kalimat = 'Nurul Fikri'
abjad = ['a', 'i', 'u', 'e', 'o', ' ']
def konsonan(data):
    huruf = []
    for item in data:
        if item not in abjad:
            huruf += item
    return huruf
print(konsonan(kalimat))