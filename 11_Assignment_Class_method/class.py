class Book:
    # Class variable shared by all instances
    total_books = 0

    def __init__(self, title):
        self.title = title  # Instance variable for book title
        # Increment the total book count using the class method
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        # Modify the class variable using cls
        cls.total_books += 1

    @classmethod
    def display_total_books(cls):
        print(f"Total books added: {cls.total_books}")


# Creating book instances
book1 = Book("Python Basics")
book2 = Book("Data Structures")
book3 = Book("Machine Learning")

# Display the total number of books
Book.display_total_books()
