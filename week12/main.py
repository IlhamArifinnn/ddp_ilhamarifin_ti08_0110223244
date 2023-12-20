class Orang:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def cetak(self):
        print(f'nama saya {self.fname} {self.lname}')

class Mahasiswa(Orang):
    def __init__(self, fname, lname,prodi,angkatan):
        super().__init__(fname, lname)
        self.prodi = prodi
        self.angkatan = angkatan

    def tampilkan(self):
        super().cetak()
        print(f'prodi saya {self.prodi}')
        print(f'saya angkatan {self.angkatan}')

class Karyawan(Orang):
    def __init__(self, fname, lname,jabatan):
        super().__init__(fname, lname)
        self.jabatan = jabatan

    def print(self):
        super().cetak()
        print(f'jabatan saya {self.jabatan}')

# OBJEK ORANG
x = Orang('agus','suparman')
x.cetak()

# OBJEK MAHASISWA
y = Mahasiswa('imam','suprapto','ti',2023)
y.tampilkan()

#OBJEK KARYAWAN
z = Karyawan('budi','supomo','ob')
z.print()
