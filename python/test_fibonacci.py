# Fibonacci Squence adalah deret angka yang diperoleh
# dengan menjumlahkan dua angka sebelumnya.
# Multiple Assignment memungkinkan dua variabel
# untuk mendapatkan nilai baru mereka dalam satu operasi.
a = 0
b = 1
while a < 100:
    print(a)
    # a, b = b, a+b # baris ini disebut multiple assignment
    temp = a
    a = b
    b = temp + b
