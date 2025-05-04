class Employee:
    def __init__(self, name, salary, ssn):
        # Public variable
        self.name = name
        
        # Protected variable (convention: one underscore)
        self._salary = salary
        
        # Private variable (name mangling: double underscore)
        self.__ssn = ssn

    def display_info(self):
        # Accessing all variables within the class
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN: {self.__ssn}")


# Creating an Employee object
emp = Employee("Hamna", 50000, "123-45-6789")

# Accessing public variable
print("Public Access ->", emp.name)

# Accessing protected variable (allowed but discouraged outside class)
print("Protected Access ->", emp._salary)

# Accessing private variable directly (will cause AttributeError)
try:
    print("Private Access ->", emp.__ssn)
except AttributeError as e:
    print("Private Access -> Error:", e)

# Accessing private variable using name mangling
print("Private Access with name mangling ->", emp._Employee__ssn)
