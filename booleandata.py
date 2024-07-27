# -*- coding: utf-8 -*-
"""
Title: Boolean data

Date: 07-26-24

Author: Aron James
"""

import time


#The bool function puts 0s as fasle and anything else as true

print(bool(0.3))
print(bool(0))



current_time = time.localtime() #get the current time

hour = current_time.tm_hour #split off the hour part

print('Current time: ', current_time, 'Current hour: ', hour)


#let's make a clock that shows the current time
current_time = time.localtime()

hour = current_time.tm_hour
minute = current_time.tm_min

print('The current time is: ', hour, ':', minute)

#Comparison operators: >, <, >=, <=, ==, !=, 
#Boolean operators: and (&), or (|)

#let's use an if statement to turn our clock program into an alarm clock for waking up at 7:30

if (hour > 7) | (hour == 7 & minute >= 30):
    print('It\'s time to get up!!')
    print('The current time is: ', hour, ':', minute)
else:
    print('Ur trash brock')


#the upper function can be used to convert letters all into upper case. Similarly lower converts all the letter to lowercase

name = 'Aron'
print(name)
print(name.upper())
print(name.lower())
#This can be useful for conditional statements that require name inputs and you don't want to check for CAPS


