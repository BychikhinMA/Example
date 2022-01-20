import json

# JSON

number = 1

# Преобразуем число в строку формата json

number_jason = json.dumps(number)

print(number_jason)
print(type(number_jason))

my_string = 'Moscow - Москва'   #символы кириллицы превратились в что-то непонятное - это кодировка UTF16, 
                                # специальная кодировка символов, которая использует для передачи данных по интернету.
# # Преобразуем строку на латинице в строку формата json
my_string_jason = json.dumps(my_string)
print(my_string_jason)

my_list = [1, 2, 'Москва', True, False]
# Преобразуем список значений в строку формата json
my_list_jason = json.dumps(my_list)
print(my_list_jason)
print(type(my_list_jason))


# Словари тоже можно преобразовывать в формат JSON:

my_dict = {
    'first_name': 'Иван',
    'last_name': 'Иванов',
    'age': 33,
}

my_dict_jason = json.dumps(my_dict)
print(my_dict_jason)

# Распаковка данных из формата JSON

# реобразовать строку формата JSON в обычный объект Python, 
# используется метод loads() из модуля json. 
# Метод loads() принимает 1 параметр - строку формата JSON, которую необходимо распаковать:

my_dict = {
    'first_name': 'Иван',
    'last_name': 'Иванов',
    'age': 33,
}

# Запаковываем словарь в JSON
my_dict_json = json.dumps(my_dict)
print(my_dict_json)
print(type(my_dict_json))

# Распаковываем данные из JSON

my_dict_from_jason = json.loads(my_dict_json)
print(my_dict_from_jason)
print(type(my_dict_from_jason))