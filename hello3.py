# Programming?
# giving set of intructions to the machine to perform a certain task

# Python
# It is a general purpose, high level, interpreted programming language

# machine language(binary) - 0110010 0100010 10101001
# assembly language - nuemonics - 3,2 add
# high level language - human readable 

# compiler - 
# interpretor - line by line checks for errors and executes it

# Arithmetic operators
# +,-,*,/,%(modulus),//(floor div),**(exponentiation)

print(2+3) 
print(3-2)
print(3*2)
print(3/2)

print(5%2)
print(10%2)
print(10%7)

print(3//2)
print(10//7)

print(3**2)
print(2**3)


# Variables
# a name to the value
# let x=10
a=10
b=20
print(a+b)

match_score=230
overs=15
run_rate=match_score/overs
print(run_rate)

todays_min_temp=19

# f=1.8*c+32
c=23
f=1.8*c+32
print(f)
print("welcome to python programming classes")
print("23")


# 100MB
# 100*10^6 Bytes
# 1MB -> 1000KB
# 1Kb -> 1000B
# 1B -> 8 bits
# 1 bit -> 0 or 1

# Comments
# comments are ignored by python interpretor
# Code readability

# 1. single line - #
# 2. Multi line - """ or '''

"""
this is  
a multi line
comment
"""

# 2b=10
# and=20
# hello_3=10
# 3_h=20
# matchscore=10
# match_score=10
# h-2=10

# Data types
# basic or primitive
# int,float,string,bool

# defining a variable
a=10

#accessing a variable
b=a+2
print(a)

#modifying a variable
a=20
print(a)

b=1.2

s="""hello
world
"""
print(s)

# bool - True or False
b=True
b2=False

# type()
print(type(b))
print(type(b2))
print(type(a))
print(type(s))
print(type(1.7))
print(type(1))

# Type conversion/Type casting
# converting one datatype to another
s1="21"
c=int(s1)
print(c)
print(type(c))
print(type(s1))
s2="10"
c=int(s2) #"10" -> c=10
print(c+2)
# print(s2+2)

s3="10.5"
c=float(s3)
print(c)

s4="10"
c=float(s4)
print(c)

# what is the data type of return value of float() -> float
# what is the data type of return value of input() -> string
# what is the data type of return value of int() -> string

# a=input("Enter something:")
# print(a)

k=10+20/2

# str()
a=str(10)
b=str(4.5)
c=str('hi')
d=str(True)

# string operations
# +(concatenation),*(repetition)
# + -> only 2 strings can be concatenated
k=""
s1="hello"
s2="world"
s3=s1+" "+s2
print(s3)

s4=s1*5
print(s4)

print(s1+"5")
# print(s1+5)
