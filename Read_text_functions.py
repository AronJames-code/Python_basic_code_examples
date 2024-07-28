# -*- coding: utf-8 -*-
"""
Title: Creating functions to deal with exceptions caused by the user

Date: 07-28-24

Author: Aron James
"""

#The purpose of this is to introduce more techniques using functions that can help deal with a user creating excpetions such as crtl+Cing

#text input function
def read_text(prompt):
    while True:
        try:
            result = input(prompt)
            break #If we get here then no exception was raised and we can break out of the loop
        except KeyboardInterrupt: #This will deal with the user crtl+Cing us
            print('\nPlease enter text')
    return result

name = read_text(prompt = 'Please enter your name: ')

 #Let's try it with numbers
def read_float(prompt):
    while True:
        try:
            result = input(prompt)#reads in the number the user input
            result = float(result)# turns the user input into a float
            break
        except KeyboardInterrupt:
            print('\nThat won\'t work on me') #like before they can't just close the program
        except ValueError:
            print('\nThat was not a valid number...') #accounts for them entering characters similar to the ones you're reading
    return result

number_test = read_float(prompt = 'Please enter a number: ')
print(number_test)


#These functions are nice but it would be even better if we could use them in every program that we write from now on.
#This is what is called a module, also can be known as a library in other languages.
#To do this we need to make sure that our file that contains the functions that we want is in the same folder as whatever new file we are working on.
#Then we just import it by its name, ie, 'import Read_text_functions'. It's then used like any other function.
#If we just want some particular function from the file we can do: 'from Read_text_functions import read_float'.
#Just watch out since imported function definitions can clash with other definitions that are named the same thing.




