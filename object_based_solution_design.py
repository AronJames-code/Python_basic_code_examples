# -*- coding: utf-8 -*-
"""
Title: Fashion Shop Application

Date: 08-14-2024

Author: Aron James
"""

import pickle
from Read_text_functions import *

print('''Mary's Fashion Shop
      
1. Create new stock item
2. Add stock to existing item
3. Sell stock
4. Stock report
5. Exit  
         
Enter your command:
      ''')

#We would like to create a class to hold each kind of data we wish to store. This is called object-oriented programming.
#Elements in a solution are represented by software objects.

#Creating classes for the for the objects

class Dress_1:
    def __init__(self, stock_ref, price, color, pattern, size):
        self.stock_ref = stock_ref
        self.__price = price
        self.__stock_level = 0
        self.color = color
        self.pattern = pattern
        self.size = size
        
    @property
    def price(self):
        return self.__price

    @property 
    def stock_level(self):
        return self.__stock_level
    

class Pants_1:
    def __init__(self, stock_ref, price, color, pattern, length, waist):
        self.stock_ref = stock_ref
        self.__price = price
        self.__stock_level = 0
        self.color = color
        self.pattern = pattern
        self.length = length
        self.waist = waist
        
    @property
    def price(self):
        return self.__price
    
    @property
    def stock_level(self):
        return self.__stock_level
    

x_1 = Dress_1(stock_ref = 'D0001', price = 100, color = 'red', pattern = 'swirly', size = 12)
y_1 = Pants_1(stock_ref = 'TR12327', price = 50, color = 'black', pattern = 'plain', length = 30, waist = 25)
print(x_1.price)
print(y_1.stock_level)
#Both classes contain properties to provide access to their price and stock_level attributes
#For example if you were to comment out the property statements that are in the classes, it would act as if the attributes don't exist
#Remember that here we could still see them if we typed print(x._Dress__price) and print(y._Pants__stock_level)


#Creating superclasses and subclasses
#This is a mechanism called inheritance which lets us base one class on an existing superclass.
#This would be useful here since our Dress and Pants classes contain many of the same attributes. 
#This is extremely useful for fixing errors as we would have to fix multiple errors if we were to just copy and paste our similar code and
#it would be much easier to implement new attributes since we would only have to do this once for the superclass and it would apply to all of the subclasses. 

#Here is the new superclass
class StockItem(object):
    def __init__(self, stock_ref, price, color, location):
        self.stock_ref = stock_ref
        self.__price = price
        self.color = color
        self.__stock_level = 0
        self.__StockItem_version = 1
        self.location = location
        
    def __str__(self):
        template = '''Stock Reference: {0}
Type: {1}
Price: {2}        
Stock level: {3}
Color: {4}
Location: {5}'''
        return template.format(self.stock_ref, self.item_name, self.price, self.stock_level, self.color, self.location)
    
    def check_version(self):
        #This is version 1 so there's no need to update anything
        pass
        
    max_stock_add = 10
    def add_stock(self, count):
        if (count < 0) | (count > StockItem.max_stock_add):
            raise Exception('Invalid add amount')     
        self.__stock_level = self.__stock_level + count
        
    def sell_stock(self, count):
        if count < 1:
            raise Exception('Invalid number of items to sell.')
        if count > self.__stock_level:
            raise Exception('Not enough stock to sell.')
        self.__stock_level = self.__stock_level - count
    
    @property
    def price(self):
        return self.__price
    
    @property
    def stock_level(self):
        return self.__stock_level
    
    @property
    def item_name(self):
        return 'Stock Item'


    
#Now we will create the dress and pants classes which are subclass of trhe stockitem superclass
class Dress(StockItem):
    def __init__(self, stock_ref, price, color, location, pattern, size):
        super().__init__(stock_ref = stock_ref, price = price, color = color, location = location) #This statment initializes the superclass within the subclass. 
        self.pattern = pattern
        self.size = size
        self.__Dress_version = 1
    
    def __str__(self):
        stock_details = super().__str__()
        template = '''{0}
Pattern: {1}
Size: {2}'''
        return template.format(stock_details, self.pattern, self.size)
    
    def check_version(self):
        #This is version 1 so there's no need to update anything
        super().check_version()
        pass
    
    @property
    def item_name(self):
        return 'Dress'



