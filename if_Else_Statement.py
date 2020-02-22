#Boolean Expression

print(20 > 10)
print(20 == 10)
print(20 < 10)
print(bool("hello World"))
print(bool(20))

Python Condition 

Equals						-> x ==y
Not Equals					-> x !=y
less than					-> x < y
less or equal to			-> x <=y
Greater than				-> x > y
Greater than or equal to	-> x >=y
Boolean OR 					-> x or y, x | y
Boolean AND					-> x and y, x & y
Boolean NOT 				-> not x
>>> print(20 > 10)
True
>>> print(20 < 10)
False
>>> print(20 == 10)
False
>>> print(bool("hello World"))
True
>>> print(bool(20))
True
>>> x = 70
>>> y = 60
>>> if x > y:
...     print("x is greater than y")
... else:
...     print("x is not greater than y")
...
x is greater than y
>>> if x < y:
...     print("x is grater than y")
... else:
...     print("x is not grater than y")
...
x is not grater than y
>>> if x < y:
...     print("x is grater than y")
... else:
...     print("x is not grater than y")
...
x is not grater than y
>>> if x > y:
...     print("x is greater than y")
... elif x >= y:
...     print("x is greater than or equal to y")
... elif y < x:
...     print("y is smaller than x")
... else:
...     print("x is nothing")
...
x is greater than y
>>> if x == y:
...     print("Answer 1")
... elif x < y :
... 	print("Answer 2")
... elif x<=y:
...      print("Answer 3")
... else:
...     print("Default")
...
Default
>>>

#short hand if
if x > y: print("x is greater than y")

>>> x = 50
>>> y = 150
>>> if x > y: print("x is greater than y")
... elif x == y: print("x and y are equal")
... else:print("x is less than y")
...
x is less than y
>>> x = 50
>>> y = 150
>>> print(x) if x > y else print(y)
150

#and is logical operator

>>> x = 50
>>> y = 40
>>> z = 100
>>> if x > y and z > x:
...     print("All conditions are ture")
...
All conditions are ture
>>> if x < y and z > x:
...     print("All conditions are ture")
... else:
...     print("Some comdition are false")
...
Some comdition are false

# or is a logical operator

>>> x = 50
>>> y = 40
>>> z = 100
>>> if x > y or z < y:
...     print("One conditions are ture")
... elif x > y and z > y:
...     print("All conditions are ture")
... else:
...     print(
... "nothing else")
...
One conditions are ture

>>> if x > y and x > y and z > x:
...      print("Answer1")
... elif x == y or z == y or z > y and x > y and  x > y:
...     print("Answer2")
... elif z > y and y < x or z > y:
...     print("Answer3")
... else:
...     print("Default")
Answer1
if x > y and x > y and z > x:
      print("Answer1")
 elif x == y or z == y or z > y and x > y and  x > y:
     print("Answer2")
 elif z > y and y < x or z > y:
     print("Answer3")
 else:
     print("Default")
Answer1

x = int(input("Please Enter your Number:"))
if x <= 90 and x == 100:
	print("Grade A") 
elif x >= 80 and x == 89:
	print("Grade B")
elif x >= 60 and x == 79:
	print("Grade C")
elif x >=50 and x == 59:
	print("Grade D")
elif x <= 50:
	print("Grade F") 
else:
	print("nothing")


x = 50
if  x > 10:
	print("x is ten")
	if x > 20:
		print("x is greater than 20")
	else:
		print("No, x is greater than 20")

if x > 10 and x != 10 or x > 20:
	print("x is greater than 10 and 20")
else:
	print("x is not greater than 10 & 20")


>>> x = 50
>>> if  x > 10:
...     print("x is ten")
...     if  x > 20:
...             print("x is greater than 20")
...     else:
...             print("No, x is greater than 20")
...
x is ten
x is greater than 20



>>>loops
>>> student = "SFU"
>>> Batch = "3"
>>> Gender = "Male"
>>> if student == "SFU":
...     print("You\'re SFU student")
...     if Batch =="3":
...             print("Yes, I'm form batch 3")
...     else:
...             print("No, I'm form other batch")
... else:
...     print("You'are not SFU student")
...
You are SFU student
Yes, i am form batch3


