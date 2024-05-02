# PYTHON FUNCTIONS
def greet(): #function definition
    print('hello world') #function body

greet() #calling a function
def number():
    print(44)

number()
def add():
    num1=20
    num2=30
    sum=num1+num2
    print(sum)

add()
add()
number()

def s():
    sub=40-4
    print(sub)

s()
def divi():
    prod=40/6
    print(prod)

divi()
def how():
    string="how are you?"
    return string

print(how())

def lists():
    fruits=['mnago', 'banana','guava','avocado']
    return fruits

print(lists())

def addition(num1,num2): #num1 and num2 are parameters
    sum1=num1+num2
    return sum1

addition(30,50)
print(addition(30,50)) #30 and 50 are arguments passed to num1 and num2 parameters
print(addition(90,40))
print(addition(30,66))
print(addition(75,88))

def naming(name):
    """this function is for printing the name and a string"""
    print(f'hello {name},how was your day')

naming('john')
naming('jesse')
naming('minna')

def area(radius):
    return 3.142*radius**2

print(area(7))
print(area(14))
print(area(27))

import math
def area1(r):
    return math.pi*r**2
print(area1(7))

print(math.sqrt(81))
print(math.log(50))

from math import factorial
print(factorial(4)) #4!=1*2*3*4 5!=1*2*3*4*5
