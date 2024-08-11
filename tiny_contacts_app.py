# -*- coding: utf-8 -*-
"""
Title: Tiny Contacts App

Date: 08/11/2024

Author: Aron James
"""

#This application will provide a quick way of storing contact details.

from Read_text_functions import * #This allows us to use the functions from the earlier file

def new_contact_proto(): #Code for creating a contact
    print('Create new contact')
    read_text('Enter the contact name: ')
    read_text('Enter the contact address ')
    read_text('Enter the contact phone ')


def find_contact_proto(): #Code for finding a contact. This is only really one contact and serves to function as a prototype function.
    print('Find contact')
    name = read_text('Enter the contact name: ')
    if name == 'John Test':
        print('Name: John Test')
        print('Address: 123 testdrive, city ST, 12345')
        print('Phone: 555-555-5555')
    else:
        print('This name was not found.')


menu = '''Tiny Contacts #This is our menu prompt

1. New Contact
2. Find Contact
3. Exit Program


Please choose one of the above: '''


while True:
    command = read_int(menu)
    while (command < 1) | (command > 3):
        print('Please choose a number that corresponds to one of the given options....\n')
        command = read_int(menu)
    if command == 1:
        #new_contact_proto()
        new_contact()
    elif command == 2:
        #find_contact_proto()
        find_contact()
    elif command == 3:
        break
    break


#With the prototype being completed we can now work on writing code which will actually read in contact details. 
#Let's start by creating lists that can hold the names, addresses, and phone numbers for the contacts.

names = []
addresses = []
phones = []

#We can now use code very similar to our new_contact_proto

def new_contact(): #Code for creating a contact
    print('Create new contact')
    names.append(read_text('Enter the contact name: '))
    addresses.append(read_text('Enter the contact address '))
    phones.append(read_text('Enter the contact phone '))


def find_contact(): #This will search for a contact based off of just the name
    contact = read_text('Enter the contact name: ')
    contact = contact.strip() #The purpose here is the standardize the text. Remove all whitespaces and make it all lowercase so that we can be confident in comparing our values.
    contact = contact.lower()
    count = 0
    for name in names:
        name = name.strip()
        name = name.lower()
        if name == contact:
            break
        count = count + 1 #If the name is not the same as the requested name then we iterate the count. This will serve as the index spot for when we display the name, address, and phone number later on.
    if count < len(names):
        print('Name: ', names[count])
        print('Address: ', addresses[count])
        print('Phone Number: ', phones[count])
    else:
        print('Could not find the contact...')
        
#We could make this more sophisticated by adding another menu within the find_contact() definition that allows use to search by address or phone number as well but this will do for now.






