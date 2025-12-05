# Functions
# A function is a block of code that performs a specific task.
# It can take inputs, process them, and return an output.
# Functions help in code reusability and modularity.

# naming rules for functions are same as variables
# function syntax
"""
def function_name(parameters):
    # function body
    return value
"""

# function definition
import random


def greet(name):
    print(f"Hello, {name}!")

def greet_world():
    print("Hello, World!")


# function call
greet("Alice")
# greet()
greet("Bob")

def guess_the_number():
    number = int(input("Guess a number between 1 and 10: "))
    given_number = random.randint(1,11)
    if number == given_number:
        print("Congratulations! You guessed it right.")
    else:
        print("Try again!")

guess_the_number()
greet("Charlie")
guess_the_number()





def triangle_area(base, height):
    area = 0.5 * base * height
    return area

area1 = triangle_area(5, 10)
print(f"Area of triangle with base 5 and height 10 is {area1}")
area2 = triangle_area(7, 3)
print(f"Area of triangle with base 7 and height 3 is {area2}")
    
