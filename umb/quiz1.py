# NPM(dalam bentuk komentar)
# (tambahan karakter new line)
# No Struk: # 1
# Nama Kasir:
# Barang 1:
# Harga Barang Rp:
# Barang 2:
# Harga Barang 2:
# Barang 3:
# Harga Barang 3:
# --------------------
# Total Bayar Rp 
# (Tamabh karakter new line)
# TERIMA KASIH SUDAH BERBELANJA DI TOKO KAMI

import datetime

x = datetime.datetime.now()

# npm : 2355201085
no_struk = int(input("No Struk : "))
nama_kasir = input("Nama Kasir : ")
barang1 = input("Barang 1 : ")
harag_barang_1 = int(input("Harga Barang 1 Rp : "))
barang2 = input("Barang 2 : ")
harag_barang_2 = int(input("Harga Barang 2 Rp : "))
barang3 = input("Barang 3 : ")
harag_barang_3 = int(input("Harga Barang 3 Rp : "))

total_barang = (barang1, barang2, barang3)

print("----------------------------------------------")
print("Total Barang : ", len(total_barang))
print("Total Bayar Rp : ", harag_barang_1 + harag_barang_2 + harag_barang_3, "\n")

print("Kasir,")
print(nama_kasir)

print("Bengkulu, %a/%a/%a"% (x.day, x.month, x.year))

print("TERIMA KASIH SUDAH BERBELANJA DI TOKO KAMI")

