class Decorator:
    def __init__(self, fx):
        self.fx = fx
    def __call__(self):
        print("Helloss")
        self.fx()
        print("Goodbye")
a = Decorator(lambda: print("Welcome to Python!"))
a()  # Output: Helloss Welcome to Python! Goodbye

def greet(fx):
    def rapper():
     print("Hello")
     fx()
     print("Goodbye")
    return rapper
@greet
def greet2():
    print("Welcome to Python!")
greet2()
@greet
def greet3():
    print("Hello jane!")
greet3()