class Car:
    def __init__(self, model):
        self.model = model
        self.started = False

    def start(self):
        self.started = True
        print(f"{self.model} started.")

    def stop(self):
        self.started = False
        print(f"{self.model} stopped.")

    def drive(self):
        if self.started:
            print(f"{self.model} is driving.")
        else:
            print(f"{self.model} is not started yet.")
