#Tuple

Tuple - ()

t = 12345, 54321, 'hello!'
t[0]

t
# Tuples may be nested
u = t, (1, 2, 3, 4, 5)
u

# Tuples are immutable:
t[0] = 88888

#but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v

fruit = ("apple", "banana","cherry","orange", "kiwi", "melon", "mango")
print(fruit[2:5])

#can not change the tuple but we can change list. 
#so we change to the list and change we want and again chage the tuple
>>> t = 12345, 54321, 'hello!'
>>> x = list(t)
>>> x[0]
12345
>>> x[0] = 1010
>>> x
[1010, 54321, 'hello!']
>>> t = tuple(x)
>>> t
(1010, 54321, 'hello!')