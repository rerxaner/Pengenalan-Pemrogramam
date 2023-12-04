import datetime
from colorama import Fore, Back, Style, init

init(autoreset=True)

print(Style.BRIGHT + "LEMBAR HASIL STUDI")
print("Nama : Rahman Badio")
print("NPM : 2355201085")
print(Style.BRIGHT + "--------------------------", '\n')

a, b, c = 4, 3, 2
sks = 3
print("A : {}\nB : {}\nC : {}\nSKS : {}".format(a,b,c,sks), '\n')

print(f"1. Logika Matematika : {sks} sks")
nilai_a = float(input("Nilai Logika Matematika : "))
print(f"2. Pemrograman : {sks} sks")
nilai_b = float(input("Nilai Pemrograman : "))

total_nilai = (nilai_a + nilai_b) * sks
index_prestasi = total_nilai / (sks * 2)
tanggal = datetime.datetime.now()

print('Total Nilai =', Back.MAGENTA + str(round(total_nilai, 2)))

if index_prestasi >= 3.5 or index_prestasi == 4:
    print('Index Prestasi =', Fore.GREEN + 'A')
elif index_prestasi >= 3:
    print('Index Prestasi =', Fore.CYAN + 'B')
elif index_prestasi >= 2:
    print('Index Prestasi =', Fore.YELLOW + 'C')
else:
    print('Index Prestasi =', Fore.RED + 'D')

print('\n')
print(tanggal.strftime("Bengkulu, %d-%m-%Y"))
print("Prodi : Teknik Informatika")