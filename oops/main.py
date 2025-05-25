# class Person:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#     def display(self):
#        return f"Name1: {self.name}, Age: {self.age}"
#     def add(self, marks):
#         self.marks = marks
#         print(f'your name is : {self.name}, this is your age: {self.age},  here are your marks: {self.marks}')
# show = Person("john", 22, )
# Person.display(show)
# show.display()
# show.add(344)   
# print(show.__dict__)       




# class Student(Person):
#     def __init__(self, name, age, rollno):
#         super().__init__(name, age)
#         self.rollno = rollno
#     def display(self):
#         super().display()
#         print(f"Roll No.: {self.rollno}")

# a = Student("John", 22, 101)
# # a.display()
# a.add(344)
# print(a.__dict__)        

# class Myfav():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display(self):
#         return f"Name34: {self.name}, Age: {self.age}"
#     def add(self, marks):
#         self.marks = marks
#         return f'this is your: {self.name}, this is your age: {self.age}, here is your marks: {self.marks}'
# show = Myfav('ali', 18)
# show.display()
# show.add(344)
# print( show.display())  
# print(show.add(78)) 

class StudentMarks:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display(self):
            sum = 0
            for i in self.marks:
             sum += i
            return f"Name: {self.name}, your avg Marks: {sum/3}"    
s1 = StudentMarks("Ali", [45, 67, 89])            
s2 = StudentMarks("abeer", [45, 67, 89])            
s3 = StudentMarks("anwar", [45, 67, 89])            
s1.display()
s1.name = "Hussain"
print(s1.display())
print(s2.display())
print(s3.name)