# Funtion returning multiple values 
# create a function that return both the area and circumference of a cricle given its radius
import math
def circle_properties(radius):
    area = math.pi * radius **2
    circumference = 2 * math.pi * radius
    return area, circumference
a, c = circle_properties(5)
print(f"Area: {round(a ,2)}, Circumference: {round(c ,2)}")  # Output: Area: 
