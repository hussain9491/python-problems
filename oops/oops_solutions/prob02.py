# add method to the Employed class that display the name of the employee and their role and salary amount.
class Employed:
    def __init__(self, name, role, salary):
        self.Name = name
        self.role = role
        self.salaryamount = salary

    def display(self):
        return f"Name: {self.Name} Salary Amount: ${self.salaryamount} Role: {self.role}"

class Unemployed(Employed):
    def __init__(self, name, role, characteristics):
        super().__init__(name, role, 0)  # Setting salary to 0 for unemployed
        self.characteristics = characteristics
    
    def display(self):
        return f"Name: {self.Name} Role: {self.role} Characteristics: {self.characteristics}"

# Create instances
failure = Unemployed("John", "Jobless", "Lack of experience")
# emp1 = Employed("John Doe", "Software Engineer", 70000)
# emp2 = Employed("Jane Smith", "Data Scientist", 80000)

# Print information
print(failure.display())
# print(emp1.display())
# print(emp2.__dict__)
# print(emp1.Name)
# print(emp2.salaryamount)

