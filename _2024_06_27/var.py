# Переменные и типы данных
name = "Alice"  # строка
age = 25  # целое число
height = 1.75  # число с плавающей точкой
is_student = True  # булево значение

# Условные конструкции
if age >= 18:
    print("Adult")
else:
    print("Minor")

# Цикл for
for i in range(5):
    print(i)  # выводит числа от 0 до 4

# Цикл while
count = 0
while count < 5:
    print(count)
    count += 1

# Определение функции
def greet(name):
    return f"Hello, {name}!"

# Вызов функции
print(greet("Alice"))


# Лямбда-функция для сложения двух чисел
add = lambda x, y: x + y
print(add(3, 5))
