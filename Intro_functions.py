# -*- coding: utf-8 -*-
"""
Re_introduction to Python

@author: Aron James

Date: 07-24-2024
"""
#The random library pretty self explanatory
import random
#This can get the date and time from the PC's clock and also contains the sleep function
import time
#Add text, images and sound to programs
import snaps


#The Ord Function gives the value that represents the given character

print(ord('2'))

#The chr Function does essentially the opposite of ord

print(chr(50))

#The bin Function takes a number and returns a string of bits that represents the value of that number

print(bin(255))

#Note that the 0b prefix just represents the type of number it is, ie, it's binary. The actual number follows

#Using the random library to create a die throw
Die_1 = random.randint(1,6)
print('You have rolled a', Die_1)


#The sleep function gives the user the impression that the computer is 'thinking' about the problem.
#Gives the user time to read what the program displays
Coin_1 = random.randint(1,2)
print('Flipping the coin Please stand by...')
time.sleep(3)
print('You got a', Coin_1)



