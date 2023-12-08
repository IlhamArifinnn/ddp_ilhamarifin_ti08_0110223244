def segitiga(alas: int,tinggi: int, sisi: int):
    luas = (alas * tinggi) / 2
    keliling = sisi + sisi + sisi
    print(f'luas segitiga dengan alas {alas} dan tinngi {tinggi} = {luas}')
    print(f'keliling segitiga dengan sisi {sisi} = {keliling}')

def persegi(s: int):
    luas = s * s
    keliling = 4 * s
    print(f'luas persegi dengan panjang sisi {s} = {luas}')
    print(f'keliling persegi dengan panjang sisi {s} = {keliling}')

def persegi_panjang(p: int,l: int):
    luas = p * l
    keliling = 2 * (p + l)
    print(f'luas persegi panjang dengan panjang {p} dan lebar {l} = {luas}')
    print(f'keliling persegi panjang dengan panjang {p} dan lebar {l} = {keliling}')

def belah_ketupat(d1: int,d2: int,sisi: int):
    luas = (d1 * d2) / 2
    keliling = sisi + sisi + sisi + sisi
    print(f'luas belah ketupat dengan panjang diagonal1 {d1} dan diagonal2 {d2} = {luas}')
    print(f'keliling belah ketupat dengan sisi {sisi} = {keliling}')

def jajar_genjang(a: int,t: int,sisi: int):
    luas = a * t
    keliling = sisi + sisi + sisi + sisi
    print(f'luas jajar genjang dengan alas {a} dan tinggi {t} = {luas}')
    print(f'keliling jajar genjang dengan sisi {sisi} = {keliling}')

def lingkaran(r:int):
    luas = 3.14 * r * r
    keliling = 2 * 3.14 * r
    print(f'luas lingkaran dengan jari-jari {r} = {luas}')
    print(f'keliling lingkaran dengan jari-jari {r} = {keliling}')

def trapesium(a,b,t,sisi):
    luas = (a + b) * t / 2
    keliling = sisi + sisi + sisi + sisi
    print(f'luas trapesium dengan sisi {a}, {b} dan tinggi {t} = {luas}')
    print(f'keliling trapesium dengan sisi {sisi} = {keliling}')