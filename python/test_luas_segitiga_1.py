alas = float(input('Masukan alas: '))
tinggi = float(input('Masukan tinggi: '))

luas = 1/2 * (alas * tinggi)

# fungsi round() digunakan untuk membuatkan nilai numerik.
# angka 2 dalam round(luas,2) yaitu untuk membulatkan nilai luas
# menjadi dua digit dibelakang koma
print('luas segitiga = ', round(luas,2))