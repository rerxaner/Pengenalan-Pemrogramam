import datetime

x = datetime.datetime.now()

print('Bengkulu, %a/%a/%a'% (x.day, x.month, x.year), '%d:%d:%d'% (x.hour, x.minute, x.second))