umur = int(input("Masukan umur anda: "))

if umur < 1:
    print('Bayi')
elif umur < 3:
    print('Batita')
elif umur < 5:
    print('Balita')
elif umur < 12:
    print('Anak-Anak')
elif umur < 27:
    print('Remaja')
elif umur < 30:
    print('Pemuda')
elif umur < 60:
    print('Dewasa')
else:
    print('Lansia')