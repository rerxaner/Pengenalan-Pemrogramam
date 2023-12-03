nama = input("Masukan nama anda: ")
tahun = int(input("Tahun berapa anda lahir: "))

if tahun >= 1944 and tahun <= 1964:
    print(f"{nama}, berdasarkan tahun kelahiran anda termasuk Baby boomer")
elif tahun >= 1965 and tahun <= 1979:
    print(f"{nama}, berdasarkan tahun kelahiran anda termasuk Generasi X")
elif tahun >= 1980 and tahun <= 1994:
    print(f"{nama}, berdasarkan tahun kelahiran anda termasuk Generasi Y")
elif tahun >= 1995 and tahun <= 2015:
    print(f"{nama}, berdasarkan tahun kelahiran anda termasuk Generasi Z")
else:
    print(f"{nama}, berdasarkan tahun kelahiran anda termasuk Generasi Tidak Diketahui")
