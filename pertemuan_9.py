# soal 1
# Buatlah sebuah fungsi bernama celcius_ke_fahrenheit yang menerima satu argumen: suhu dalam celcius. Fungsi ini harus mengembalikan suhu yang dikonversi ke Fahrenheit.
# print(celcius_ke_farenheit(0)) 
# # Output: 32.0
# print(celcius_ke_farenheit(100))
# print Output: 212.0

def celcius_ke_farenheit(celcius):
    hasil_koversi = (celcius * 9/5) + 32
    return hasil_koversi

print(celcius_ke_farenheit(0))
print(celcius_ke_farenheit(100))

print("==============================")
print("==============================")
print("==============================")





# soal 2
# Buatlah sebuah fungsi bernama is_genap yang menerima satu argumen: bilangan bulat. Fungsi ini harus mengembalikan True jika bilangan tersebut genap, dan False jika bilangan tersebut ganjil.
# print(is_genap(4))
# Output: True
# print(is_genap(7))
# Output: False

def is_genap(angka):
    hasil = angka  % 2 == 0
    return hasil

genap = 4
print(f" Output dari bilangan {genap} adalah {is_genap(genap)}")
print(is_genap(13))

print("==============================")
print("==============================")
print("==============================")




# soal 3
# Buatlah fungsi untuk melihat ketrangan lulus atau tidak lulus : 
# nilai (80) #lulus
# nilai(60) #gagal

def nilai_kelulusan(nilai):
    print()
    if nilai >= 80:
        return 'lulus'
    else:
        return 'gagal'
print(nilai_kelulusan(80))
print(nilai_kelulusan(60))

print("==============================")
print("==============================")
print("==============================")




# soal 4
# Buatlah fungsi untuk menampilkan bilangan ganjil yang kurang argumens
# bilangan(20) # 1,3,5,7,9,11,13,15,17,19

def bilangan(n):
    for i in range(1, n):
        if i % 2 != 0:
            print(i, end=", ")
    print()
bilangan(20)

print("==============================")
print("==============================")
print("==============================")


  

# soal tambahan
# ini tantangan kalo bisa pulang
# output syamil bisa pulang apa tidak
def ddp(ketentuan):
    if ketentuan == 'bisa':
        print("syamil pulang")
    elif ketentua == 'gagal':
        print("syamil tidak pulang")
    else:
        print("inputan tidak valid")


ddp("bisa")