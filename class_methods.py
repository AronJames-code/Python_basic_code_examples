# -*- coding: utf-8 -*-
"""
Title: Use classes to create active objects

Date: 08-13-2024

Author: Aron James
"""

from Read_text_functions import *
from classes import new_contact, find_contact

#Going back to the contacts class we will add an attribute that keeps track of the hours worked
class Contact:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
        self.hours_worked = 0


def add_session_to_contact():
    print('Add session')
    contact = find_contact()
    if contact != None:
        print('Name: ', contact.name)
        print('Previous hours worked: ', contact.hours_worked)
        session_length = read_float('Session Length: ')
        contact.hours_worked = contact.hours_worked + session_length
        print('Updated hours worked: ', contact.hours_worked)
    else:
        print('This name was not found.')
        
new_con = Contact('Aron James', '123 laneroad hw', '1234567890')
contacts = []
contacts.append(new_con)

add_session_to_contact()

#This code my not work right because we need the other files to be imported but im having toruble wince those files containa  lot more
#information that just the functions that I wanted imported.


age = 32
user_age = read_int('Enter your age: ')

if user_age < age:
    print('Good')
else:
    raise Exception('That is a really old.')
        