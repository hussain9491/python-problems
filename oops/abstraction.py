# Abstraction in Python
# Abstraction is a concept in OOP that allows you to hide the complex implementation details and show only the essential features of the object.
class Car:
    def __init__(self):
        self.speed = 0
        self.acc = False
        self.clutch = False
    def start(self):
        self.clutch = True 
        self.acc = True
        self.speed = 5
        return f"Car started... with speed: {self.speed} km/h"
go = Car()
print(go.start()) 
#ab hame ye to nhi pata laga naa ye ki clutch ka kya hua kese ye false se true hua
#  hame ye to sirf ye pata laga ki car start ho gayi hai    
# bas isiii ko abstraction kehte hain
# abstraction ka matlab hai ki aapko sirf ye pata ho ki koi cheez  kaam karti hai lekin uski implementation ka nhi pata ho kese kr rhhi h
     









