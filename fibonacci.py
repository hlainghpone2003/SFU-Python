#fibonacci number module

#n = int (input('please enter a number:'))

def fib(n): # write fibonacci series up to n
	a, b = 0, 1
	while a < n:
		print(a,end='')
		a, b = b, a + b
	print()

#Go to fibonacci powerpoint 
def fib2(n): #return fibonacci series up to n
	result = []
	a, b = 0, 1
	while a <n:
		result.append(a)
		a, b = b, a + b
	return result