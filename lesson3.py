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