nama = input("Masukan nama anda: ")
ttl = int(input("Tahun berapa anda lahir: "))

if ttl >= 1944 and ttl <= 1964:
    print(f"{nama}, berdasarkan tahun kelahiran anda termasuk Baby boomer")
elif ttl >= 1965 and ttl <= 1979:
    print(f"{nama}, berdasarkan tahun kelahiran anda termasuk Generasi X")
elif ttl >= 1980 and ttl <= 1994:
    print(f"{nama}, berdasarkan tahun kelahiran anda termasuk Generasi Y")
elif ttl >= 1995 and ttl <= 2015:
    print(f"{nama}, berdasarkan tahun kelahiran anda termasuk Generasi Z")
else:
    print(f"{nama}, berdasarkan tahun kelahiran anda termasuk Generasi Tidak Diketahui")
