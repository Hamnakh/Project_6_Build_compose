# Class representing an Employee
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display_info(self):
        print(f"Employee ID: {self.emp_id}, Name: {self.name}")


# Class representing a Department that aggregates an Employee
class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation: store reference to Employee

    def show_department_info(self):
        print(f"Department: {self.dept_name}")
        print("Employee in Department:")
        self.employee.display_info()


# Create an independent Employee object
emp1 = Employee("Hamna", 101)

# Employee exists independently and can be used without Department
emp1.display_info()

print("-----")

# Create a Department and pass the existing Employee object
dept = Department("HR", emp1)

# Display department info and aggregated employee info
dept.show_department_info()
