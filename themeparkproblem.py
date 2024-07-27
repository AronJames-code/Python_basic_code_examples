# -*- coding: utf-8 -*-
"""
Title: Theme Park Ride Age Requirement Determiner

Date: 07-26-24

Author: Aron James
"""
#The purpose of this code is just to show basic examples of nested if statements and practicing conditional statements

print('''Welcom to the Theme Park!
      
Here are the available rides:\n
1. Scenic River Cruise
2. Carnival Carousel
3. Jungle Adventure Water Splash
4. Downhill Mountain Run
5. The Regurgitator''')

user_selection = input('\nPlease select the number that corresponds to the ride: ')
user_selection = int(user_selection)

#Nested if statemnets are used to filter the age requirements for theme park rides
if (user_selection == 1):
    print('This ride has no age requirements.')
if (user_selection == 2):
    age = input('Please enter your age in years: ')
    age = int(age)
    if (age >= 3):
        print('You are eligible to ride.')
    else:
        print('You are not eligible to ride.')
if (user_selection == 3):
    age = input('Please enter your age in years: ')
    age = int(age)
    if (age >= 6):
        print('You are eligible to ride.')
    else:
        print('You are not eligible to ride.')
if (user_selection == 4):
    age = input('Please enter your age in years: ')
    age = int(age)
    if (age >= 12):
        print('You are eligible to ride.')
    else:
        print('You are not eligible to ride.')
if (user_selection == 5):
    age = input('Please enter your age in years: ')
    age = int(age)
    if (age >= 12) & (age < 70):
        print('You are eligible to ride.')
    else:
        print('You are not eligible to ride.')
else:
    print('Please try again and input a valid number next time, ie, a number between 1 and 5.')


