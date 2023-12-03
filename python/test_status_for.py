users = {'Rahman': 'active', 'Afrizal': 'inactive', 'Egi': 'active', 'Kevin': 'inactive'}

print(type(users))

for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
        print('Pemain {} sedang {}'.format(user, status))

active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
        print('Pemain {} sedang {}'.format(user, status))