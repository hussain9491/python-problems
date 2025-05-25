# create an electrical car class that inherits from the Car class and has an additional attribute for battery capacity.
# Inheritance
class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def display(self):
        return f"Model: {self.model}, Year: {self.year}"
 
dis = Car("Tesla", 2020)
print(dis.display())

# now i add color and price to the car class in herit from the parents class
class Final(Car):
    def __init__(self, model, year, color, price):
        super().__init__(model, year)  # Call the parent constructor
        self.color = color
        self.price = price

    def displaycar(self):
      return f"Model: {self.model}, Year: {self.year}, Color: {self.color}, Price: {self.price}"         
dis1 = Final("Toyota", 2020,"red","$50,000")

print(dis1.displaycar())