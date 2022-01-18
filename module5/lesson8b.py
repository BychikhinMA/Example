# Чистка коллекций

# Использование FOR
print('Чистка коллекций')

letters = ['a', 'b']

for letter in letters:
    letters.remove(letter)

print('Список после чистки', letters)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

for letter in letters:
    letters.remove(letter)

print('Список после чистки', letters)


# Использование метода While

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
i = 3
while i < len(letters):
    letters.remove(letters[i])

print('Список после чистки', letters)

numbers = [100, 101, 200, 201, 300, 301, ]

i = 0
while i < len(numbers):
    number = numbers[i]
    if number % 2 == 0:
        numbers.remove(number)
    else:
        i += 1
print('Список после чистки: ', numbers)

# В теле списке мы создаем переменную number - текущий элемент списка. 
# Затем мы проверяем число number на четность. 
# Если оно нечетное, то удаляем его, при этом, важно: 
# не увеличиваем счетчик цикла i.
#  Счетчик i увеличиваем только в том случае, если элемент не удаляется 
# - это правило чистки коллекций, запомни его.