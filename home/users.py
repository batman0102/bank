from bank import *

Human = Bank2('Ruslan', 16, 9999, 'qwerty123')

print(Human.get_name())
Human.set_name('Alihan')
print(Human.get_name())
print()
print (int(Human.age))
Human.age = 17
print (int(Human.age))
print()
print(Human._Bank__money)
Human.money = 9998
print(int(Human.money))
print()
print(Human._Bank__key)
Human.key = '123qwerty'
print(Human.key)