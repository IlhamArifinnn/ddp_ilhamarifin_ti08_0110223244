# class / blue print / template
class Gempa:

# konstruktor
    def __init__(self,tempat,kekuatan):
        self.lokasi = tempat  # atribute
        self.skala = kekuatan # atribute
        
# method / instance
    def akibat(self):
        lokasi = self.lokasi
        if self.skala <= 2:
            print(f'dampak gempa {lokasi} tidak berasa')
        elif self.skala > 2 and self.skala <= 4:
            print(f'dampak gempa {lokasi} bangunan retak-retak')
        elif self.skala > 4 and self.skala <= 6:
            print(f'dampak gempa {lokasi} bangunan roboh')
        else :
            print(f'dampak gempa {lokasi} bangunan roboh dan berpotensi tsunami')

# object here