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
from fibonocci import fib2
print(fib2(5))

# 3. from module_name import function_name as fn
from fibonocci import fib as fibonacci_function
fibonacci_function(6)

# 4. import module_name as mn
import fibonocci as fb
fb.fib(4)

# 5. from module_name import *
from fibonocci import *

fib(3)
print(fib2(7))
print(first_ten)