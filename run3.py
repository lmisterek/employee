from employee import Employee, Developer, Manager

# Instantiate a new developer with Python as the coding language
dev_1 = Developer('Corey', 'Schafer', 50000, 'Corey.Schafer@company.com', 'Python')

# Instantiate a new manager as a manager of dev_1
mgr_1 = Manager('Sue', 'Smith', 90000, '', [dev_1])


# print the employees array assigned to mgr_1
print(mgr_1.employees)

# print the email attribute of mgr_1, this is empty
print(mgr_1.email)

# print the entire list of employees assigned to manager 1
mgr_1.print_emps()

# Print a True/False statement to test if Manager is a subclass of the Employee class
print(issubclass(Manager, Employee))