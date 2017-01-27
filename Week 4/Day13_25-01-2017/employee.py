import sys

class Employee:
	'Base class for all employee'
	empCount = 0
	
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1

	def displayCount(self):
		print "Total Employee %d" % Employee.empCount

	def displayEmployee(self):
		print "Name:", self.name, ",Salary:", self.salary

emp1 = Employee("Tejas", 1000)
emp1.displayEmployee()
emp2 = Employee("Hardik", 50000)
emp2.displayEmployee()

emp1.name = "Naitik"
emp1.displayEmployee()

emp3 = Employee("Manthan", 25000)
emp3.displayEmployee()
print "Total Employee: %d" % Employee.empCount

print "Employee.__doc__ :", Employee.__doc__
print "Employee.__name__ :", Employee.__name__
print "Employee.__module__ :", Employee.__module__

# print "Employee.__bases__ :", Employee.__bases__
# print "Employee.__dict__ :", Employee.__dict__

# delete salary attribute of employee3
# del emp3.salary
# emp3.displayEmployee()