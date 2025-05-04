class Logger:
    def __init__(self):
        # Constructor: Called when object is created
        print("Logger object created.")

    def __del__(self):
        # Destructor: Called when object is destroyed
        print("Logger object destroyed.")


# Creating Logger object
log1 = Logger()

# Manually deleting the object to trigger destructor
del log1

# Note: If you don't use 'del', the destructor runs when the program ends.
