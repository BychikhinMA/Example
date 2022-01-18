import random
import datetime


value = 10  # Число, которое мы ищем
fake_list = []  # Искомое значение

for _ in range(1000000):    # Используя цикл for, добавляем в лист fake_list 1 миллион случайных чисел:
    fake_list.append(random.randint(0, 1000))   # Добавляем диапозон поиска

start = datetime.datetime.now() # засекаем время старта:
    # Функция datetime.now() из модуля datetime возвращает текущую дату и время с миллисекундами.
found = False
for number in fake_list:    # Пишем поиск значения с помощью цикла for
    if number == value:
        found = True    # После цикла распечатываем результат поиска значения - переменную found:
print(found)

print(datetime.datetime.now() - start)  # считаем время выполнения цикла - из текущего времени вычитаем время старта

# Пишем новый код, но уже через оператор While
start = datetime.datetime.now()
found = False
i = 0
while i < len(fake_list) and not found:
    if fake_list[i] == value:
        found = True
    i += 1
print(found)
print(datetime.datetime.now() - start)
# Как итог мы можем увидеть в терминале разницу в работе циклов, цикл While отработал в 33 раза быстрее

# Это совсем не значит, что цикл while работает быстрее чем for - они работают одинаково эффективно, одинаково быстро.
#  Данный пример показывает разницу алгоритмов. 
# Для решения данной конкретной задачи - задачи поиска нужного значения, оптимальнее использовать цикл while. 
# Для других задач будет лучшим решением использовать цикл for. 
# Поэтому очень важно перед написанием кода составить алгоритм программы