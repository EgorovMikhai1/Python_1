import array

# Создание массива целых чисел
arr = array.array('i', [1, 2, 3, 2, 4])

# append(x): добавляет элемент x в конец массива
arr.append(5)
print("append:", arr)  # Output: array('i', [1, 2, 3, 2, 4, 5])

# buffer_info(): возвращает кортеж (адрес буфера, количество элементов)
info = arr.buffer_info()
print("buffer_info:", info)  # Output: (address, 6)

# byteswap(): меняет порядок байтов в каждом элементе массива
arr.byteswap()
print("byteswap:", arr)  # Output: измененные элементы массива (в зависимости от платформы)

# count(x): возвращает количество вхождений x в массиве
count = arr.count(2)
print("count:", count)  # Output: 2

# extend(iterable): добавляет элементы из iterable в конец массива
arr.extend([6, 7, 8])
print("extend:", arr)  # Output: array('i', [1, 2, 3, 2, 4, 5, 6, 7, 8])

# fromlist(list): добавляет элементы из списка
arr.fromlist([9, 10])
print("fromlist:", arr)  # Output: array('i', [1, 2, 3, 2, 4, 5, 6, 7, 8, 9, 10])

# index(x): возвращает индекс первого вхождения x
# index = arr.index(4)
# print("index:", index)  # Output: 4

# insert(i, x): вставляет элемент x в позицию i
arr.insert(0, 0)
print("insert:", arr)  # Output: array('i', [0, 1, 2, 3, 2, 4, 5, 6, 7, 8, 9, 10])

# pop([i]): удаляет и возвращает элемент по индексу i (или последний элемент, если i не указан)
element = arr.pop()
print("pop:", element)  # Output: 10
print("after pop:", arr)  # Output: array('i', [0, 1, 2, 3, 2, 4, 5, 6, 7, 8, 9])

# remove(x): удаляет первое вхождение элемента x
# arr.remove(2)
# print("remove:", arr)  # Output: array('i', [0, 1, 3, 2, 4, 5, 6, 7, 8, 9])

# reverse(): разворачивает массив
arr.reverse()
print("reverse:", arr)  # Output: array('i', [9, 8, 7, 6, 5, 4, 2, 3, 1, 0])

# tolist(): возвращает массив в виде списка
lst = arr.tolist()
print("tolist:", lst)  # Output: [9, 8, 7, 6, 5, 4, 2, 3, 1, 0]

# Метод получения среза массива
sliced_arr = arr[2:5]
print("slice:", sliced_arr)  # Output: array('i', [7, 6, 5])

# Итерация по элементам массива
print("iteration:")
for item in arr:
    print(item)
