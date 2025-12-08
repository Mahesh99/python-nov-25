# Functions
# A function is a block of code that performs a specific task.
# It can take inputs, process them, and return an output.
# Functions help in code reusability and modularity.

# naming rules for functions are same as variables
# None is keyword that represents the absence of a value
# function syntax
"""
def function_name(parameters):
    # function body
    return value
"""

# function definition
import random

# example 1
def greet(name):
    print(f"Hello, {name}!")

def greet_world():
    print("Hello, World!")


# function call
greet("Alice")
# greet()
greet("Bob")

# example 2
def guess_the_number():
    number = int(input("Guess a number between 1 and 10: "))
    given_number = random.randint(1,11)
    if number == given_number:
        print("Congratulations! You guessed it right.")
    else:
        print("Try again!")

# r=guess_the_number()
# print(r)  # This will print None since the function does not return anything
greet("Charlie")
# guess_the_number()




# example 3
# base =5, height=10
def triangle_area(base, height):
    area = 0.5 * base * height
    return area

area1 = triangle_area(5, 10)
print(f"Area of triangle with base 5 and height 10 is {area1}")
area2 = triangle_area(7, 3)
print(f"Area of triangle with base 7 and height 3 is {area2}")
    
# ln=len(l)

l=[1,2,3,4,5]


# example 4
# input_list = l
def modify_list(input_list):
    input_list.append(6)
    print(input_list)

modify_list(l)
print(l)  # l is modified because lists are mutable
# print(input_list) 



# Function with default parameter
# during function definition, parameters with default values are defined at the end
# if no argument is passed for that parameter during function call, the default value is used
# syntax
"""
def function_name(param1, param2, param3=default_value, ...):  
    # function body
    return value
"""

# example 1
def power(base, exponent=2):
    return base ** exponent

result1 = power(3)
print(f"3 squared is {result1}")

result2 = power(2, 3)
print(f"2 cubed is {result2}")

# example 2
def introduce(name, age=18, country="India"): 
    print(f"My name is {name} and I am {age} years old. I live in {country}.")

introduce("David")
introduce("Eva", 25)
introduce("Frank", country="USA")
introduce("Frank", country="USA", age=28)
introduce("Grace", 30, "Canada")

print("hello")
print("hello",end=" ")
print("hello",end=" ")
print()




# Function with variable number of arguments
# syntax
"""
def function_name(*args):
    # function body
    return value
"""

# example 1
# args=tuple of arguments # args=(1,2,3)
def summarize(*args):
    total = 0
    for num in args:
        total += num
    return total

sum1 = summarize(1, 2, 3)
print(f"Sum of 1, 2, 3 is {sum1}")

sum2 = summarize(5, 10, 15, 20)
print(f"Sum of 5, 10, 15, 20 is {sum2}")

sum3 = summarize()
print(f"Sum with no arguments is {sum3}")



# keyword arguments
# Function with variable number of keyword arguments
# syntax
"""
def function_name(**kwargs):
    # function body
    return value
"""


# example 1
# kwargs=dict of arguments # kwargs={'name':'Alice', 'age':30, 'city':'New York'}
def display_info(**kwargs):
    print(kwargs.items())
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=30, city="New York")
display_info(country="USA", profession="Engineer")


# positional and keyword arguments together
# example 1
def order_food(main_course, *sides, drink="Water", dessert="None", **extras):
    print(f"Main Course: {main_course}")
    print(f"Sides: {sides}")
    print(f"Drink: {drink}")
    print(f"Dessert: {dessert}")
    print(f"Extras: {extras}")

order_food("Pizza", "Fries", "Salad", drink="Soda", dessert="Ice Cream")
order_food("Burger", "Onion Rings")
order_food("Pasta", cheese="Extra Cheese", sauce="Marinara")

"""
Types of arguments:
1. Positional Arguments
2. Default Arguments
3. Variable-length Arguments (*args)
4. Variable-length Keyword Arguments (**kwargs)
"""



def test_func(a,b=10):
    c=a+b
    print(a)
    return c

k=test_func(10,5) + test_func(3)
print(k) 



def greatest():
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    if a>b:
        print("a greater")
    else:
        print("b greater")


# only when we call the function, the code inside it will run
# greatest()


# LEGB
# Local, Enclosing, Global, Built-in
# definition
# whenever you try to access a variable, Python looks for it in the following order: 
# 1. Local (inside the current function)
# 2. Enclosing (inside enclosing functions)
# 3. Global (at the top-level of the module)
# 4. Built-in (Python's built-in names)

x=100  # global variable
def outer_function():
    x=200  # enclosing variable
    def inner_function():
        x=300  # local variable
        print("Inner function x:", x)
    inner_function()
    print("Outer function x:", x)

outer_function()



# len("hello")  # built-in function
# print(dir(__builtins__))


k=5
def func1():
    global k
    k=10
    print("inside func1:",k)
func1()
print("outside func1:",k)


# lambda functions
# anonymous functions
# syntax
""" 
lambda parameters: expression
"""
# example 1
square = lambda x: x ** 2

# def square(x):
#     return x ** 2

result = square(5)
print(f"Square of 5 is {result}")


add = lambda x, y: x + y
result = add(3, 7)
print(f"Sum of 3 and 7 is {result}")

print(add(10,20))


# example 2
# sorting a list of tuples based on the second element
data = [(1, 3), (2, 1), (4, 2), (3, 5)]
# data.sort(reverse=True)
data.sort(key=lambda x: x[1]) # 3,1,2,5
print(data)

# l=[5,2,9,1]
# l.sort()
# print(l)

# high-order functions
# functions that take other functions as arguments or return functions as results
# map() and filter() are examples of high-order functions

ran_nums = [4,5,12,9,6]

# example 1 - map
# using map to square each number in the list
squared_nums = list(map(lambda x: x ** 2, ran_nums))
# squared_nums = list(map(lambda x: x ** 2, [4,5,12,9,6]))
print("Squared numbers:", squared_nums)

# example 1 - filter
# using filter to get even numbers from the list
even_nums = list(filter(lambda x: x % 2 == 0, ran_nums))
print("Even numbers:", even_nums)

# example 2 - filter
# filter words with length greater than 4
words = ["apple", "banana", "cherry", "date", "fig", "grape"]
long_words = list(filter(lambda word: len(word) > 4, words))
print("Long words:", long_words)