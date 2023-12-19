cacah = 0
total = 0

data = int(input('Masukan data: '))

while data != -1: # -1 untuk berhenti
    cacah += 1
    total += data
    data = int(input('Masukan data lagi:'))
    
rerata = total / cacah

print('Rata rata', rerata)