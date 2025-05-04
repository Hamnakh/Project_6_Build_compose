class Car:
    # Public variable
    brand = "Toyota"
    
    # Public method
    def start(self):
        print(f"The {self.brand} car has started!")
    
    def __init__(self, brand=None):
        if brand:
            self.brand = brand

# Example usage
if __name__ == "__main__":
    # Create a car object with default brand
    car1 = Car()
    print(f"Car1 brand: {car1.brand}")  # Accessing public variable
    car1.start()  # Calling public method
    
    # Create a car object with custom brand
    car2 = Car("Honda")
    print(f"Car2 brand: {car2.brand}")  # Accessing public variable
    car2.start()  # Calling public method
    
    # Modifying public variable from outside the class
    car1.brand = "Ford"
    print(f"Car1 new brand: {car1.brand}")
    car1.start() 