#Sets

includes a data type for sets.
Curly braces or the set() fuction can be used to create sets.
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) #show that duplicates have been removed
'orange' in basket # fast member testing
'crabgrass' in basket

Demonstrate set operation on unique letter form two words

a = set('abracadabra')
b = set('alacazam')
a                              #unique letter in a
a - b                          #letter in a but not in b
a | b                          #letter in a or b or both
a & b                          #letter in both a and b
a ^ b                          #letter in a or b but not both

>>> a - b
{'r', 'b', 'd'}
>>> a | b
{'l', 'd', 'm', 'a', 'c', 'r', 'b', 'z'}
>>> a & b
{'c', 'a'}
>>> a ^ b
{'l', 'd', 'm', 'b', 'r', 'z'}

x = set('23802348')
y = set('57839012')
>>> x - y
{'4'}
>>> y - x
{'5', '1', '7', '9'}
>>> x | y
{'1', '3', '9', '0', '8', '7', '4', '5', '2'}
>>> x & y
{'8', '2', '3', '0'}
>>> x ^ y
{'1', '9', '7', '4', '5'}


fruits = {"apple", "banana", "cherry", "orange", "kiwi", "lemon", "mango"}
print("cherry" in fruits)



a = {x for x in 'abracadabra' if x not in 'abc'}
a
--------- 

>>>Dictionaries

#Dictionaries
#Another useful data type built into Python is the dictionaries

tel = {'jack' : 4098, 'sape':4139}
tel['sape']
tel['guide'] = 4127 


list(tel) #change
sorted(student) #Alphabet sorting
'MgOo' in student

'MaMa' not in student

dict([('sape', 4139), ('guide',4127), ('jack',4098)])
dict(sape=4139, guide= 4127, jack= 4098)

{x: x**2 for x in (2,4,6)}
{2: 4, 4: 16, 6: 36}

>>> for x in 2, 4, 6:
...     print(x,x**2)
...
2 4
4 16
6 36
>>> for x in 2, 4, 6:
...     print(x,':',x**2)
...
2 : 4
4 : 16
6 : 36

{x: x**3 for x in (10, 20, 30, 40, 50) }
{10: 1000, 20: 8000, 30: 27000, 40: 64000, 50: 125000}

-----------
When looping through dictionaries

>>> knights = {'gallahad': 'the pure', 'robin':'brave', 'sape': 4355}
>>> for k, v in knights.items():
...     print(k,v)
...
gallahad the pure
robin brave
>>> for k, v in knights.items():
...     print(k,v)
...
gallahad the pure
robin brave
sape 4355
>>> for x, y in enumerate(['tic','tac', 'toe']):
...     print(x, y)
...
0 tic
1 tac
2 toe