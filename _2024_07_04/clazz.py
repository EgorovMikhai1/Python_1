class Animal:
    
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print('Eating')    
        
dog = Animal('dog')   

class Dog(Animal):
    def __init__(self, name):
        self.name = name
       
       
       
dog2 = Dog('dog')
dog.eat()