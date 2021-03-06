print('Цикл While')
#While condition:
    #code
#до тех пор пока условие выполняется:
    #код цикла

# Цикл while означает - до тех пор пока условие condition будет возвращать True, 
# нужно выполнить код в теле цикла. Условие condition называется - условие цикла.

#Самый простой пример цикла while - это вечный цикл:
#while True:
    #pass
#Этот цикл будет выполняться всегда, потому что в качестве условия мы написали True - истина
#В отличие от цикла for, в цикле while нам самим нужно контролировать счетчик цикла. 

numbers = [101, 202, 505,]

i = 0   # создание переменной i - счетчик цикла
while i < len(numbers): # Создаем цикл While, 
                        # Условием цикла является выражение i < len(numbers) - 
                        # пока это выражение возвращает True, то цикл выполняется. 
    number = numbers[i] # В теле цикла создаем переменную number - элемент списка numbers по индексу i
    if number % 2 == 0: # Далее делаем проверку на четност
        print(number)
    i += 1  # Увеличиваем счетчик цикла на 1, чтобы на следующей итерации получить второй элемент из списка.
print('Конец программы!')

print('--------')

print('Операторы break и continue')

#break (от англ. break - прервать) - прервать цикл и 
# continue (от англ. continue - продолжить) - перейти к следующей итерации без выполнения нижележащего кода.

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

i = 0

for number in numbers:
    if number == 0:
        print('Нашли на итерации', i + 1)
    i += 1
print('Всего итераций выполненно:', i)

print('-----------')
# Сократим и добавим оператор Break

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

i = 0

for number in numbers:
    if number == 0:
        print('Нашли на итерации', i + 1)
        break
    i += 1
print('Всего итераций выполненно:', i)
# не рекомендуется использовать Break если без него можно обойтись. 
# Использование оператора break снижает читаемость кода и увеличивает шанс возникновения ошибки.
print('---------')

# Поиск значения циклом While(Самый верный способ)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

i = 0
found = False

while i < len(numbers) and not found:   # написали цикл while и в условие цикла передаем выражение, состоящее из двух частей
    if numbers[i] == 0:
        print('Нашли на итерации', i + 1)
        found = True
    i += 1
print('Всего итераций выполнено', i)
