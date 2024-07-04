#  lambda аргументы: выражение

# Обычная функция
def add(x, y):
    return x + y

# Эквивалентная лямбда-функция
add_lambda = lambda x, y: x + y

print(add(2, 3))        # Вывод: 5
print(add_lambda(2, 3)) # Вывод: 5

# Лямбда-функция в составе других функций
# Пример с использованием map
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
print(list(squared))  # Вывод: [1, 4, 9, 16, 25]

# Пример с использованием filter
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Вывод: [2, 4]

# Пример с использованием reduce
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Вывод: 120

# Сортировка с использованием лямбда-функции
# Список кортежей
points = [(1, 2), (3, 1), (5, -1), (2, 3)]

# Сортировка по второму элементу каждого кортежа
sorted_points = sorted(points, key=lambda point: point[1])
print(sorted_points)  # Вывод: [(5, -1), (3, 1), (1, 2), (2, 3)]



