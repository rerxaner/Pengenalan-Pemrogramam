import datetime

print("LEMBAR HASIL STUDI")
print("Nama : Rahman Badio")
print("NPM : 2355201085")

print("-----------------------------------------------------")

A = 4
print("A :", A)
B = 3
print("B :", B)
C = 2
print("C :", C)
SKS = 3
print("SKS : ", SKS)

sks_1 = 3
sks_2 = 3

print("1. Logika Matematika : ", sks_1, "sks")
nilai_a = int(input("Nilai Logika Matematika : "))
print("2. Pemrograman : ", sks_2, "sks")
nilai_b = int(input("Nilai Pemrograman : "))

nilai_1 = nilai_a * sks_1
nilai_2 = nilai_b * sks_2
total_nilai = nilai_1 + nilai_2
print("Total Nilai = ", total_nilai)

sks = sks_1 + sks_2
index_prestasi = total_nilai / sks
print("Index Prestasi = ", index_prestasi)

print("\n")

x = datetime.datetime.now()
print("Bengkulu, %a-%a-%a"% (x.day, x.month, x.year))
print("Prodi : Teknik Informatika")