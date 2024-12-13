from Animal import Animal

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, sirip_ekor, warna):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.sirip_ekor = sirip_ekor
        self.warna = warna

    def info_ikan(self):
        super().info_animal()
        print("Sirip ekor \t\t : ", self.sirip_ekor,
              "\nWarna \t\t\t : ", self.warna)
        
print("=============================")

Ikan_nila= Ikan("Nila","Larva","Air","Bertelur","Bulat","Hitam keabuan")
Ikan_nila.info_ikan()

print("==============================")

Ikan_gabus = Ikan("Gabus","Katak","Air","Bertelur","Panjang","Hijau kehitaman")
Ikan_gabus.info_ikan()