def hitung(operasi, x, y):
    if operasi == 'penjumlahan':
        return x + y
    elif operasi == 'pengurangan':
        return x - y
    elif operasi == 'perkalian':
        return x * y
    elif operasi == 'pembagian':
        if y != 0:
            return x / y
        else:
            print('Error: Pembagian dengan nol tidak diizinkan.')
            return None
    else:
        print('Operasi tidak valid.')
        return None

def kalkulator():
    print('Pilih Operasi')
    print('1. Penjumlahan')
    print('2. Pengurangan')
    print('3. Perkalian')
    print('4. Pembagian')

kalkulator()
pilihan = int(input('Masukkan pilihan 1/2/3/4 = '))

if 1 <= pilihan <= 4:
    x = int(input('Masukkan bilangan pertama: '))
    y = int(input('Masukkan bilangan kedua: '))
    hasil = hitung(
        'penjumlahan' if pilihan == 1 else
        'pengurangan' if pilihan == 2 else
        'perkalian' if pilihan == 3 else
        'pembagian',
        x, y
    )

    if hasil is not None:
        print(f'Hasil: {hasil}')
else:
    print('Operasi tidak valid')
