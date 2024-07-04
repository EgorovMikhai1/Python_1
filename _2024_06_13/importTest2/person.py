class Person:
    def __init__(self, name):
        self.name = name

    def drive_car(self, car):
        print(f"{self.name} is going to drive the {car.model}.")
        car.start()
        car.drive()
