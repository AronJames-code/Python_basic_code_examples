# -*- coding: utf-8 -*-
"""
Title: Storing Collections of Data

Date: 8-8-24

Author: Aron James
"""
from Read_text_functions import * #We want to use our read_float function from last time

#Lists in Python

#Use brackets [] to create a list in Python
sales = []
#After creating a list we can append (add) stuff to the list
sales.append(32)
print(sales)
print(sales[0])
#Here notice that the first print statement printed out the entire list while the second print statement printed out the specific item that was indexed in the list
#Again Python indexing starts at 0 so we index 0 in order to print the first item, 1 for the second, etc. 
#We can keep using the append command to add more items to the list if we want to
sales.append(31)
print(sales)


#By specifiying the index we can changed particular items in the list as well
sales[1] = 50
print(sales)
#In the above code, we changed our value at index 1, 31, into 50

#python will raise an exxception if we try to index an item that is outside of the list
print(sales[2])


#Python DOES allow us to create lists with multiple different data types include but this is generally a bad practice
sales.append('string')
print(sales)


#Reading lists
#The best way to read a list is the use a loop
real_sales = []

for i in range(1,11):
    prompt = 'Enter the sales for store ' + str(i) + ': '
    real_sales.append(read_float(prompt))

print(real_sales)
#This code gathers prompts the user to input the sales from each of the respective stores.


#Using for loops to display lists
count = 1
for sale in real_sales:
    print('Store number ', count, 'had', sale, 'sales.')
    count = count + 1
#This loops prints out the sales of the given store while iterating the count variable until we reach the end of the real_sales list. 


real_sales.clear() #removes all of the entries in the list


#Placeholder funntions are functions that we know that we wil need but will fill out at a later date.

def future_function():
    '''
    Definition of what the function does
    '''
    pass #this is the placeholder statement. This doesn't actually do anything when python is run.
    
    
    

