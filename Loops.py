# -*- coding: utf-8 -*-
"""
Title: Introducing Loops

Date: 07-27-24

Author: Aron James
"""
#This is best practiced by highlighting sections of the code you wish to execute and then hitting F9. F5 will run the entire code which won't work well since the first section of the code is an infinite loop :))))
import time

#The while loop allows a program to repeat statements while a given condition is true

while True:#False:
    print('Looping...')
    time.sleep(1)
#The loop above will go on continuouly forever if our condition is true. 
#we can delete the 'True' and uncomment out the 'False' and then our program will no execute at all.


#Here's a better example to show off this. Highlight this next section and hit F9
# to run rather than F5. 
condition = True
while condition:
    print('Looping...')
    condition = False
print('Done Looping.')
#Since the variable condition is true at the start python initiates the loop.
#during the loop our condition variable is set to false so when python goes back to 
#loop again it skips it this time

#We can also make loops using other conditional statements
i = 0
while (i < 10):
    print(i)
    time.sleep(0.5) #This statements causes the program to pause for 0.5 seconds. It's here to help demonstrate how the program is going back into the same loop multiple times as there are multimple pauses.
    i = i + 1
print('Loop is finished.')
#this starts with our iteration, i, equal to 0. It then adds 1 to i each time the loop is preformed until i gets to 10.
#Once i is 10 our condition for our while loop becomes false and so the loop is skipped.



#Detect invalid number entry using exceptions
#If we want our program to retain control when an exception is raised, we can add error handlers using a Python construction called 'try'.

num_validation = False #Setting it to false in order to initiate the start of the while loop
while num_validation == False:
    try:
        num = input('Please input an integer: ')
        num = int(num)
        num_validation = True #If we get here it means that there was no exception raised by the int(num) function and so we can change the input to true in order to break out of the while loop
    except ValueError: #This is for if the user enters something that isn't an integer, ie, something that causes our int(num) function to fail
        print('Invalid input. Please enter some digits.') #Prompts the user to enter something valid and goes back to the start of the loop.
        
print('You have input the number: ', num)


#We can also include multiple exceptions for just one try function. For example someone could mess up your program by ctrl+C while using it and cause it to crash
#The fix for this is using the 'KeyboardInterrupt' exception. 


num_validation = False #Setting it to false in order to initiate the start of the while loop
while num_validation == False:
    try:
        num = input('Please input an integer: ')
        num = int(num)
        num_validation = True #If we get here it means that there was no exception raised by the int(num) function and so we can change the input to true in order to break out of the while loop
    except ValueError: #This is for if the user enters something that isn't an integer, ie, something that causes our int(num) function to fail
        print('Invalid input. Please enter some digits.') #Prompts the user to enter something valid and goes back to the start of the loop.
    except KeyboardInterrupt: #This is for anyone trying to ctrl+C the program
        print('You think you can stop me??? Try again loser.')
        
print('You have input the number: ', num)



#Breaking out of loops. In the other examples we exited a loop by changing our num_validation variable to true but we can also get out of loops using the 'break' function
while True: #Notice we don't need the num_validation variable anymore, we can just initiate the loop by setting it to true.
    try:
        num = input('Please enter an integer: ')
        num = int(num)
        break #This breaks out of the loop after out int(num) works successfully
    except ValueError: 
        print('Invalid input. Please enter some digits.') 
    except KeyboardInterrupt:
        print('You think you can stop me??? Try again loser.')
        
print('You have input the number: ', num)

#If statements can be useful to identifying when a program needs to break out of a loop



#Returning to the top of a loop with continue
#Using 'continue' in a loop will return the user back to the top of the loop
while True:
    num = input('Please enter an integer: ')
    num = int(num)
    if (num == 11):
        print('Sorry but that number is not allowed') #Maybe 11 corresponds to an item that is unavailable at the moment
        continue #Go back to the start of the loop
    print('You have selected the number: ', num)
    break #Program is finished




#The for loop is used to work through lots of data. 
names = ('Rob', 'Mary', 'David', 'Jenny', 'Chris', 'Timmy')
for name in names:
    print(name) #Here 'names' is our list of data. The 'name' variable takes on each name value and iterates to the next name for the next loop. The loop finishes after the last name
    time.sleep(0.5)

#Perhaps an easier way to understand the for loop:
for i in range(1, 20): #This creates a variable, i, and places it in the start of our defined range, 1-20. Also notice that python won't include the upper part of this range. If we wanted 20, we would need: range(1, 21)
    print(i) #Now we are printing i and then repeating the loop with the next value of i.
    time.sleep(0.5)

#We can write the above for loop as an equivalent while loop:
i = 1
while (i < 20):
    print(i)
    time.sleep(0.5)
    i = i + 1

#breaks work the exact same way in for loops. continues will cause the iterating variable to move onto the next item in the data collection.