import math

print('Menghitung luas segitiga sembarang')
print('------------------------')

def luas_segitiga_sembarang(a, b, c):
    s = (a+b+c) / 2
    luas = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return luas

while True:
    A = input('Sisi pertama = ')
    B = input('Sisi kedua = ')
    C = input('Sisi ketiga = ')

    try:
        a = float(A)
        b = float(B)
        c = float(C)

        luas = luas_segitiga_sembarang(a, b, c)
        print('Luas =', round(luas, 2))
        break
    except ValueError:
        print('Masukan bilangan!!')