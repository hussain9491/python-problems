a=(4,2,(4,5))
b=(6,2,(5,4))
print( a<b)
# Type casting
print("Hello,\b World!") #\b backspace
print("Hello,\tWorld!")  #\t tab
print("Hello, \"World!\"")
print("Hello,\\ World!")

print("hussian " +  "\b ali" + "\teshal " + "\b Fatima")


print(len("Hello,\bWorld!"))#calculating length of a string even the space will be treated as character

h= "="
print(h.join(["ali", "alisa"]))
# hexa
print("\u0001")  # prints 'A'

# comparison
m = "xango" < "nana"   # False jo alphabet phle aata h wo baad me aane wale alpha se chota hota h
n = "Apple" < "apple"    # True, because uppercase come first
print(m, n )
# implicit type casting handle by python handle by types
# num_int = 7j
# num_complex = num_int + 3  # int + complex → complex
# print(num_complex, type(num_complex))
num_int = 10.7
num_float = num_int + 5j # int + float = float. skipped type hint to see what data type is assigned at runtime
print(num_float, type(num_float))

# explicit casting we have handle manually
num_str = "17"
print(int(num_str) + num_int) # ✅  casting str to int, arthmitic operation perfomed
print(num_str + str(num_int)) # ✅  casting int to str, string concatenation performed

# pythpn allow tuple convert to list 
tup: tuple = (1, 2.7, 3, 'OB')
lst = list(tup) # skipped type hint to see what data type is assigned at runtime
print(lst, type(lst))

