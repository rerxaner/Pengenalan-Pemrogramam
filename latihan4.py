x = input("Masukkan nilai pertama : ")
y = input("Masukkan nilai kedua : ")

try:
	i = int(x)
	j = int(y)
except ValueError:
	try:
		i = float(x)
		j = float(y)
	except ValueError:
		print("Masukkan nilai yang benar!!!")
	else:
		print(f'{x} + {y} =', i + j)
		print(f'{x} - {y} =', i - j)
		print(f'{x} x {y} =', i * j)
		print(f'{x} ** {y} =', i ** j)
		if j != 0:
			print(f'{x} / {y} =', i / j)
			print(f'{x} // {y} =', i // j)
			print(f'{x} % {y} =', i % j)
		else:
			print('Tidak dapat melakukan operasi pembagian NOL !!!')
else:
	print(f'{x} + {y} =', i + j)
	print(f'{x} - {y} =', i - j)
	print(f'{x} x {y} =', i * j)
	print(f'{x} ** {y} =', i ** j)
	if j != 0:
		print(f'{x} / {y} =', i / j);
		print(f'{x} // {y} =', i // j);
		print(f'{x} % {y} =', i % j)
	else:
		print('Tidak dapat melakukan pembagian dan persen dengan NOL !!!')
