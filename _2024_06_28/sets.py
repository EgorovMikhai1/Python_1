# Создание множества
my_set = {1, 2, 3, 4, 5}

# Добавление элемента
my_set.add(5)
print(my_set)

# Удаление элемента
my_set.remove(3)

# Удаление элемента с проверкой существования
my_set.discard(10)  # Не вызовет ошибку, если элемента нет

# Удаление и возвращение случайного элемента
random_element = my_set.pop()
print(random_element)

# Удаление всех элементов
my_set.clear()

# Проверка на принадлежность
print(2 in my_set)  # Output: False

# Объединение множеств
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # Или set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}

# Пересечение множеств
intersection_set = set1 & set2  # Или set1.intersection(set2)
print(intersection_set)  # Output: {3}

# Разность множеств
difference_set = set1 - set2  # Или set1.difference(set2)
print(difference_set)  # Output: {1, 2}

# Симметрическая разность множеств
symmetric_difference_set = set1 ^ set2  # Или set1.symmetric_difference(set2)
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}

# Итерация по элементам
for item in my_set:
    print(item)
