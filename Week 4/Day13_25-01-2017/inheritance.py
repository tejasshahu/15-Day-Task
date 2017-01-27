class Parent:
	parentAttr = 100
	def __init__(self):
		print "Parent constructor"
	def parentMethod(self):
		print "Parent Method"
	def setAttr(self, attr):
		Parent.parentAttr = attr
	def getAttr(self):
		print "parent attribute:", Parent.parentAttr
	def myMethod(self):
		print "Parent myMethod"

class Child(Parent):
	def __init__(self):
		print "Child constructor"
	def childMethod(self):
		print "child Method"
	def myMethod(self):
		print "Child myMethod"

c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()

p = Parent()
p.parentMethod()
c.myMethod() #child calls overridden method