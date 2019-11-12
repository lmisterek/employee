from employee import Employee, Developer


# Instantiate two employees
emp_1 = Employee('Corey', 'Schafer', 50000, 'Corey.Schafer@company.com')
emp_2 = Employee('Test', 'User', 60000, 'Test.User@company.com')

# Instantiate two new developers (Developer is a subclass of Employee)
dev_1 = Developer('Corey', 'Schafer', 50000, 'Corey.Schafer@company.com', 'Python')
dev_2 = Developer('Test', 'User', 60000, 'Test.User@company.com', 'Java')

# Print the programming language for dev_1
print(dev_1.prog_lang)

# Print a True/False statement to test if mgr_1 is an instance of the Developer class
print(isinstance(mgr_1, Developer))