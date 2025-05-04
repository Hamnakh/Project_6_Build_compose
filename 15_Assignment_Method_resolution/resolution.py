# Base class
class A:
    def show(self):
        print("Show from class A")

# Derived class B overrides show()
class B(A):
    def show(self):
        print("Show from class B")

# Derived class C overrides show()
class C(A):
    def show(self):
        print("Show from class C")

# Class D inherits from B and C (Diamond Inheritance)
class D(B, C):
    pass  # No override; will use MRO to resolve which 'show()' to call

# Create an object of D
obj = D()

# Call the show method
obj.show()

# Display the Method Resolution Order
print("\nMRO of class D:", [cls.__name__ for cls in D.__mro__])
