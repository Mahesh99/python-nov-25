# Modules
# A Module is a python files containing functions, classes, and variables.

# Importing a Module
# can be done in 5 different ways
# 1. import module_name
# 2. from module_name import function_name  
# 3. from module_name import function_name as fn
# 4. import module_name as mn
# 5. from module_name import *  


# 1. import module_name
import fibonocci

fibonocci.fib(10)
print(fibonocci.fib2(10))
print(fibonocci.first_ten)


# 2. from module_name import function_name
from fibonocci import fib2,fib
print(fib2(5))

# 3. from module_name import function_name as fn
from fibonocci import fib as f,fib2 as f2
f(6)
print(f2(9))

# 4. import module_name as mn
# most commonly used
import fibonocci as fb
fb.fib(4)

# 5. from module_name import *
from fibonocci import *

fib(3)
print(fib2(7))
print(first_ten)





# Why use Modules?
# 1. Reusability: You can reuse the code in multiple programs without rewriting it
# 2. Organization: Modules help in organizing code into manageable sections
# 3. Namespace Management: Modules provide a separate namespace, reducing naming conflicts

# Reusability
import random
print(random.randint(1,101))


# Namespace management
import fibonocci as fb
fb.fib(4)


def fib():
    pass

fib()


# There are 2 types of modules
# 1. Built-in Modules: These are pre-installed with Python (e.g., math, random, os)
# 2. User-defined Modules: These are created by users to organize code (e.g fibonocci.py)

import math
print(math.sqrt(16))
print(math.pi)
print(math.factorial(5))
print(dir(math))

import random
print(random.choice(['apple', 'banana', 'cherry']))
print(random.randrange(10, 50))
print(random.random())  # random float between 0 and 1
list1=[1,2,3,4,5]
random.shuffle(list1)
print(list1)

# Module Search Path
# Python searches for modules in a specific order:
# 1. Current Directory
# 2. PYTHONPATH Directories(Environment Variable)
# 3. Standard Library Directories
# 4. Site-packages Directories (Third-party packages)

import sys
print(sys.path)  # List of directories Python searches for modules
# You can add your own directory to sys.path if needed

import mynewmodule
mynewmodule.testfunc()