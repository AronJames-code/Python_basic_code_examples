# -*- coding: utf-8 -*-
"""
Title: Sorting tables of data

Date: 8-9-2024

Author: Aron James
"""
import random

#Lists act as vectors but sometimes we will need to store data with higher dimensions or matrices. These tables can be thought of as a list of lists, or column in a table.
#This is useful for when we have multiple related lists that would be easier to work with if they were stored in just one dataset. 

#Let's create some sample data first...
#Function for getting 10 random data points each ranging from 1 to 100.
def get_data():
    data = []
    for i in range(1,11):
        data.append(random.randint(1,100))
    return data

#Assigning each day the 10 data points
mon_data = get_data()
tue_data = get_data()
wed_data = get_data()
thu_data = get_data()
fri_data = get_data()
sat_data = get_data()
sun_data = get_data()

#Creating a matrix of the data points for each day
week = [mon_data, tue_data, wed_data, thu_data, fri_data, sat_data, sun_data]

for day in week:
    print(day)

#We can print any individual data point by calling on it using 2 sets of brackets. The first bracket designates the row while the second is the column:
print(week[2][3]) #Remember that python treats the 0th index as the first item in the list so this print statement is calling for the value in row #3 and column #4


#Calculate the total data per week
def total_data(day):
    total = 0
    for value in day:
        total = total + value
    return total

#Take the day totals and put them into their own list or vector
day_totals = []
for day in range(0,len(week)):
    day_totals.append(total_data(week[day]))
print(day_totals)


#A tuple is just like a list but the one significant difference is that it is not possible to change the contents of a tuple.
#The word for this is called 'immutable'.

#A tuple is created as a list of items enclosed in parentheses. 


