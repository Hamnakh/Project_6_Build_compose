# Decorator function
def log_function_call(func):
    def wrapper():
        print("Function is being called")  # Log message
        func()  # Call the original function
    return wrapper

# Apply the decorator to the function
@log_function_call
def say_hello():
    print("Hello, World!")

# Call the decorated function
say_hello()
