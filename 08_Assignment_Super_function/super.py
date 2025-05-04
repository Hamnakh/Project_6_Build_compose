# Base class
class Person:
    def __init__(self, name):
        self.name = name  # Public attribute for person's name

# Derived class
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)   # Call the base class constructor
        self.subject = subject   # Add new attribute for teacher's subject

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Subject: {self.subject}")


# Creating an object of Teacher
teacher1 = Teacher("Hamna", "Mathematics")

# Display teacher's information
teacher1.display_info()
