list - []


word = 'Programming'

	P   r  o  g  r  a  m  m  i  n  g
	0   1  2  3  4  5  6  7  8  9  10
  -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

>>> word = 'Programming'
>>> word[3:5]
'gr'
>>>
>>> word[0]
'P'
>>> word[7]
'm'
>>> word[-2]
'n'
>>> word[-1]
'g'
>>> word[3:5]
'gr'
>>> word[0:10]
'Programmin'
>>> word[:9]
'Programmi'
>>> word[3:]
'gramming'
>>> word[5:-3]
'amm'
>>> word[-3:5]
''
>>> word[:2] + word[3:]
'Prgramming'



  len(word)
  #len = length

>>> len(word)
11
>>> square = 'Square'
>>> len(square)
6
>>> len(word) + len(square)
17
>>> cube = [10,20,30,45,50]
>>> cube
[10, 20, 30, 45, 50]
>>> cube[0]
10
>>> cube[4]
50
>>> cube[3] = 40 #replace
>>> cube
[10, 20, 30, 40, 50]
>>>cube[0]
10
>>> cube[4]
50
>>> cube[3] = 40
>>> cube
[10, 20, 30, 40, 50]
>>> cube[5] = 60
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list assignment index out of range
>>> cube.append(60)
>>> cube
[10, 20, 30, 40, 50, 60]
>>> cube.append(40+5+20+10)
>>> cube
[10, 20, 30, 40, 50, 60, 75]
>>> cube.reverse
<built-in method reverse of list object at 0x000001E364B15448>
>>> cube.reverse()
>>> cube
[75, 60, 50, 40, 30, 20, 10]
>>> cube.sort()
>>> cube
[10, 20, 30, 40, 50, 60, 75]
>>> cube.remove(75)
>>> cube
[10, 20, 30, 40, 50, 60]
>>> cube.pop()
60
>>> cube.pop()
50

cube1 = [10,20,30,45,50]
cube2 = [1,2,3,4,5]
cube1.extend(cube2)

del cube1[3]
del cube1[1:3]
del cube1[:]

programA = ['A','B','C','D','E']
programB = ['a','b','c','d','e']
programC = programA + programB
programC 
['A','B','C','D','E','a','b','c','d','e']
programD = [1,2,3,4,5]
programC = programC + programD
programC[9:] = []
programC[5:9] = programD
programC

len(programC)
a = [10, 20, 30, 40, 50]
b = [60, 70, 80, 90, 100]
c = [110, 120, 130, ,140, 150]
x = [a, b, c]
x