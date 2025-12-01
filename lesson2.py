# conditional statements in Python 
# if, if-else, if-elif-else
# indentation is important in Python
# even odd
# greater number among two numbers
# greatest number among three numbers

# if syntax
"""
if condition:
    # code to be executed if condition is True
"""

# battery=int(input("Enter battery level: ")) # 25 12
# if battery < 20:
#     print("Low battery!")
#     print("Please charge your device.")

# print("some print statement after if block")





# if-else syntax
"""
if condition:
    # code to be executed if condition is True
else:
    # code to be executed if condition is False
"""

# number=int(input("Enter a number: ")) # 7 8
# if number % 2 == 0:
#     print(f"{number} is even")
# else:
#     print(f"{number} is odd")

# print("some print statement after if-else block")



# loan eligibility
# age=int(input("Enter your age: "))  # 25 17
# salary=int(input("Enter your salary: "))  # 50000 15000

# if age >= 18 and salary >= 20000:
#     print("You are eligible for the loan.")
# else:
#     print("You are not eligible for the loan.")



# if-elif-else syntax
""" 
if condition1:
    # code to be executed if condition1 is True
elif condition2:
    # code to be executed if condition2 is True
else:
    # code to be executed if both condition1 and condition2 are False


else is optional    
"""


# grading system
# O,A,B,C,D,No grade,Fail
# marks=int(input("Enter your marks: "))  # 95 85 75 65 55 45 30
# if marks >= 90:
#     print("Grade: O")
# elif marks >= 80:
#     print("Grade: A")
# elif marks >= 70:
#     print("Grade: B")
# elif marks >= 60:
#     print("Grade: C")
# elif marks >= 35:
#     print("No grade")
# else:
#     print("Fail")

# print("some print statement after if-elif-else block")




# nested if
# number=int(input("Enter a number: "))  # 15 -5 0
# if number % 3 ==0:
#     if number % 5==0:
#         print(f"{number} is divisible by both 3 and 5")
#     else:
#         print(f"{number} is divisible by 3 but not by 5")
#     print(f"{number} is divisible by 3 but not by 5")
# else:
#     print(f"{number} is not divisible by 3")

"""
# what all are considered False in Python?
constants defined to be false: None and False
zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
empty sequences and collections: '', (), [], {}, set(), range(0)
"""

# Loops in Python
# for loop, while loop

# when do we use loops?
# to execute a block of code multiple times

# for loop syntax
"""
for variable in iterable:
    # code to be executed for each item in the iterable

iterable: list, tuple, string, range, etc.
iterable is an object which can be iterated over (one item at a time)
"""

# for i in range(100):
#     print("hello")

s="python programming"
for c in s:
    print(f"{c}-hi")


l=[10,20,30,40,50]
for num in l:
    print(num*2)

s={'one', 'two', 'three'}
for item in s:
    print(item)

rollnos=["13311A1247","13311A1248","13311A1249","13311A1250"]
for no in rollnos:
    print(no[-2:])

fruits=["apple","banana","cherry"]
for fruit in fruits:
    print(fruit.upper())

for fruit in fruits:
    if fruits.index(fruit)==0:
        print(fruit.upper())
    else:
        print(fruit)

"""
fruits=["apple","banana","cherry"]
iteration 1:
fruit="apple"
if fruits.index(fruit)==0: => 0==0
    print(fruit.upper()) <------

iteration 2:
fruit="banana"
if fruits.index(fruit)==0: => 1==0
    print(fruit.upper())
else:
    print(fruit)<------

iteration 3:
fruit="cherry"
if fruits.index(fruit)==0: => 2==0 
    print(fruit.upper())
else:
    print(fruit)<------

"""

if True:
    print("Hello")

if "":
    print("World")
l=[1,2,3]
if l:
    print("Python")

k=["a","b","c"]
for i in k:
    print(i+i) #'a'+'a' => 'aa'


# range() function
# generates a sequence of numbers
#
# syntax: 
# range(start, stop, step)

# range(stop) => start=0, step=1
# range(start, stop) => step=1
# range(start, stop, step)

for i in range(5):  # 0 to 4
    print(i)

for i in range(7):
    print(i)

for i in range(2, 8):  # 2 to 7
    print(i)

for i in range(1, 10, 2): 
    print(i)

for i in range(2,11,2):
    print(i)

for i in range(20,201,20):
    print(i)

"""
2x1=2
2x2=4
2x3=6
"""
for i in range(2,21,2):
    print(f"2x{i//2}={i}")

for i in range(10,0,-1):
    print(i)


# while loop syntax
"""
while condition:
    # code to be executed as long as condition is True
"""

count=1

while count <= 10:
    print(count)
    count += 1

# print numbers from 10 to 1
count=10
while count >= 1:
    print(count)
    count -= 1

count=2


while count <= 20:
    print(count)
    count += 2

while False:
    print("hello")

# while True:
#     print("hello")

# continue
# example
# continue statement is used to skip the current iteration and move to the next iteration of the loop
for i in range(1,11):
    if i % 2 == 0:
        continue
    print(i)



# print odd numbers from 1 to 20
for i in range(1,21):
    if i == 5 or i == 11 or i ==17:
        continue
    print(i)
    print("hi")

l=['a','b','c','d','e']
for item in l:
    print(item)
    if item == 'c':
        continue

# 2 continue statements
for i in range(1,16):
    if i % 3 == 0:
        continue
    print(i)
    if i % 5 == 0:
        continue
    
c=10
# while c > 0:
#     if c == 7 or c == 3:
#         # c-=1
#         continue
#     print(c)
#     c -= 1

# list comphrehension
# squares of numbers from 1 to 10
squares=[i**2 for i in range(1,11)]
print(squares)

nums=[i for i in range(1,11)]
print(nums)

tens=[i*10 for i in range(1,11)]
print(tens)

evens=[i for i in range(2,11,2)]
print(evens)

odds=[i for i in range(1,11,2)]
print(odds)                 

odds=[i for i in range(1,11) if i%2!=0]
print(odds)             

# list with varaible strings
lstrs=["hi","hello","python","programming","data","science","machine","learning"]


str5len=[s for s in lstrs if len(s)<=5]
print(str5len)

# if else in list comprehension
parity=["even" if i%2==0 else "odd" for i in range(1,11)]
print(parity)

l2=[i//i if i%2==0 else i**2 for i in range(1,11)]
print(l2)

# nested loops in list comprehension
pairs=[(i,j) for i in range(1,6) for j in range(1,3)]
print(pairs)

pairs2=[(i,j) for i in range(1,6) for j in range(1,3) if i!=j]
print(pairs2)

l=['rahul','sachin','sourav','virat']
s=['chary','kumar','singh']
combinations=[char+" "+k for char in l for k in s]
print(combinations)

