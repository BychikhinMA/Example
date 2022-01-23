#  Исключения

try:
    a = 1 / 0
except ZeroDivisionError:
    print('Ошибка деления на 0. Выходим')
except Exception as e:
    print('Неизвестная ошибка')
else:
    print('Все хорошо!')
finally:
    print('Я выполню в любом случае')

# Try/Except Попытка/ Исключение 

print('Начало программы!')

try:
    a = 1 / 0
except:
    a = 0
print('a =', a)
print('Конец программы')

print('Начало программы!')

try: 
    a = 1 / 0
except:
    print('Ошибка') # В сообщениях об ошибках всегда нужно писать содержательное объяснение почему ошибка возникла
    a = 0
print('КОнец программы')


print('Начало программы!')

try: 
    a = 1 / 0
except Exception as e: # Exception - оператор который позволяет понять в чем ошибка.
    #  Через " as e" мы превращаем Exception в объект, который позволит понять в чем именно ошибка
    print('Ошибка', e)
    a = 0
print('КОнец программы')



all_money = 1000
workers = 0

try:
    each_money = all_money / workers
except Exception as e:
    print('Ошибка', e)
    print('Общее количество сотрудников = 0')
    each_money = -1
print('Сумма с каждого сотрудника =', each_money)



# Усложнение задачи с получением данных из словаря

boss_birthday = {
    'all_money': 1000,
    'workers': 0
}

try:
    each_money = boss_birthday['all_money'] / boss_birthday['workers']
except Exception as e:
    print('Ошибка', e)
    print('Общее количество сотрудников = 0.')
    each_money = -1

print('Сумма с каждого сотрудника:', each_money)


boss_birthday = {
    'workers': 10
}

try:
    each_money = boss_birthday['all_money'] / boss_birthday['workers']
except KeyError as e:
    print('В словаре boss_birthday отсутствует ключ', e)
    each_money = -1
except ZeroDivisionError as e:
    print('Общее количество сотрудников = 0.', e)
    each_money = -1
except Exception as e:
    print('Неизвестная ошибка:', e)
    each_money = -1

print('Сумма с каждого сотрудника:', each_money)