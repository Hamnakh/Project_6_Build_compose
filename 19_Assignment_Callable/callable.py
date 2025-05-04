class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # Set the multiplication factor

    def __call__(self, value):
        result = self.factor * value
        print(f"Multiplying {value} by factor {self.factor} gives {result}")
        return result


# Create an instance of Multiplier with a factor of 3
triple = Multiplier(3)

# Check if the object is callable
print("Is 'triple' callable?", callable(triple))

# Use the object like a function
triple(10)  # Should print: Multiplying 10 by factor 3 gives 30
