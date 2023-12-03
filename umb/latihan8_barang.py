hargaSabun = int(input("Masukan Harga Sabun: Rp "))
hargaSampo = int(input("Masukan Harga Sampo: Rp "))
hargaMinyak = int(input("Masukan Harga Minyak: Rp "))

totalBelanja = hargaSampo + hargaSabun + hargaMinyak

if totalBelanja >= 150000:
    print("Kamu Mendapat Diskon 10%")
    diskon = totalBelanja * (10/100)
    print("Total diskon 10% :", diskon)
    bayar = totalBelanja - diskon
    print("Total yang harus dibayar Rp %s" %bayar)

if totalBelanja < 150000:
    print("Kamu Mendapatkan permen")
    print("Total yang harus dibayar Rp %s" %totalBelanja)