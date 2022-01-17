my_string = 'а,б,В,Г,д,Д,д'

print(my_string.upper()) # перевод строки в врехний регистр
print(my_string.lower()) # перевод строки в нижний регистр
print(my_string.count('д')) # поиск символов под вторыми груглыми скобками с учетом его регистра
print(my_string.lower().count('д')) 
print(my_string.capitalize()) # Перевод только первого символа в верхний регистр, а остальных в нижний регистр

my_string_lower = my_string.lower() # более соращенная версия для перевода в нижний регистр
print(my_string_lower)
#

my_string_len= len(my_string_lower)
print(f'длина строки my_string_lower = {my_string_len}') # len - длинна строки 