import datetime

print("LEMBAR HASIL STUDI")
print("Nama : Rahman Badio")
print("NPM : 2355201085")
print("------------------------")

A = 4
print("A :", A)
B = 3
print("B :", B)
C = 2
print("C :", C)
SKS = 3
print("SKS : ", SKS)

print("1. Logika Matematika : ", SKS, "sks")
nilai_a = int(input("Nilai Logika Matematika : "))
print("2. Pemrograman : ", SKS, "sks")
nilai_b = int(input("Nilai Pemrograman : "))

total_nilai = (nilai_a * SKS) + (nilai_b * SKS)
print("Total Nilai = ", total_nilai)

index_prestasi = total_nilai / (SKS * 2)
print("Index Prestasi = ", index_prestasi)

print("\n")

x = datetime.datetime.now()
print("Bengkulu, %a-%a-%a"% (x.day, x.month, x.year))
print("Prodi : Teknik Informatika")