# create a class named `Car` with attributes `make`, `model`, and `year`.
#  Create an instance of the class and print the values of the attributes. Also,
#  print the `__dict__` attribute of the instance to see all attributes and their values.
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.Model = model
        self.year = year

display = Car("Toyota", "Camry", 2023)
print(display.Model)
print(display.make)
print(display.year)
print(display.__dict__)  # {'make': 'Toyota', 'Model': 'Camry', 'year': 2023}

