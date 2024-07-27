# -*- coding: utf-8 -*-
"""
Title: Variables

Date: 07-25-24

Author: Aron James
"""

#Assign variables to integers and floats
num = 5
print(num)
num = num + 5
print(num)

#Also assign variables to strings
customer_name = 'Fred'
print(customer_name)

message = 'The name is ' + customer_name
print(message)

#Triple quotes and double quotes can be used to include quotes as part of the text
#If python doesn't like you putting apostrophes or quotes in you text, add more quotes to the whole thing to make it work
print('''... and then Luke said It's a trap''')
print('''... and then Luke said "It's a trap"''')
#These may also be used to span a string over multiple lines


#Similar things can also be accomplished using escape characters
print('\\') #prints \
print('\'') #prints '
print('\"') #prints "
print('hi bill\nhi tom') #create a new line
print('hi bill \thi tom') #create a tab indent
print('hi bill \r hi tom') #return the printing position to the start of the line(useless essentially)
print('\a') #makes the windows sound


#Input functions wait for the user to type in a string and hit the enter key.
name = input('Enter you name please: ')
#can also be used similar to the sleep function
input('Press Enter to continue...') #Might as well just use the sleep function though




