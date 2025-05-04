class Dog:
    def __init__(self, name, breed):
        # Instance variables
        self.name = name
        self.breed = breed

    def bark(self):
        # Instance method that uses the dog's name
        print(f"{self.name} says: Woof! Woof!")


# Creating a Dog object
dog1 = Dog("Buddy", "Golden Retriever")

# Calling the instance method
dog1.bark()
