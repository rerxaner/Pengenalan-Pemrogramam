while True:
    panjang = input("Masukan Panjang: ")
    lebar = input("Masukan Lebar: ")

    if panjang.isnumeric() and lebar.isdigit():
        P = int(panjang)
        L = int(lebar)
        break
    else:
        print("Masukkan angka!!! Coba lagi..")

luas = P * L
print("Hasil = ", luas)