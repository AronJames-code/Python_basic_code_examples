# -*- coding: utf-8 -*-
"""
Title: Creating a user menu

Date: 8-8-24

Author: Aron James
"""

#This program will print out a user menu and then allow the selection of the desired function. Taken from the begin to code with python book by Rob Miles
#This also introduces the 'elif' statement which is just else if in one word

def print_sales():
    pass

def sort_high_low():
    pass

def sort_low_high():
    pass

def highest_lowest():
    pass

def total_sales():
    pass

def average_sales():
    pass

def enter_figures():
    pass

#Note that to be orderly and neat we can even create these functions in a different file and import it into this one before coding
menu = '''Ice Cream Sales

1. Print the Sales
2. Sort High to Low
3. Sort Low to High
4. Highest and Lowest
5. Total Sales
6. Average Sales
7. Enter Figures


Enter your command: '''

command = input()
command_int = int(command)
#We might want to reuse our code form earlier which prevents the user from entering non valid inputs such and non integers in this case.

if command_int == 1:
    print_sales()
elif command_int == 2:
    sort_high_low()
elif command_int == 3:
    sort_low_high()
elif command_int == 4:
    highest_lowest()
elif command_int == 5:
    total_sales()
elif command_int == 6:
    average_sales()
elif command_int == 7:
    enter_figures()

#This is a solid menu layout




