nama = ['Rahman', 'Dion', 'Adam', 'Genathan', 'Yulius', 'Andreza', 'Ahmad', 'Bryan', 'Dean', 'Ferdi', 'Egi', 'Afrizal', 'Kevin']

print(type(nama))

# menghitung jumlah string didalam list
for teman in range(len(nama)):
    print(teman, nama[teman])

print('\n')

# menghitung jumlah words dalam nama teman setiap string
for huruf in nama:
    print(huruf, len(huruf))