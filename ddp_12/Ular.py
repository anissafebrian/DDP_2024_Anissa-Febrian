from Animal import Animal

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, ukuran, warna):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.ukuran = ukuran
        self.warna = warna

    def info_ular(self):
        super().info_animal()
        print("Ukuran \t\t\t: ", self.ukuran,
              "\nWarna \t\t\t: ", self.warna)
print("===============================")

Ular_sanca_hijau = Ular("Sanca hijau", "Tikus, Burung, Kadal dll", "Hutan", "Bertelur", "2 meter", "Hijau")
Ular_sanca_hijau.info_ular()

print("================================")

Ular_kadut = Ular("Ular kadut", "belut, kepiting udang dll", "Air", "Bertelur", "2,4 meter", "Cokelat")
Ular_kadut.info_ular()