#Here's a way to specify the name of the class we are working on without returning characters with underscores.
x_test = StockItem(stock_ref = 'D0001', price = 100, color = 'red', location = 'None')
x = Dress(stock_ref = 'D0001', price = 100, color = 'red', pattern = 'swirly', size = 12, location = 'None')
print(x_test.item_name)
print(x.item_name)


#Method overriding in classes, or superceding a method in a superclass with one in the subclass
o = object()
print(o)

class StrTest(object):
    def __str__(self):
        return 'string from StrTest'
    
o = StrTest()
print(o)

#Before the o printed out the object's location but now it has a new method that returns the string: string from StrTest insead.
#Now let's make a new class that extends the superclass

class StrTestSub(object):
    def __str__(self):
        return super().__str__() + '... with sub\n'
    
o = StrTestSub()
print(o)
#Now we can go back and use these methods in the stockitem class and other classes
print(x, '\n')



#Protecting data in a class hierarchy
#The getattr(self, '_location', None) is a function with three arguments. First is a reference to an object, the second is
#is a string containing the name of the attribute for which we want to get the value, and the third is the value to be returned
#if the attribute is not present in the object.
#The hasattr(new_dress, 'location') function take two arguments. The first is a reference to an object and the second is 
#the name of the attribute you're looking for. 

d = Dress(stock_ref = 'D01', price = 100, color = 'red', pattern = 'swirly', size = 12, location = 'Shop Window')
d.add_stock(5)
print(d, '\n')
d.sell_stock(2)
print(d, '\n')

#The main layout of the application:
class FashionShop(object):
    
    
    def __init__(self):
        self.__stock_dictionary = {}
    
    def save(self, filename):
        '''
        Saves the fashion shop item to the give file name
        '''
        with open(filename, 'wb') as out_file:
            pickle.dump(self, out_file)
    
    @staticmethod #This makes the load part of the class rather than part of the object. 
    def load(filename):
        '''
        Loads a fashion shop item from the give file name
        '''
        with open(filename, 'rb') as input_file:
            result = pickle.load(input_file)
            return result
    
    def store_new_stock_item(self, stock_item):
        '''
        Create a new fashion shop item
        The item is indexed on the stock_ref attribute
        '''
        if stock_item.stock_ref in self.__stock_dictionary:
            raise Exception('Item already present.')
        self.__stock_dictionary[stock_item.stock_ref] = stock_item

    def find_stock_item(self, stock_ref):
        '''
        Gets an item from the stock
        Returns None if there is no item for stock reference
        '''
        if stock_ref in self.__stock_dictionary:
            return self.__stock_dictionary[stock_ref]
        else:
            return None
    
    def __str__(self):
        stock = map(str, self.__stock_dictionary.values())
        stock_list = '\n'.join(stock)
        template = '''Items in stock:
{0}
'''
        return template.format(stock_list)
    


shop = FashionShop()
shop.save('FashionShop.pickle')
loaded_shop = FashionShop.load('FashionShop.pickle')

shop.store_new_stock_item(d)

item = shop.find_stock_item('D01')
print(item)

print(shop)


#Create a user interface component

class FashionShopShellApplication:
    def __init__(self, filename):
        '''
    Manages the fashion shop data
    Displays a message if the load fails and creates a new shop
    '''
        FashionShopShellApplication.__filename = filename
        try:
            self.__shop = FashionShop.load(filename)
        except:
            print('Fashion shop not loaded.')
            print('Creating an empty fashion shop...')
            self.__shop = FashionShop()
            
    def main_menu(self):
        prompt = '''Mary's Fashion Shop

1. Create new stock item
2. Add stock to existing item
3. Sell stock
4. Stock report
5. Exit   
        
Enter your command: '''
        
        while(True):
            command = read_int(prompt)
            if command == 1:
                self.create_new_stock_item()
            elif command == 2:
                self.add_stock()
            elif command == 3:
                self.sell_stock()
            elif command == 4:
                self.do_report()
            elif command == 5:
                self.__shop.save(FashionShopShellApplication.__filename)
                print('Shop data saved.')
                break

ui = FashionShopShellApplication('FashionShop.pickle')
ui.main_menu()




