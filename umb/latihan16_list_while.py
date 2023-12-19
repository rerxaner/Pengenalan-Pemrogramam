list_provinsi = [
    'aceh',
    'bengkulu',
    'jambi',
    'lampung',
    'riau',
    'padang',
    'palembang',
    'medan'
]

nama_provinsi = input('Masukan nama provinsi: ')

i = 0
while i < len(list_provinsi):
    provinsi = list_provinsi[i]
    if provinsi == nama_provinsi:
        print('Provinsi yang dicari berada diindex ke-', i)
        break
    i += 1

else:
    print('Provinsi yang dicari tidak ditemukan')