list_provinsi = [
    'aceh',
    'bengkulu',
    'jambi',
    'lampung',
    'riau'
    'padang',
    'palembang',
    'medan'
]

nama_provinsi = input('Masukan nama provinsi: ')

for i, provinsi in enumerate(list_provinsi):
    if provinsi.lower() == nama_provinsi.lower():
        print('Provinsi yang di cari berda di index ke', i)
        break
else:
   print('Provinsi yang dicari tidak ditemukan')