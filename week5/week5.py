nama =["B 1234 LI","Zx25R","249.8 cc",
"Hijau"]

nama.append("100 JT")
nama.append("roda 2")

nama.insert(2,"Kawasaki ninja")
nama.insert(3,"sepeda motor")

print(nama)


hitung = input("1:persegi, 2:lingkaran, 3:segitiga")
match hitung:
    case 1 | "1" | "persegi"| "Persegi":
        s = int(input("Masukan panjang sisi ="))
        l_persegi = s*s
        print("luas persegi dengan panjang sisi", s ,"=",l_persegi)

    case 2 | "2" | "lingkaran" | "Lingkaran":
        r = int(input("masukan panjang jari-jari = "))
        l_lingkaran = 3,14 * r * r
        print("luas lingkaran dengan panjang jari-jari", r, "= ", l_lingkaran)

    case 3 | "3" | "segitiga" | "Segitiga":
        a = int(input("masukan panjang alas = "))
        t = int(input("masukan tinggi segitiga = "))
        l_segitiga = 0.5 * a * t
        print("luas segitiga dengan alas", a, "dan tinggi", t, "= ", l_segitiga)

    case _:
        print("anda salah memilih")
