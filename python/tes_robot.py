class Robot:
    jumlah_hidup = 0 # variabel kelas
    def __init__(self, nama):
        self.nama = nama
        Robot.jumlah_hidup += 1
    def __del__(self):
        Robot.jumlah_hidup -= 1
    def __info__(self):
        print('Robot :', self.nama)
        print('Robot hidup :', Robot.jumlah_hidup)

robotA = Robot('Rahman')
robotB = Robot('Yulius')   
robotC = Robot('Egi')
print('Robot Hidup',Robot.jumlah_hidup)

print(robotA.__info__())