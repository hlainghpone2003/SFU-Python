#loops

-while Loops
-for Loops

Condition is true, while loop execute a set of statements

x = 1
while x < 7:
	print(x)
	x += 1

>>> x = 1
>>> while x < 7:
...     print(x)
...     x += 1
...
1
2
3
4
5
6
while loop variable ready.

x=1
while x < 7:
	print(x)
	if x == 5:
		break
	x += 1
	>>> x = 1
>>> while x < 7:
...     print(x)
...     if x ==5:
...             break
...     x += 1
...
1
2
3
4
5
>>> while x < 100:
...     print(x)
...     if x == 5:
...             break
...     x +=5
...
50
55
60
65
70
75
80
85
90
95

for Loops

# for loop is iterating over a sequence
 
fruit = ["apple","banana","orange","pineapple","coconut","cucumber"]
for x in fruit:
	print(x)

>>> fruit = ["apple","banana","orange","pineapple","coconut","cucumber"]
>>> for x in fruit:
...     print(x)
...
apple
banana
orange
pineapple
coconut
cucumber
#looping in a string 
for x in "pineapple":
	print(x)

>>> fruit = ["apple","banana","orange","pineapple","coconut","cucumber"]
>>> for x in "pineapple":
...     print(x)
...
p
i
n
e
a
p
p
l
e
#the break statement 

#stop after condition 
fruit = ["apple","banana","orange","pineapple","coconut","cucumber"]
for x in fruit:
	print(x)
	if x == "pineapple":
		break

>>> for x in fruit:
...     print(x)
...     if x == "pineapple":
...             break
...
apple
banana
orange
pineapple
-----
#stop before condition
fruit = ["apple","banana","orange","pineapple","coconut","cucumber"]
for x in fruit:
	if x == "pineapple":
		break
	print(x)

>>> for x in fruit:
...     if x == "pineapple":
...             break
...     print(x)
...
apple
banana
orange
# the continue statement - stop  the current iteration
fruit = ["apple","banana","orange","pineapple","coconut","cucumber"]
for x in fruit:
	if x == "pineapple":
		continue
	print(x)

>>> for x in fruit:
...     if x == "pineapple":
...             continue
...     print(x)
...
apple
banana
orange
coconut
cucumber

# the rang () functioin - a set of special number 

for x in range(10):
	print(x)

>>> for x in range (10):
...     print (x)
...
0
1
2
3
4
5
6
7
8
9

for x in range(10,100):
	print(x)

>>> for x in range (10,100):
...     print(x)
...
10
11
12
13
to 
99

for x in range(10,100,5):
	print(x)
>>> for x in range (10, 100, 5):
...     print(x)
...
10
15
20
25
30
35
40
45
50
55
60
65
70
75
80
85
90
95


#Nested loops

numberA = [1,2,3,4,5]
numberB = [1,2,3,4,5]

for x in numberA:
	for y in numberB:
		print(x,y)
		>>> for x in numberA:
...     for y in numberB:
...             print(x,y)
...
1 1
1 2
1 3
1 4
1 5
2 1
2 2
2 3
2 4
2 5
3 1
3 2
3 3
3 4
3 5
4 1
4 2
4 3
4 4
4 5
5 1
5 2
5 3
5 4
5 5

numberA = [1,2,3,4,5]
numberB = [1,2,3,4,5]
numberC = [1,2,3,4,5]
for x in numberA:
	for y in numberB:
		for z in numberC
			print(x,y,z)

