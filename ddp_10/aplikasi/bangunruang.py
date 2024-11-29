import math

# Deklarasi fungsi

def l_balok(p, l, t):
    hitung = 2 * (p*l)+(p*t)+(l*t)
    print(f'Luas balok adalah {hitung}')

def l_kubus(sisi):
    hitung = 6 * sisi ** 2
    print(f'Luas kubus adalah {hitung}')

def l_tabung(phi, jari_jari, tinggi):
    hitung = 2 * 3.14 * (jari_jari + tinggi)
    print(f'Luas tabung adalah {hitung}')

def l_limas(alas, sisi):
    hitung = alas + sisi
    print(f'Luas limas adalah {hitung}')

def l_prisma(alas, sisi):
    hitung = ( 2 * alas ) + sisi
    print(f'Luas prisma adalah {hitung}')
