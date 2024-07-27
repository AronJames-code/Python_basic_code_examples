# -*- coding: utf-8 -*-
"""
Title: Greeter

Date: 07-25-24

Author: Aron James
"""
#Write a basic program in python for greeting people

#Asks the user for their name
name = input('Please enter your name: ')
print('Hello', name)


#The int function can be used to convert a string into a number varbable
age_text = input('Please enter you age in years : ')
age_int = int(age_text) #converts string age data into integer
age_in_10_years = age_int + 10
print('Your age in a decade will be ', age_in_10_years)
#this doesn't work if the user doesn't enter an integer


#A more effecient way
age = int(input('Please enter you age in years: '))
print('Your age in a decade will be ', age + 10)
#can be useful but makes the program a bit harder to understand
# this can become a big deal for larger more complicated programs


#We can also convert a string into a floating point value
age_text = input('Please enter you age in years : ')
age_float = float(age_text)
age_in_10_years = age_float + 10
print('Your age in a decade will be ', age_in_10_years)

#You can convert between int and float values. Beware that when going from float to integer it always rounds down
#Floating point values are always truncated and so the fractional part is always discarded