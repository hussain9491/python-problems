# polymorphism in functions
# write a function that multiply that multiplies two numbers, but can also accept and add string 

def multiply(a, b):
    # Try to convert inputs to numbers if possible
    try:
        num1 = float(a)
        num2 = float(b) 
        return num1 * num2
    # If conversion fails, treat as strings
    except ValueError:
        return str(a) * int(b) if isinstance(b, str) and b.isdigit() else a + b
    

user = input("Enter a number or a string: ")
user2 = input("Enter another number or a string: ")
result = multiply(user, user2)
print(result)

#  output: 20


