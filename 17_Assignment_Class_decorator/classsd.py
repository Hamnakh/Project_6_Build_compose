# Class decorator function
def add_greeting(cls):
    # Define a new method inside the decorator
    def greet(self):
        return "Hello from Decorator!"
    
    # Attach the method to the class
    cls.greet = greet
    
    return cls  # Return the modified class

# Apply the decorator to the Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        return f"My name is {self.name}"

# Create an instance of Person
p = Person("Hamna")

# Call methods
print(p.show_name())       # Original method
print(p.greet())           # Added by decorator
