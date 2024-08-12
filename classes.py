# -*- coding: utf-8 -*-
"""
Title: Creating a class

Date: 08/11/2024

Author: Aron James
"""
from Read_text_functions import *
import pickle


#A class can serve as a kind of container that holds various data that we want it to hold. 
class Contact:
    pass

x = Contact() #This creates an instance of a class. We can now add attributes to it

x.name = 'Aron James'

#We can update our code from the tiny contacts app from earlier but using classes this time

contacts = []
def new_contact():
    print('Create a new contact.')
    new_con = Contact() #Creating an instance of a class, Contacts
    new_con.name = read_text('Enter the contact name: ') #This reads in all of the attributes of our instance
    new_con.address = read_text('Enter the contact address: ')
    new_con.phone = read_text('Enter the contact phone number: ')
    contacts.append(new_con) #This adds to our list of contacts
    

def find_contact():
    print('Find a contact')
    search = read_text('Enter the contact name: ') #User enters the name to be searched
    search = search.strip()#These eliminate the white spaces and make everything lower case so that the search is easier
    search = search.lower()
    result = None #Setting our result to none. if we don't end up getting a result then this will trigger the else statement at the end.
    for contact in contacts: #Searches through our list of contacts
        name = contact.name #Our contact is a class so we are going to compare the name attribute of the class
        name = name.strip()
        name = name.lower()
        
        if name.startswith(search) | name.endswith(search): #Compares if either name we end up with matches
            result = contact #we have a match so we set our result to our contact (class)
            break
    if result != None: #This conditional ensures that result is anything except the None value to proceed
        print('Name: ', result.name)
        print('Address: ', result.address)
        print('Phone: ', result.phone)
    else: #our result never got changed if we reach here so we end the function.
        print('Cound not find the contact.')


#Note that there are many other things that can be done in order to make this application better
#Perhaps we want to implement an additional function that allows us to edit information about a contact.
#Or we should probably address certain issues that may arise such as how our program doesn't address having duplicate names.
        
#Note that if we wanted to pull a name from our contacts class we would index and then apply the .name convention, ie, contacts[0].name
new_contact()
print(contacts[0].name)
print(contacts[0].address)
print(contacts[0].phone)

#Everything in python is actually an object. 
age_int = 25
print(type(age_int))
age_string = 'Twenty-five'
print(type(age_string))


#Python has a method of storing large data structures called pickling.
output_file = open('contacts.pickle', 'wb') #Method for opeing a pickle file (wb means write binary)
output_file.close()
def save_contacts(file_name): #Saves new contact data to the file.
    
    print('Save contacts')
    with open(file_name, 'wb') as out_file:
        pickle.dump(contacts, out_file)

#We can also load data from a pickled file
def load_contacts(file_name):
    global contacts
    print('Load Contacts')
    with open(file_name, 'rb') as input_file: #rb means read binary
        contacts = pickle.load(input_file)
        


##The python initializer method, used to create a class and initialize it at the same time

class InitPrint:
    def __init__(self):
        print('You made an InitPrint instance')

x = InitPrint()
#When the above code is run, we see that the statement telling us that we made an InitPrint instance appears right when we set x equal to the class, or it initializes in other words.

#We can also add arguments to this. This is best understood by testing down below 
class InitName:
    def __init__(self, new_name):
        self.name = new_name


name_test = InitName('Trump') #This initializes a class containing an attribute of name which in the class we had set equal to the argument, in this case, Trump
print(name_test.name)

#We can extend this examples to creating lists similar to how we did earlier:
name_list = []
name_list.append(InitName('Harry'))
name_list.append(InitName('Donald'))
name_list.append(InitName('Jackson'))
print(name_list[0].name)
print(name_list[1].name)
print(name_list[2].name)
#This is the greatest way of making sure that an object is only ever created with an appropriate set of attributes
#This would be a great way of re-creating our tiny contacts application from earlier



