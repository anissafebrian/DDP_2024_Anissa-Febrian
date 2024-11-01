# 5. buat program python untuk mencari luas dan keliling tabung

#input
jari_jari = float(input("Masukkan jari-jari tabung: "))
tinggi = float(input("Masukkan tinggi tabung: "))

#proses
luas_permukaan = 2 * 22/7 * jari_jari * (jari_jari + tinggi)
keliling_alas = 2 * 22/7 * jari_jari

print(f"Luas permukaan tabung: {luas_permukaan:.2f}")
print(f"Keliling alas tabung: {keliling_alas:.2f}")