import math
from colorama import Fore, init

init(autoreset=True)

print(Fore.BLUE + '+-----------------------------------+')
print(Fore.RED + '| Menghitung Jarak antara dua titik |')
print(Fore.BLUE + '+-----------------------------------+')

def jarak_dua_titik(x1, y1, x2, y2):
    rumus_jarak = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return rumus_jarak

while True:
    try:
        x1 = int(input('X1 = '))
        y1 = int(input('Y1 = '))
        x2 = int(input('X2 = '))
        y2 = int(input('Y2 = '))

        hitung_jarak = jarak_dua_titik(x1, y1, x2, y2)
        print('Jarak =', hitung_jarak)
        break
    except ValueError:
        print('Ulangi!!')