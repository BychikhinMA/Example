# Генератор списков
# генератор списков - это конструкция, которая создает список. 
# Генератор списков имеет следующий синтаксис:
#новый_список = [выражение for элемент in список]

import datetime

count = 10000000
fake_list1 = []
fake_list2 = []

start = datetime.datetime.now()
for number in range(count):
    fake_list1.append(number)
time1 = datetime.datetime.now() - start
print('С помощью цикла:', time1)

start = datetime.datetime.now()
fake_list2 = [number for number in range(count)]
time2 = datetime.datetime.now() - start
print('С помощью генератора:', time2)

print('Выигрыш времени в процентах:', (time1 - time2) / time1 * 100)



numbers = [100, 101, 200, 201, 300, 301]

even_numbers = [number for number in numbers if number % 2 == 0]
odd_numbers = [number for number in numbers if number % 2 != 0 ]

print(even_numbers)
print(odd_numbers)

numbers = [100, 101, 200, 201, 300, 301]

even_numbers = ['двести' if number == 200 else number for number in numbers if number % 2 == 0]

print(even_numbers)