print('Menghitung Keliling Lingkran')
print('----------------------------')

def kelililing_lingkran(r):
    rumus_keliling = 2 * 3.14 * r
    return rumus_keliling

while True:
    radius = input('Masukan Jari-jari = ')

    try:
        r = float(radius)

        hasil_keliling = kelililing_lingkran(r)
        print('Keliling = ', round(hasil_keliling, 2))
        break
    except ValueError:
        print('Ulangi lagi!!')