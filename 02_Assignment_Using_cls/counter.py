class Counter:
    # Class variable to keep track of the count
    count = 0
    
    def __init__(self):
        # Increment the count when a new object is created
        Counter.count += 1
    
    @classmethod
    def get_count(cls):
        # Class method to get the current count
        return cls.count
    
    @classmethod
    def display_count(cls):
        # Class method to display the count
        print(f"Total number of Counter objects created: {cls.count}")

# Example usage
if __name__ == "__main__":
    # Create some Counter objects
    c1 = Counter()
    c2 = Counter()
    c3 = Counter()
    
    # Display the count using class method
    Counter.display_count()
    
    # Get the count using class method
    total_count = Counter.get_count()
    print(f"Total count (using get_count): {total_count}") 