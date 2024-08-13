# -*- coding: utf-8 -*-
"""
Title: Protecting data attributes against damage

Date: 8-13-2024

Author: Aron James
"""

#By adding an underscore to the beginning of the attribute name we can mark it as internal the the class it's in. This doesn't provide any actual protection for the value. 
#adding 2 undercores however let's us achieve a higher level of security which makes it harder to access from outside the class.

#Let's see how this works by testing it out...
class Secret:
    def __init__(self):
        self._secret = 99
        self.__top_secret = 100

x = Secret()

print(x._secret) #This prints out the 99
print(x.__top_secret) #This pretends that this attribute does not exist
#We can still refer to this attribute while inside the class just not outside it, see below
#THis is accessed in a different way
print(x._Secret__top_secret)
#This underscore convention thus serves as a pretty good security measure but can't stop a very determinded person who knows what's going on.


class Contact:
    
    __min_text_length = 18
    
    @staticmethod #These don't operate within the instance of the class. They are grouped witha class because it might make sense to us.
    def valid_text(text):
        if len(text) < Contact.__min_text_length:
            return False
        else:
            return True

x = 'The length of this text is seven.'
y = 'Length is three.'


print(Contact.valid_text(x)) #This will print True
print(Contact.valid_text(y)) #This will print False


#Next there are properties which let us preserve the simpla access to data attributes held in an object while allowing use to validate the actions performed on the data attribute.
#It's essentially a way of providing security to our attributes within classes.

class People:
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not Contact.validate_text(name):
            raise Exception('Invalid name')
        self.__name = name





