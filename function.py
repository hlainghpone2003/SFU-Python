def say_hello():
	print('Hello World')

say_hello()

#function_parameter

def print_max(a,b):
	if a > b:
		print(a, 'is maxmium')
	elif a == b:
		print(a, 'is equal to', b)
	else:
		print(b,'is maxmium')

def func(x):
	print('x is ', x)
	x = 2
	print('change location x to ', x)

x = 50
func(x)
print('x is still', x)

x = 30
def func(x):
	x = 2

def func(x):
	x = 10

#Global Statement

def func():
	global x 
	print('x is ', x)
	x = 2
	print('change global x to', x)


x = 50
func()
print('Value of x is', x)

def say(message, time=1):
	print(message * times)

say ('Hello')
say ('Hello', 5)
say ('Good Bye')

#keyword Aurgemnt

def func(a, b=5, c=10):
	print('a is ', a, 'and b is', b, 'and c is ', c)

	func(3,8)
	func(24,c=26)
	func(c=29, a=39)

def func (a,b=5, c=6):
...     print('a is {0}. and b is {1}. c is {2}'. format(a,b,c))
...
>>> func(3,8)
a is 3. and b is 8. c is 6
	if x < 101 and x > 89 or x == 100:
		print("A")
	elif x < 89 and x > 79:
		print("B")



def total(a=5,*numbers, **phonebook):
	print('a',a)

	for single_item in numbers:
		print('single_item',single_item)

	for first_part, second part in phonebook.item():
		print(first_part,second_part)

total(10,326, 40, 58, 0, 99, 1, 2, 3, Jack=1123,john=2231,Inge=1459)


#returnstatement

def maximum (x,y):			
	if x > y:
		return x 
	elif x == y:
		return 'The numbers are equal'
	else:
		return y


print(maximum(3,8))

print(maximum(20,10))

 def max(x):
...     x = 50
...     return x
...
>>> x = 20
>>> max(x)
50
>>> print(max(x))
50


def print_max(x, y):
	'''Prints the maximum of two numbers
		the two values must be integers.
	'''

	x = int(x)
	y = int(y)

	if x > y:
		print(x, 'is maximum')

	elif x < y:
		print(y, 'is maximum')
	else:
		print(x, '&', y, 'is equal')

	print_max(5,9)

	print(print_max.__doc__)


def paper():
	'''1.A reference helps you to find the 
	original source should you need to check
	something again. '''

	'''2. Click Publishing Tools
	 at the top of your business or brand page '''

print(paper.__doc__)