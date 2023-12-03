import datetime

print("LEMBAR HASIL STUDI")
print("Nama : Rahman Badio")
print("NPM : 2355201085")
print("-------------------")

a, b, c = 4, 3, 2
sks = 3
print("A : {}\nB : {}\nC : {}\nSKS : {}".format(a,b,c,sks))

print(f"1. Logika Matematika : {sks} sks")
nilai_a = int(input("Nilai Logika Matematika : "))
print(f"2. Pemrograman : {sks} sks")
nilai_b = int(input("Nilai Pemrograman : "))

total_nilai = (nilai_a + nilai_b) * sks
index_prestasi = total_nilai / (sks * 2)
tanggal = datetime.datetime.now()

print(f"Total Nilai = {total_nilai}")
print(f"Index Prestasi = {index_prestasi} \n")
print(tanggal.strftime("Bengkulu, %d-%m-%Y"))
print("Prodi : Teknik Informatika")