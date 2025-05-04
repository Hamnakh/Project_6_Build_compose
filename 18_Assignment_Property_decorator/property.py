class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    # Getter method
    @property
    def price(self):
        print("Getting price...")
        return self._price

    # Setter method
    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative!")
        else:
            print("Setting price...")
            self._price = value

    # Deleter method
    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price


# Usage
product = Product(100)

# Accessing the price
print(product.price)  # Calls @property

# Updating the price
product.price = 150    # Calls @setter

# Trying to set a negative price
product.price = -20    # Rejected

# Deleting the price
del product.price      # Calls @deleter
