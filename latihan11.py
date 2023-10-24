# Soal
# Buatlah coding untuk menghitung luas lingkaran dan bujur sangkar, dimana jari jari dan sisi diinputkan oleh user

print("Menghitung Luas Lingkaran dan Bujur Sangkar")

r = float(input("Masukkan Jari Jari: "))
s = float(input("Masukkan Sisi: "))

phi = 3.14

luas_lingkaran = phi * r * r
luas_bujur_sangkar = s * s

print("Luas Lingkaran = ", luas_lingkaran)
print("Luas Bujur Sangkar = ", luas_bujur_sangkar)
