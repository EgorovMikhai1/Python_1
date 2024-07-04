
# Создание словаря
my_dict = {'one': 1, 
           'two': 2, 
           'three': 3, 'four': 4, 'five': 5, 'six': 6}

# Добавление или изменение элемента
my_dict['four'] = 4

# Доступ по ключу
print(my_dict['one'])  # Output: 1

# Удаление элемента по ключу
del my_dict['two']

# Получение значения с проверкой существования ключа
value = my_dict.get('three', 'default_value')
print(value)  # Output: 3

# Получение всех ключей
keys = my_dict.keys()
print(keys)  # Output: dict_keys(['one', 'three', 'four'])

# Получение всех значений
values = my_dict.values()
print(values)  # Output: dict_values([1, 3, 4])

# Получение всех пар ключ-значение
items = my_dict.items()
print(items)  # Output: dict_items([('one', 1), ('three', 3), ('four', 4)])

# Удаление и возвращение элемента по ключу
removed_value = my_dict.pop('one')
print(removed_value)  # Output: 1

# Удаление и возвращение последней пары ключ-значение
last_item = my_dict.popitem()
print(last_item)  # Output: ('four', 4)

# Очистка словаря
my_dict.clear()

# Итерация по ключам и значениям
for key, value in my_dict.items():
    print(f"{key}: {value}")
