# Создание кортежа
my_tuple = (1, 2, 3, 4, 5)

# Доступ по индексу
print(my_tuple[0])  # Output: 1

# Кортежи неизменяемы, поэтому элементы нельзя добавлять или удалять

# Доступ к части кортежа (срез)
sub_tuple = my_tuple[1:3]
print(sub_tuple)  # Output: (2, 3)

# Подсчет количества вхождений элемента
count = my_tuple.count(2)
print(count)  # Output: 1

# Поиск элемента по значению
index = my_tuple.index(3)
print(index)  # Output: 2

# Итерация по элементам
for item in my_tuple:
    print(item)
