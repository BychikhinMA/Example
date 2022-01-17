import random
import time
import os #  позволяет импортировать модуль с функциями самой операционной системы

number1 = random.randint(1, 3) # данная функция позволяет выводить рандомные числа в указанном диапазоне
number2 = random.randint(1, 3)
number3 = random.randint(1, 3)

os.system('clear')
print(number1)
time.sleep(1)  # данная импортируемый модуль time  с функцией sleep позволяет создать задержку перед выполнением кода
os.system('clear')
print(number2)
time.sleep(2)
os.system('clear')
print(number3)

numb1 = random.random() # данная функция позволяет выводить случайные десятичные числа
numb2 = random.random()
numb3 = random.random()

os.system('clear') # позволяет задействовать функцию системы очистки терминала (clear)

print(numb1)
print(numb2)
print(numb3)