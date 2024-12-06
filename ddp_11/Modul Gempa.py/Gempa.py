class Gempa:
    lokasi = ''
    skala = ''

    # Contractor
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    # method/fungsi
    def dampak(self):
        if self.skala <2 :
            ket = 'Gempa tidak berasa'
        elif self.skala >=2 and self.skala <4 :
            ket = 'Bangunan retak'  
        elif self.skala >=4 and self.skala <6 :
            ket = 'Bangunan roboh'
        else :
            ket = 'bangunan Roboh dan berptensi tsunami'

        print('Lokasi gempa', self.lokasi, 
            '\nSkala skala', self.skala, 
            '\nDampak gempa', ket)