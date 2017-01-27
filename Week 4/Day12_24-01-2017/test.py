import sys

print "Hello World!!!" * 2

counter = 100
mile = 1000.0
name = "Tejas"

print(counter)
print(mile)
print(name)

a = b = c = 1
d, e, f = 1, 2, 'Tejas'

print(a)
print(b)
print(e)
print(f)

tuple = ('xyz','20.0',20,20.0)
print(tuple)

list = ['xyz','20.0',20,20.0]
list[2] = "hi"
print(list)

dict = {}
dict['one'] = "this is one"
dict['2'] = "two"

tinydict = {'name': 'tejas','language': 'python','position': 'trainee'}
print (dict['one'])
print (tinydict.values())
print (tinydict.keys())

x = set("python tutorial")
print(x)
print(oct(a))

str = "hello python"

print "STRING:",str.capitalize()

list = ['abc', 8, 12.0]
it = iter(list) #build iterator object
#print(next(it)) #it prints next available element in iterator

while True:
	try:
		print (next(it))
	except StopIteration:
		sys.exit()