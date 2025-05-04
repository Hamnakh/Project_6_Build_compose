🐍 Python OOP Concepts – Assignments
This repository contains a collection of Python programs that demonstrate essential Object-Oriented Programming (OOP) concepts. Each assignment showcases a specific concept using practical and well-structured class designs.

📚 Overview of Assignments
Each assignment focuses on one of the core principles or features of OOP in Python, such as constructors, class methods, inheritance, decorators, and more.

🗂️ Assignment List
1. 🔁 Using self
Goal:
Create a class Student with attributes name and marks. Use the self keyword in the constructor to initialize these attributes. Add a display() method to print student details.

2. 🧮 Using cls
Goal:
Create a class Counter that tracks how many instances are created using a class variable. Use a class method and the cls keyword to display and manage the count.

3. 🚗 Public Variables and Methods
Goal:
Create a Car class with a public variable brand and a public method start(). Demonstrate access to both from outside the class.

4. 🏦 Class Variables and Class Methods
Goal:
Create a Bank class with a class variable bank_name. Add a class method change_bank_name(cls, name) to modify the variable and reflect changes across all instances.

5. ➕ Static Variables and Static Methods
Goal:
Create a utility class MathUtils with a static method add(a, b) that returns the sum of two numbers. No instance or class variables should be used.

6. 📝 Constructors and Destructors
Goal:
Create a Logger class that prints a message when an object is created (constructor) and when it is destroyed (destructor).

7. 🔐 Access Modifiers: Public, Protected, Private
Goal:
Create an Employee class with:

a public variable name

a protected variable _salary

a private variable __ssn
Try accessing all three and observe the results.

8. 🧬 Using super() Function
Goal:
Create a base class Person with a constructor for name. Create a subclass Teacher that adds a subject field and uses super() to call the parent constructor.

9. 🧱 Abstract Classes and Methods
Goal:
Use the abc module to create an abstract class Shape with an abstract method area(). Implement a subclass Rectangle that defines the area() method.

10. 🐶 Instance Methods
Goal:
Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog’s name.

11. 📘 Class Methods
Goal:
Create a Book class with a class variable total_books. Use a class method increment_book_count() to update the count each time a book is added.

12. 🌡️ Static Methods
Goal:
Create a TemperatureConverter class with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit equivalent.

13. ⚙️ Composition
Goal:
Create two classes: Engine and Car. Use composition to include an Engine object within the Car class. Access methods of Engine from Car.

14. 🧩 Aggregation
Goal:
Create Department and Employee classes. Use aggregation by letting a Department object store a reference to an independent Employee object.

15. 🧬 Method Resolution Order (MRO) & Diamond Inheritance
Goal:
Create classes A, B, C, and D where:

B and C inherit from A

D inherits from both B and C
Override a method and observe how MRO works when calling it from D.

16. 📝 Function Decorators
Goal:
Write a decorator log_function_call that prints "Function is being called" before executing a function. Apply it to a function say_hello().

17. 🎁 Class Decorators
Goal:
Create a class decorator add_greeting that adds a greet() method returning "Hello from Decorator!". Apply it to the Person class.

18. 🛒 Property Decorators
Goal:
Create a class Product with a private attribute _price. Use @property, @setter, and @deleter to manage access to this attribute.

19. 🔄 callable() and __call__()
Goal:
Create a Multiplier class with an __init__() to set a factor. Implement __call__() to multiply input by the factor. Verify with callable().

20. ⚠️ Creating a Custom Exception
Goal:
Define a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18, and handle it using try...except.

21. ⏳ Making a Class Iterable
Goal:
Create a Countdown class that accepts a start number. Implement __iter__() and __next__() to make it iterable in a loop, counting down to 0.

