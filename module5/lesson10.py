#Словари
my_dict = {
    'name': 'Боб',  # Элемент словаря, где 'name' является ключом, а 'Боб' значением
    'age': 33,  # Элемент словаря, где 'age' является ключом, а '33' значением
}
# Ключ должен быть уникальным в пределах одного словаря. 
# В одном словаре не может быть 2х одинаковых ключей.

person = {
    'first_name': 'Pol',
    'last_name': 'Maccartni',
    'age': '50'
}
# У словарей нет индексов, только ключи
name = person['first_name']
last_name = person['last_name']
age = person['age']

print('имя', name)
print('фамилия', last_name)
print('возраст', age)

# Еще один пример работы со словарем
user = {'name': 'Алиса', 'login': 'alice01'}

# Напиши свой код после этой строки
name = user['name']
print(name)


# добавление и изменение ключей в словаре:

person = {}
# Добавляем в словарь новую пару ключ-значение
# Новый ключ = 'first_name'
# Значение нового ключа = 'Пол'

person['first_name'] = 'Pol'

# Добавляем в словарь новую пару ключ-значение
# Новый ключ = 'age'
# Значение нового ключа = 33

person['age'] = 33

print(person)

person = {'first_name': 'pol', 'age': 33, }
# Добавляем в словарь новый ключ - cities: список значений 

person['cities'] = ['Moscow', 'London', 'Paris']

print(person)


peson = {
    'first_name': 'Pol',
    'age': 33,
    'cities': ['Moscow', 'London', 'Paris']
}
city1 = peson['cities'][0]
city2 = peson['cities'][1]

for city in peson['cities']:
    print(city)


# Best practice
# Метод GET для получения значений к ключу

person = {'name': 'Bob'}

person_name = person['name']
# Если мы попытаемся получить значение несуществующего ключа,
#  то программа вылетит с ошибкой:
# Ошибка KeyError - это ошибка ключа. Python говорит, что в словаре нет запрашиваемого ключа.
# Мы можем попытаться получить значение ключа, для этого используется метод get(). 
# Первый параметр метода get() - это ключ, значение которого нужно получить:


person = {'name': 'Bob'}

person_name = person.get('name')
print(person_name)



# Если метод get() не найдет в словаре искомый ключ, 
# то возвращается значение None, при этом программа не вылетает с ошибкой. 
# Метод get() принимает 2 параметра: первый - имя ключа, второй - значение по умолчанию (дефолтное значение) 
# - это значение, которое вернет метод get(), если переданный ключ не будет найден в словаре:
person = {}

person_name = person.get('name', 'Ключа name в словаре нет')

print(person_name)

#Если при решении задачи ты обрабатываешь словарь, 
# в котором может не быть искомых ключей, всегда используй метод get().

