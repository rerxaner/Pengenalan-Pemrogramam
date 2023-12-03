nama_karyawan = input("Masukan nama karywana: ")
gaji_pokok = float(input("Masukan gaji pokok: "))
tunjangan = float(input("Masukan gaji tunjangan: "))

gaji_kotor = gaji_pokok + tunjangan

if gaji_kotor >= 5000000:
    gaji_bersih = gaji_kotor * (8/100)
    print("Gaji pokok dan tunjangan anda dikenakan pajak 5% dan BPJS 3%", gaji_bersih)
else:
    gaji_bersih = gaji_kotor * (4/100)
    print("Gaji pokok dan tunjagan anda dikenakan pajak 3% dan BPJS 1%", gaji_bersih)
