# Introduce Functions, WHat are they? How do they improve Coding? Advantages of Functions
# Functions without parameters
# # 1st Function
def welcome():
    print("This is my first fuction")

# 2nd Function
def add():
    num1 = 20
    num2 = 89
    answer = num1 + num2
    print('The addition is ', answer)
 

# 3rd Function
def substract():
    num1 = 20
    num2 = 89
    answer = num1 - num2
    print('The Difference is ', answer)

# Function call
welcome()
add()
substract()

# Students to Do a function to divide and multiply two numbers
# Guide on some they try the multiple/division as they call the functions.
# From this example tehy can understand that fuctions can split a large code into small bits.

#EG1
def greet(name):  # 'name' is a parameter
    print(f"Hello, {name}!")

greet("Alice")  # 'Alice' is an argument passed to the 'name' parameter

# add 
def add(x, y):  # 'x' and 'y' are parameters
    result = x + y
    return result

sum_result = add(3, 5)  # 3 and 5 are arguments passed to 'x' and 'y' parameters

#nested function
def outer_function():
    x = 5
    def inner_function():
        print(x)
    inner_function()
outer_function()

import math

def calculate_area(radius):
    return math.pi * radius ** 2

print(calculate_area(7))

