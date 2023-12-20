class Animal:
    def __init__(self,nama,makanan,hidup,berkembangBiak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembangBiak = berkembangBiak


    def tampilkan(self):
        print(f'saya {self.nama}, makanan saya {self.makanan}, saya hidup di {self.hidup}, dan saya berkembangbiak dengan {self.berkembangBiak} ')
        
# 1.
class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembangBiak,bergerak):
        super().__init__(nama, makanan, hidup, berkembangBiak)
        self.bergerak = bergerak
     
    def print(self):
        super().tampilkan
        print(f'saya bergerak dengan {self.bergerak}')


# 2.
class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembangBiak,bergerak):
        super().__init__(nama, makanan, hidup, berkembangBiak)
        self.bergerak = bergerak
  
    def print(self):
        super().tampilkan
        print(f'saya bergerak dengan {self.bergerak}')


# 3. 
class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembangBiak,bergerak):
        super().__init__(nama, makanan, hidup, berkembangBiak)
        self.bergerak = bergerak

    def print(self):
        super().tampilkan
        print(f'saya bergerak dengan {self.bergerak}')

    

# objek burung
x = Burung('merpati','biji-bijian','udara','bertelur','terbang')
x.tampilkan()
x.print()


print()

# objek ikan
y = Ikan('koi','cacing sutra','air','bertelur','berenang')
y.tampilkan()
y.print()


print()

# objek ular
z = Ular('python','katak','darat','bertelur', 'merayap')
z.tampilkan()
z.print()