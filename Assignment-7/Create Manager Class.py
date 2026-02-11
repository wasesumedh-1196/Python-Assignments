
# Create a python programe to show how the manager class inherits, 
# attributes & methods from both person & employee & how we can add 
# additional behaviours & properties in the manager class

# Parent class 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Parent class 2
class Employee:
    def __init__(self, emp_id, salary):
        self.emp_id = emp_id
        self.salary = salary

    def display_employee(self):
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)


# Child class (Multiple Inheritance)
class Manager(Person, Employee):
    def __init__(self, name, age, emp_id, salary, department, bonus):
        # Initializing parent class constructors
        Person.__init__(self, name, age)
        Employee.__init__(self, emp_id, salary)

        # Manager's own attributes
        self.department = department
        self.bonus = bonus

    # Manager's own method
    def display_manager(self):
        print("Department:", self.department)
        print("Bonus:", self.bonus)

    # Additional behavior
    def total_salary(self):
        return self.salary + self.bonus


# Creating object of Manager class
m1 = Manager("Mahesh Saste", 19, "ADT25SOCB0602", 50000, "Sales", 10000)

print("---- Person Details ----")
m1.display_person()

print("\n---- Employee Details ----")
m1.display_employee()

print("\n---- Manager Details ----")
m1.display_manager()

print("\nTotal Salary:", m1.total_salary())
