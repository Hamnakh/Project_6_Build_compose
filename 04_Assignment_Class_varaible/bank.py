class Bank:
    # Class variable
    bank_name = "State Bank"
    
    def __init__(self, branch):
        self.branch = branch
    
    @classmethod
    def change_bank_name(cls, new_name):
        # Class method to change the bank name
        cls.bank_name = new_name
    
    def display_info(self):
        print(f"Bank Name: {self.bank_name}")
        print(f"Branch: {self.branch}")

# Example usage
if __name__ == "__main__":
    # Create two bank instances
    bank1 = Bank("Main Branch")
    bank2 = Bank("City Branch")
    
    # Display initial information
    print("Initial Information:")
    bank1.display_info()
    bank2.display_info()
    
    # Change bank name using class method
    print("\nAfter changing bank name:")
    Bank.change_bank_name("National Bank")
    
    # Display information after change
    bank1.display_info()
    bank2.display_info()
    
    # Create a new instance after name change
    print("\nNew instance after name change:")
    bank3 = Bank("Sub Branch")
    bank3.display_info() 