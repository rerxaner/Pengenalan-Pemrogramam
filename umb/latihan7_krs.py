import datetime

tanggal = datetime.datetime.now()

print("KARTU RENCANA STUDI")
print("*******************")

nama = input("Nama: ")
npm = int(input("NPM: "))

print("Prodi: Teknik Informatika")
print("semester: 1")

print("Mata Kuliah:")
mata_kuliah_1 = input("1: ")
mata_kuliah_2 = input("2: ")
mata_kuliah_3 = input("3: ")
mata_kuliah_4 = input("4: ")

total_mata_kuliah = [mata_kuliah_1, mata_kuliah_2, mata_kuliah_3, mata_kuliah_4]
print("Total Mata Kuliah yang diambil: ", len(total_mata_kuliah), "\n")

print("Bengkulu, %a/%a/%a"% (tanggal.day, tanggal.month, tanggal.year))

print("Mahasiswa", "\n")
print(nama)
print(npm)

