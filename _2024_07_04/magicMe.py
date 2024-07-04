#Эти методы позволяют определять поведение объектов при взаимодействии с основными операциями и встроенными функциями

#Этот метод называется конструктором и вызывается при создании нового экземпляра класса.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

person = Person("Alice", 30)
print(person)


#Этот метод должен возвращать строковое представление объекта, предназначенное для пользователя.
class Person:
    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

print(person)  # Вывод: Person(name=Alice, age=30)


#Этот метод должен возвращать строку, которая является официальным строковым
# представлением объекта и должна быть информативной для разработчика.
class Person:
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

repr(person)  # Вывод: Person('Alice', 30)


#Метод __len__ определяет поведение функции len(), возвращая длину или размер объекта.
class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

my_list = MyList([1, 2, 3])
len(my_list)  # Вывод: 3


#Метод __getitem__ позволяет объекту поддерживать доступ по индексу, как для списков или словарей.
#Getter
# class MyList:
#     def __getitem__(self, index):
#         return self.items[index]
#
# my_list = MyList([1, 2, 3])
# print(my_list[0])  # Вывод: 1


#Метод __setitem__ позволяет объекту поддерживать установку значения по индексу.
#Setter
# class MyList:
#     def __setitem__(self, index, value):
#         self.items[index] = value
#
# my_list[0] = 10
# print(my_list[0])  # Вывод: 10


#Метод __delitem__ позволяет объекту поддерживать удаление элемента по индексу.
# class MyList:
#     def __delitem__(self, index):
#         del self.items[index]
#
# del my_list[0]
# print(my_list.items)  # Вывод: [2, 3]


#Методы __iter__ и __next__ позволяют объекту поддерживать итерацию, что необходимо для работы в цикле for.
class MyList:
    def __iter__(self):
        self.index = 0
        return self


    def __next__(self):
        if self.index < len(self.items):
            result = self.items[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

# my_list = MyList([1, 2, 3])
# for item in my_list:
#     print(item)



#В Python метод __call__ позволяет объекту быть вызываемым как функция.
# В Java нет прямого аналога, но можно использовать функциональные интерфейсы, такие как Runnable или Callable.
class Adder:
    def __call__(self, a, b):
        return a + b

add = Adder()
print(add(2, 3))  # Вывод: 5


#В Python методы __enter__ и __exit__ используются
# для управления ресурсами с помощью контекстных менеджеров.
# В Java для этого используется интерфейс AutoCloseable.
#Эти методы используются для поддержки менеджеров контекста, таких как with.
class MyContext:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")

with MyContext():
    print("Inside context")


#Другие магические методы
#__add__, __sub__, __mul__ и т.д. — для перегрузки арифметических операторов.
#__eq__, __lt__, __le__ и т.д. — для перегрузки операторов сравнения.
#__contains__ — для поддержки оператора in.
#__del__ — деструктор, вызывается при удалении объекта.