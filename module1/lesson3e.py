#дублирование строк осуществялется через *
my_string  = 'a'

new_string = my_string * 2
print(new_string)

new_string1 = f'{my_string}gggg ' * 4 #каждый элемент строки будет учитывать знак ! и его включать в дублирование
print(new_string1)
