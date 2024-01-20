def hitung_luas_lingkaran():
    print('Menghitung luas lingkaran')
    radius = float(input('Jari-jari = '))
    luas = 3.14 * radius * radius
    print('Luas=', luas)

def hitung_luas_persegipanjang():
    print('Menghitung luas persegi panjang')
    panjang = float(input('Panjang = '))
    lebar = float(input('Lebar = '))
    luas = panjang * lebar
    print('Luas=', luas)
    
def hitung_luas_segitiga():
    print('Menghitung luas segitiga')
    alas = float(input('Alas = '))
    tinggi = float(input('Tinggi = '))
    luas = 1/2 * (alas * tinggi)
    print('Luas=', luas)
    
print('Menghitung luas')
print('1. Lingkaran')
print('2. Persegi Panjang')
print('3. Segitiga')

pilihan = int(input('Pilihan [1|2|3] : '))
if pilihan == 1:
    hitung_luas_lingkaran()
elif pilihan == 2:
    hitung_luas_persegipanjang()
elif pilihan == 3:
    hitung_luas_segitiga()
else:
    print('Pilihan salah')
