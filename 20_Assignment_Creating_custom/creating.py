# Step 1: Define the custom exception
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be at least 18"):
        self.message = message
        super().__init__(self.message)

# Step 2: Function that checks age and may raise the exception
def check_age(age):
    if age < 18:
        raise InvalidAgeError()  # Raise custom exception
    else:
        print("Access granted.")

# Step 3: Using try...except to handle the custom exception
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print("InvalidAgeError caught:", e)
except ValueError:
    print("Please enter a valid number for age.")
