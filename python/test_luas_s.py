from colorama import Fore, init

init(autoreset=True)

print(Fore.CYAN + '+--------------------------+')
print(Fore.GREEN + '| Menghitung Luas Segitiga |')
print(Fore.CYAN + '+--------------------------+ \n')

def luas_segitiga(a, t):
    luas = 1/2 * (a * t)
    return luas

while True:
    alas = input('Masukan alas: ')
    tinggi = input('Masukan tinggi: ')

    try:
        a = int(alas)
        t = int(tinggi)

        luas = luas_segitiga(a, t)
        print('luas segitiga = ', luas)
        break
    except ValueError:
        print(Fore.RED + 'Coba Lagi!! \n')
