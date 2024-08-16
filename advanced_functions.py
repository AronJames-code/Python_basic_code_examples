# -*- coding: utf-8 -*-
"""
Title: Advanced Functions

Date: 8-16-2024

Author: Aron James
"""
import time

def func_1():
    print('This is function 1')
    
def func_2():
    print('This is function 2')
    
x = func_1
x()
y = func_2
y()


#Robot Dancer
def forward():
    print('Robot moving foward')
    time.sleep(1)
    
def backward():
    print('Robot moving backward')
    time.sleep(1)
    
def left():
    print('Robot moving left')
    time.sleep(1)
    
def right():
    print('Robot moving right')
    time.sleep(1)

dance_moves = [forward, backward, left, right]

def Dance(moves):
    print('Dance time...')
    for move in moves:
        move()
    print('Dance over')
    
    
Dance(dance_moves)


#Lambda expressions are tiny functions that can be written on one line
def increment(x):
    return x + 1

increment_lambda = lambda x : x + 1
#These two functions above do the same thing
print(increment(4))
print(increment_lambda(4))


numbers = [1,2,3,4,5,6,7,8]
list(numbers)
incremented_numbers = map(increment, numbers)
list(incremented_numbers)

#This can be done quicker with lambda wince we wouldn't have need to create the increment function in the first place
lambda_numbers = map(lambda x : x + 1, numbers)
list(lambda_numbers)


#The yield function returns a results to the caller, but python remembers the position reached in the function.
def yielding():
    yield 1
    yield 2
    yield 3
    yield 4

for i in yielding():
    print(i)

list(yielding())

def yield_return():
    yield 1
    yield 2
    return 3
    yield 4

for i in yield_return():
    print(i)
#This highlights the difference between yield and return. The values of yield are shown but when return is reached, the function stops. 
#3 isn't shown because that's not how return works and yield 4 doesn't print because return stops the function before it is reached. 


#We can create functions that accept an arbitrary number of arguments, this is done using an asterisk

def add_function(*values):
    total = 0
    for value in values:
        total = total + value
    return total

add_function(1, 2)
add_function(1,2,3,4,5,6)

#We can also force the user to supply at least one number in a function before making the rest of inputs arbitrary:
def add_function_2(start, *values):
    total = 0
    for value in values:
        total = total + value
    total = total + start
    return total

#Lastly we can't give lists are arguments to functions unless we use an askerisk to 'unpack' them first
num_list = [1,2,3,4]

add_function(*num_list)

#Note that there is also a much easier way to create an add function as it already exists as sum
def add_function_3(*values):
    return sum(values)

add_function_3(*num_list)


