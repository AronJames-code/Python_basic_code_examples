# -*- coding: utf-8 -*-
"""
Title: Functions

Date: 07-28-24

Author: Aron James
"""

#Functions help break up a large solution into individual components. 
#they're especially helpful for when you need to perform a set of statements multiple times throughout the code

#Here's a simple function that just says hello
def greeter():
    print('Hello loser.')

#Notice that when we run the above chunk of code nothing happens, well nothing that produces as output that is
#We can call the function by running the function name or even variables assigned to it

greeter() #this will print 'Hello loser'.
x = greeter
x()
#Here x is set to the value of greeter. then we call x as if it is a function by including the ()



#Functions can also call other functions
def m2():
    print('the')

def m3():
    print('sat on')

def m1():
    m2()
    print('cat')
    m3()
    print('mat')
    

m1()
#This is sort of similar to how if statements and loops can be nested within each other.


#Parameters are the things that go into the function which are needed for some fucntions to produce an output. They go in the paranthesis and are separated by commas
#Our examples thus far have had no parameters and thus empty paranthesis ()

def print_times_table(multiple):
    count = 1
    while (count <= 12):
        product = count * multiple
        print(count, 'x', multiple, '=', product)
        count = count + 1
#This code creates an elementary school times table sheet

print_times_table(99) #Here you can enter different values in place of the parameter. variables are also allowed
#Here our value, 9, is called the argument which is the thing that's being passed into the function. The parameter, multiple, is the name within the function that represents the argument


#Functions can also have multiple parameters
def super_times_table(multiple, max_value):
    count = 1
    while (count < max_value + 1): #We need the +1 since python excludes the upper bound. We could also say 'while (count <= max_value):' like before
        product = count * multiple
        print(count, 'x', multiple, '=', product)
        count = count + 1

super_times_table(5, 25) #The second argument here is a limit on how many times tables we are printing. Before we defined it to be <= 12 but now we can choose

        
#What if we want this function to work with integer values only? Python has a built in function called isinstance

def super_times_table_2(multiple, max_value):
    if isinstance(multiple, int) == False:
        raise Exception('This only works correctly with integer values!!')
    if isinstance(max_value, int) == False:
        raise Exception('This only works correctly with integer values!!')
    count = 1
    while (count < max_value + 1): #We need the +1 since python excludes the upper bound. We could also say 'while (count <= max_value):' like before
        product = count * multiple
        print(count, 'x', multiple, '=', product)
        count = count + 1

super_times_table_2('Ur trash', 12)
super_times_table_2(5, 'Brock')

#In case we forget what positions our parameters were placed python also allows us to use keywords to identiy arguments

super_times_table_2(multiple = 8, max_value = 12)
#This means we can also input the arguments out of order if we feel like it for some reason or forget the order. I wouldn't get into the habbit of doing this as it will just make stuff confusing.
super_times_table_2(max_value = 12, multiple = 8)



#We can also provide default values for our functions. This allows for the user flexibility to choose their argument values but we have a predefined one anyways.
def super_times_table_3(multiple, max_value = 12): #Here we can set the max_value to be 12 since that is common for times tables but the user has the option to change it.
    if isinstance(multiple, int) == False:
        raise Exception('This only works correctly with integer values!!')
    if isinstance(max_value, int) == False:
        raise Exception('This only works correctly with integer values!!')
    count = 1
    while (count < max_value + 1): #We need the +1 since python excludes the upper bound. We could also say 'while (count <= max_value):' like before
        product = count * multiple
        print(count, 'x', multiple, '=', product)
        count = count + 1

super_times_table_3(6) #This goes up to 12 x 6 just as expected
super_times_table_3(6, 20) #This goes up to 20 as we specified here. 



#Functions are also able to return values 
#Here's an example with a very simple function whose sole purpose is to take an integer argument, add 4 to it, and return the resulting sum.
def add_4(input):
    sum = input + 4
    return sum #Here the function is returning a value

output = add_4(5) #let's set the sum returned to a new variable
print(output)
#Note that the execution of a function will end when a return statement is reached. This means we cannot have multiple things returned. 



#Variables that are created within a function are called 'local variables'. They exist only within the fucntion itself and can't be called outside the function
#THe benefit of this is we are able to reuse variable names for all of our functions. For example many coders will use the variable i for counting (iterating)
#so because each function stores local variables, we can keep using i every time instead of doing like i1, i2, i3, i4, ... etc. 
#Sometimes a program will contain data that needs to be shared among all functions. To do this we declare these variables outside of the function and then pass them
#into the functions as arguments. Below is an example to illustrate:
number = 1
def function_1():
    number = 2
    print(number)

function_1()
print(number)
#Here both variables are called 'number' but they clearly contain different values. number = 1 is a global variable while number = 2 is a local variable


