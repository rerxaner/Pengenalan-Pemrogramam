import numpy as np

print('Menghitung luas segitiga')
print('------------------------')

a = float(input('Sisi pertama = '))
b = float(input('Sisi kedua = '))
c = float(input('Sisi ketiga = '))

s = 1/2 * (a + b + c)
luas = np.sqrt(s * (s - a) * (s - b) * (s - c))

print('Luas Segitiga = ', round(luas, 2))