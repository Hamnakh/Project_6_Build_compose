class Countdown:
    def __init__(self, start):
        self.current = start  # Initialize starting point

    def __iter__(self):
        return self  # Return the iterator object

    def __next__(self):
        if self.current < 0:
            raise StopIteration  # End of iteration
        else:
            value = self.current
            self.current -= 1
            return value

# Example usage
for number in Countdown(5):
    print(number)