>>> for x in numberA:
...     for y in numberB:
...             for z in numberC:
...                     print(x,y,z)
...
1 1 1
1 1 2
1 1 3
1 1 4
1 1 5
1 2 1
1 2 2
1 2 3
1 2 4
1 2 5
1 3 1
1 3 2
1 3 3
1 3 4
1 3 5
1 4 1
1 4 2
1 4 3
1 4 4
1 4 5
1 5 1
1 5 2
1 5 3
1 5 4
1 5 5
2 1 1
2 1 2
2 1 3
2 1 4
2 1 5
2 2 1
2 2 2
2 2 3
2 2 4
2 2 5
2 3 1
2 3 2
2 3 3
2 3 4
2 3 5
2 4 1
2 4 2
2 4 3
2 4 4
2 4 5
2 5 1
2 5 2
2 5 3
2 5 4
2 5 5
3 1 1
3 1 2
3 1 3
3 1 4
3 1 5
3 2 1
3 2 2
3 2 3
3 2 4
3 2 5
3 3 1
3 3 2
3 3 3
3 3 4
3 3 5
3 4 1
3 4 2
3 4 3
3 4 4
3 4 5
3 5 1
3 5 2
3 5 3
3 5 4
3 5 5
4 1 1
4 1 2
4 1 3
4 1 4
4 1 5
4 2 1
4 2 2
4 2 3
4 2 4
4 2 5
4 3 1
4 3 2
4 3 3
4 3 4
4 3 5
4 4 1
4 4 2
4 4 3
4 4 4
4 4 5
4 5 1
4 5 2
4 5 3
4 5 4
4 5 5
5 1 1
5 1 2
5 1 3
5 1 4
5 1 5
5 2 1
5 2 2
5 2 3
5 2 4
5 2 5
5 3 1
5 3 2
5 3 3
5 3 4
5 3 5
5 4 1
5 4 2
5 4 3
5 4 4
5 4 5
5 5 1
5 5 2
5 5 3
5 5 4
5 5 5


#pass
for x in [1,2,3,4,5]:
	pass

>>> for x in [1,2,3,4,5]:
...     pass
...

>>> for x in [1,2,3,4,5]:
...     if x == 3:
...             pass
...     print(x)
...
1
2
3
4
5

word = ['cat','window','defenestrate']
for w in words:
	print(w, len(w))
>>>word = ['cat','window','defenestrate']
>>> for w in word:
...     print(w, len(w))
...
cat 3
window 6
defenestrate 12

--------

for n in range(2, 10):
	for x in range(2, n):
		if n % x ==0:
			print(n,'equal',x,'*',n//x)
			break
	else:
		#looping fell through without finding  a factor 
		print(n,'is a prime number')
>>> for n in range(2, 10):
...     for x in range(2, n):
...             if n % x ==0:
...                     print(n,'equal',x,'*',n//x)
...                     break
...     else:
...             print(n,'is a prime number')
...
2 is a prime number
3 is a prime number
4 equal 2 * 2
5 is a prime number
6 equal 2 * 3
7 is a prime number
8 equal 2 * 4
9 equal 3 * 3

>>> for n in range(2, 21):
...     for x in range(2, n):
...             if n % x == 0:
...                     print(n,'equal',x,'*',n//x)
...                     break
...     else:
...             print(n,'is a prime number')
...
2 is a prime number
3 is a prime number
4 equal 2 * 2
5 is a prime number
6 equal 2 * 3
7 is a prime number
8 equal 2 * 4
9 equal 3 * 3
10 equal 2 * 5
11 is a prime number
12 equal 2 * 6
13 is a prime number
14 equal 2 * 7
15 equal 3 * 5
16 equal 2 * 8
17 is a prime number
18 equal 2 * 9
19 is a prime number
20 equal 2 * 10
----

for num in range(2,10):
	if num % 2 == 0:
		print("Found an even number", num)
		continue
	print("found a number", num)

>>> for num in range(2,10):
...     if num % 2 == 0:
...             print("Found an even number", num)
...             continue or pass
...     print("found a number", num)
...
Found an even number 2
found a number 3
Found an even number 4
found a number 5
Found an even number 6
found a number 7
Found an even number 8
found a number 9
> for num in range(2,10):
...     if num % 2 == 0:
...             print("Found an even number", num)
...             continue
...             print("number is",num +10)
...     print("found a number", num)
...
Found an even number 2
found a number 3
Found an even number 4
found a number 5
Found an even number 6
found a number 7
Found an even number 8
found a number 9
>>> for num in range(2,10):
...     if num % 2 == 0:
...             print("Found an even number", num)
...             continue
...             num += 10
...             print("number is",num)
...     print("found a number", num)
...
Found an even number 2
found a number 3
Found an even number 4
found a number 5
Found an even number 6
found a number 7
Found an even number 8
found a number 9