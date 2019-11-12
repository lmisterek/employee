class Employee:

	# class variable (this can be changed)
	raise_amount = 1.04

	# initialize the number of employees to zero.
	num_of_emps = 0

	# class attributes
	def __init__(self, first, last, pay, email=None):
		self.first = first
		self.last = last
		self.pay = pay
		if email is None:
			email = ''
		else:
			self.email = email

		# Increment the number of employees up by one inside the init method
		Employee.num_of_emps += 1

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amount = amount

	@classmethod
	#instantiate a new employee
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay, '')

	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True

	# include repr at minimum
	def __repr__(self):
		return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

	def __str__(self):
		return '{} - {}'.format(self.fullname(), self.email)

class Developer(Employee):
	raise_amt = 1.10

	def __init__(self, first, last, pay, email, prog_lang):
		super().__init__(first, last, pay, email)
		self.prog_lang = prog_lang

class Manager(Employee):

	def __init__(self, first, last, pay, email, employees=None):
		super().__init__(first, last, pay, email)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emps(self):
		for emp in self.employees:
			print('-->', emp.fullname())

		# Equivalent
		# Employee.__init__(self, first, last, pay)