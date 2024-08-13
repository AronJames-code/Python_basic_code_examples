# -*- coding: utf-8 -*-
"""
Title: Creating a session class

Date: 8-13-2024

Author: Aron James
"""
import time

#This is code to create a class that describes the time at which a session of something took place
class Session:
    
    __min_session_length = 0.5
    __max_session_length = 3.5
    
    
    @staticmethod
    def validate_session_length(session_length):
        if (session_length < Session.__min_session_length) | (session_length > Session.__max_session_length):
            return False
        else:
            return True
    
    def __init__(self, session_length):
        if Session.validate_session_length(session_length) == False:
            raise Exception('Invalid session length.')
        else:
            self.__session_length = session_length
            self.__session_end_time = time.localtime()
            self.__version = 1
            
    #****        
    @property
    def session_length(self):
        return self.__session_length

    @property 
    def session_end_time(self):
        return self.__session_end_time
        
    def __str__(self):
        template = 'Date {0} Length: {1}'
        date_string = time.asctime(self.__session_end_time)
        return template.format(date_string, self.__session_length)

current_session = 2
session_record = Session(current_session)

#Remember the strange printing convention for the double underscore class attributes
print(session_record._Session__session_length)
print(time.asctime(session_record._Session__session_end_time)) #The time.asctime makes the time that's returned much more readable.
        
#We can also add properties to obtain these values more easily. We did this starting at #****
print(session_record)



#The python map function
#This function is like the str function where it converts the the applied object into the string version of the object
#but the map function does this for all of the elements in a list. 
code = ['Line1', 'Line2', 'Line3']
print(code)
#Now we will create a function that will indent a string for us. An indent can be created using 4 spaces
def indent(x):
    return '    ' + x
print(indent('Aron'))
#We would like to apply this new function to every string in our code variable. 
#We could use a for loop but we will use map this time
indented_code = map(indent, code)
print(indented_code) #This returns interation code

for i in indented_code:
    print(i)
#Here map maps the function indent to the lines of code.


#THe join function
#Used to join items in a list with a separator inbetween them all
words = ['Hello', 'World', 'this', 'is', 'Python']
separator = ' '

sentence = separator.join(words)
print(sentence)

#We can use other separators too such as commas
words_2 = ['apple', 'banana', 'cherry']
separator = ','

fruits = separator.join(words_2)
print(fruits)

#The separator can even be blank such as to join characters in a word
chars = ['p', 'y', 't', 'h', 'o', 'n']
separator = ''

word = separator.join(chars)
print(word)




