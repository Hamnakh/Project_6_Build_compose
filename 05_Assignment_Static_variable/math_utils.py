class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def divide(a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

# Example usage
if __name__ == "__main__":
    # Using static methods without creating an instance
    print("Addition:", MathUtils.add(5, 3))
    print("Subtraction:", MathUtils.subtract(10, 4))
    print("Multiplication:", MathUtils.multiply(6, 7))
    print("Division:", MathUtils.divide(15, 3))
    
    # Also works with an instance (though not necessary)
    math = MathUtils()
    print("\nUsing instance:")
    print("Addition:", math.add(8, 2))
    print("Division by zero:", math.divide(10, 0)) 