# -*- coding: utf-8 -*-
"""
Title: Dictionaries

Date: 08/12/2024

Author: Aron James
"""

#A dictionary is another collection mechanism in python that stores data and locates particular data using a key
#This is similar to how a real life dictionary stores definitions and we find those by using key words


prices = {} #this squiggly braces are used to create a dictionary
#We can add an item to the dictionary by giving the key and the value to be stored.
prices['Bagel'] = 1.5
print(prices['Bagel'])

#We can check whether a dictionary contains a key
print('Bagel' in prices) #Returns true since 'Bagel' is part of the dictionary
print('No Bagel' in prices) #Returns false as this isn't in the dictionary.

prices['Donut'] = 2.0
prices['Coffee'] = 4.0

#We can print the entire dictionary:
print(prices)
#Note that trying to print and indexed part of the dictionary will not work, ie, prices[0] 
#This is the main difference between a dictionary and a list or tuple

#We can also create a dictionary with multiple items in one statement:

prices_2 = {'Bagel': 1.5, 'Donut': 2.0, 'Coffee': 4.0}
print(prices_2)

#We can delete entries:
del(prices['Bagel'])
print(prices)

