import datetime

waktu = datetime.datetime.now()

def hitung_harga():
    x = 0
    while True:
        nama = input('Nama Barang: ')
        if nama == str(x):
            break
        harga = float(input('Masukkan Harga: '))
        if harga == x:
            break
        x += harga
    return x

def perusahaan():
    global waktu
    print('Apotek Merpati')
    print('Rawa Makmur, Bengkulu, 0895410070077')
    print('KASIR 1 %a/%a/%a' %(waktu.day, waktu.month, waktu.year))
    print('RJJ-12345 %a:%a:%a' %(waktu.hour, waktu.minute, waktu.second))

total_harga = hitung_harga()


if total_harga > 0:    
    if total_harga >= 150000:
        diskon = total_harga * (10/100)
        DISKON = "{:,.2f}".format(diskon).replace(",", ".")
        total_harga_diskon = total_harga - diskon
        sub_total = "{:,.2f}".format(total_harga_diskon).replace(",", ".")
        bayar = int(input('Jumlah Pembayaran: ')) 
        kembali = bayar - total_harga_diskon 
        perusahaan()
        print('DISKON:', DISKON[:-3] + ',00')
        print('TOTAL:', sub_total[:-3] + ',00')
        print('BAYAR:', bayar)
        print('KEMBALI:', kembali)
    else:
        perusahaan()
        sub_total = "{:,.2f}".format(total_harga).replace(",", ".")
        print('Total:', sub_total[:-3] + ',00')
else:
    pass