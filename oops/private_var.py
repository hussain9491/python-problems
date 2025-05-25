class abc:
    def __init__(self):
        self.__private_var = "I am private"

class Child(abc):
    def show(self):
        print(self._abc__private_var)  # ✅ Works via name mangling _ laga kr parentclass se private laane ka tariqa h

c = Child()
c.show()  # Output: I am private



class Car:
    def __init__(self):
        
        self._clutch = False
car2 = Car()
print(car2._clutch) # protected variable can be accessed outside the class
# # import point private variable does not inherit to child class but protected variables do.        



class Person:
    name = "Ali"
    def __init__(self):
        # Person.name = "hussain"
        self.__class__.name = "Hussain" # 2nd method to change class attribute value from instance method.
r1 = Person()
print(r1.name)        
