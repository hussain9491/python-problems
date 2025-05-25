class Car:
    def __init__(self):
        self.speed = 0
        self.acc = False
        self._clutch = False
    def start(self):
        self.clutch = False
        self.acc = True
        self.speed = 5
        return f"Car started... with speed: {self.speed} km/h"
class Car2(Car):
    def __init__(self):
        super().__init__()
        self.gear = 5
    def stop(self):
        self.gear = 1
        self.acc = False
        self._clutch = True
        self.speed = 0
        return f"Car stopped.with gear: {self.gear - 2}, and speed:", self.speed
# # Inheritance is a way to form new classes using classes that have already been defined.
# # The newly formed classes are called derived classes, the classes that we derive from are called base classes.
# # Important benefits of inheritance are code reuse and reduction of complexity of a program.
# # Inheritance allows us to define a class that inherits all the methods and properties from another class.

# car1 = Car()
car2 = Car2()
# print(car2._clutch) # protected variable can be accessed outside the class
# # import point private variable does not inherit to child class but protected variables do.
print(car2.stop())    
# # multi level Inheritance in Python
class Car3(Car2):
    def __init__(self, color):
        super().__init__()# but abhi zaroorat nhi hai kyunki humne gear ko initialize nhi karna
        # super() is used to call the constructor of the parent class (Car2)
        self.color = color
car3 = Car3("red")
print(car3.color) # red  
print(car3.stop()) # Car stopped. {'gear': 1}, {'speed': 0}      

