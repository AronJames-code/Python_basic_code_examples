# -*- coding: utf-8 -*-
"""
Title: Investtgating Properties

Date: 8-13-2024

Author: Aron James
"""

#This aims to play around with properties so that we may understand them better

class Prop:
    @property
    def x(self):
        print('property x get')
        return self.__x
    @x.setter 
    def x(self, x):
        print('property x set:', x)
        self.__x = x
    
test = Prop()
test.x = 99
print(test.x)

test.x = test.x + 1


#Incorporating properties into the contacts application:
    
class Contact:
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
        
    @property
    def address(self):
        return self.__address
    
    @address.setter
    def address(self, address):
        self.__address = address
    
    
    
#String formatting:

name = 'Aron James'
age = 25

template = 'My name is {0} and my age is {1}'
print(template.format(name, age))
#In the code above the {0} and {1} were replaced with the variables name and age. 

#A useful convention for printing things in columns:
template_2 = 'My name is {0:20} and my age is {1:10}'
print(template_2.format(name, age))


