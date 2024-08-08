# -*- coding: utf-8 -*-
"""
Title: Bubble Sort
8-8-24
Date: 

Author: Aron James
"""

#Bubble sort progressively sorts lists one step at a time by comparing adjacent items and swapping items that are in the wrong order.

import time
import random




sales = []
amount = 0
for i in range(1,21):
    amount = random.randint(0,100)
    sales.append(amount)

print(sales)
#The above function creates a list of size 20 of sales with values ranging from 1 - 100


#First let's sort from high to low

def sort_high_low():
    for sale in range(0, len(sales)-1): #This loop will go through every item in the list. The minus one is there to keep us from going outside of the list
        if sales[sale] < sales[sale+1]: #This compares 2 individual values in the list that are next to each other
            temp = sales[sale] #These temporary variables are given to the list values, helps with swapping 
            temp_2 = sales[sale + 1]
            sales[sale] = temp_2
            sales[sale + 1] = temp

sort_high_low()
print(sales)
#The above function does a single pass through the list. This is more obvious when we repeat it a few times. 
#To fix this we just need to add another loop to the outside of our code. 



def sort_high_low_ver2():
    for complete_sort in range(0,len(sales)):
        for sale in range(0, len(sales)-1): #This loop will go through every item in the list. The minus one is there to keep us from going outside of the list
            if sales[sale] < sales[sale+1]: #This compares 2 individual values in the list that are next to each other
                temp = sales[sale] #These temporary variables are given to the list values, helps with swapping 
                temp_2 = sales[sale + 1]
                sales[sale] = temp_2
                sales[sale + 1] = temp

sort_high_low_ver2()
print(sales)
#We can now see that the large values are at the beginning of the list while the small values are at the end. 
#This code can also be made to be more efficient. After the first pass through the list, the smallest number is guaranteed to be at the bottom
#and so our nested for loop can actually be given a smaller range to work through. Here's what that would look like. 
#Additionally we can add a boolean variable to take us out of the loop early if the swaps are done before the outerloop is finished.

def sort_high_low_ver3():
    for complete_sort in range(0,len(sales)):
        for sale in range(0, len(sales)-1-complete_sort): #This loop will go through every item in the list. The minus one is there to keep us from going outside of the list
            done_swap = False
            if sales[sale] < sales[sale+1]: #This compares 2 individual values in the list that are next to each other
                temp = sales[sale] #These temporary variables are given to the list values, helps with swapping 
                temp_2 = sales[sale + 1]
                sales[sale] = temp_2
                sales[sale + 1] = temp
                done_swap = True
        if done_swap == False:
            break
                
sort_high_low_ver3()
print(sales)


