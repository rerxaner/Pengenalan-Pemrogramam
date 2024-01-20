kalimat = input('Masukan satu kalimat: ')
jumkar = {}
for kar in kalimat:
    jumkar[kar] = jumkar.get(kar, 0) + 1

# Tampilkan Frekuensi karakter
for kar, frekuensi in jumkar.items():
    if kar == ' ':
        print(f'Spasi = {frekuensi}')
    else:
        print(f'{kar} = {frekuensi}')