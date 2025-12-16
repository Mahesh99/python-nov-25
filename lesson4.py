# Modules
# A Module is a python files containing functions, classes, and variables.


# When a module is imported, the code in the module is executed once, and the functions, classes, and variables defined in the module become available for use in the importing code.

# Importing a Module
# can be done in 5 different ways
# 1. import module_name
# 2. from module_name import function_name  
# 3. from module_name import function_name as fn
# 4. import module_name as mn
# 5. from module_name import *  


# 1. import module_name
import fibonocci
print("just imported fibonocci module")


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

# import mynewmodule
# mynewmodule.testfunc()







# __name__ Variable
# When a module is run directly, the __name__ variable is set to "__main__"




print(__name__)  # This will print "__main__" when run directly
print(fibonocci.__name__)  # This will print "fibonocci"
print(math.__name__)  # This will print "math"


import guessthenumber
# guessthenumber.guess_the_number()


# pip - Python Package Installer

# pip is a package manager for Python that allows you to install and manage additional libraries and dependencies


# To install a package: pip install package_name
# To uninstall a package: pip uninstall package_name
# To list installed packages: pip list
# To upgrade a package: pip install --upgrade package_name
# Example: Installing requests package
# pip install requests

# we install packages using pip in command prompt/terminal, not in the code file



# what is a package?
# A package is a collection of Python modules organized in directories that provide specific functionality.
# Example: requests package for making HTTP requests

# Instagram package example
# instagram will divide the whole code into multiple modules and again group those modules into a package called instagram
# for example:
# instagram/
#     __init__.py
#     user.py
#     post.py
#     comment.py
#     utils/
#     utils/__init__.py
#     utils/helpers.py

# __init__.py file indicates that the directory is a package
# is used to initialize the package and can also define what is available when the package is imported


# requests package is used to make HTTP requests in Python
import requests
response=requests.get("https://pramanicus.com")
print(response.status_code)
print(response.headers)
print(response.text[:100])  # print first 100 characters of the response content