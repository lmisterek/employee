from employee import Employee


# Instantiate two employees
emp_1 = Employee('Corey', 'Schafer', 50000, 'Corey.Schafer@company.com')
emp_2 = Employee('Test', 'User', 60000, 'Test.User@company.com')


# Compare the following two print statements
print(repr(emp_1))
print(str(emp_1))

# Print the email attribute for two employees:  emp_1 and emp_2
print(emp_1.email)
print(emp_2.email)

# Set the raise amount
# this changes the raise amount for the class
Employee.set_raise_amt(1.05)

# Using a method to print the full name of an employee
print(emp_1.fullname())

# Printing the dict for the instance emp_1 
# This includes all the class attributes of the instance
print(emp_1.__dict__)

# Printing the dict for the class.  This includes all the class variables, attributes,
# and methods
print(Employee.__dict__)

# We can change the raise amount for the entire class or for just one employee
Employee.raise_amount = 1.05
emp_2.raise_amount = 1.06

# Three employees with first name, last name, and salary
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

# Instantiate a new Employee from the data given as first-last-salary (string, string, 
# integer)
new_emp_1 = Employee.from_string(emp_str_1)

# Print the new employee's first name
print("the new employees's first name is {}".format(new_emp_1.first))