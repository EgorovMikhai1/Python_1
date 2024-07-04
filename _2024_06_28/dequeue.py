from collections import deque

# Создание дека
my_deque = deque([1, 2, 3, 4, 5])

# Добавление элементов
my_deque.append(6)  # Добавление в конец
my_deque.appendleft(0)  # Добавление в начало

# Удаление элементов
my_deque.pop()  # Удаление с конца
my_deque.popleft()  # Удаление с начала

# Доступ к элементам по индексу
print(my_deque[0])  # Output: 1

# Очистка дека
my_deque.clear()

# Итерация по элементам
for item in my_deque:
    print(item)
