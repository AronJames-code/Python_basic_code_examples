# -*- coding: utf-8 -*-
"""
Title: File Reading and Writing

Date: 8-9-2024

Author: Aron James
"""

#Write into a file
output_file = open('test.txt', 'w')
#The first argument in the open function refers to the file name ane the second, 'w' here, refers to what we are going to be doing to the file. In this casing we are writing to the file.
#Exercise caution as it's very easy to overwrite an existing file. The open function will erase the existing file before writing new content to it.

#Once the file is opened we can add lines of text to it
output_file.write('First line\n')
output_file.write('Second line\n')
output_file.close() #This completes any unsatisfied writing and releases the file. 
#Writing is a method because it's created as part of an object.


#Read from a file
input_file = open('test.txt', 'r')
for line in input_file:
    print(line)
#Notice that there is an extra line inbetween our first and second prints. we can get rid of this by using the .strip() method

input_file = open('test.txt', 'r')
for line in input_file:
    line = line.strip()
    print(line)
input_file.close()
#The strip method is useful for making sure that there are no nonprintable characters at the start or end of text that is read in.

input_file.close()
#We also have to close files after they're been read as well.
#note that we can use the 'r+' argument for both reading and writing

input_file = open('test.txt', 'r')
read_file = input_file.read()
print(read_file)
input_file.close()
#This .read method is used to read an entire file at once rather than need to create a loop to do it.


#Doing things with files can result in errors. To deal with this we should note that no files should be left open and 
#the user must be made aware that something has gone wrong.
#Like before we can use the try and except constructions.

try:
    output_file = open('test_2.txt', 'w')
    for i in range(1,11):
        output_file.write('This is line # ' + str(i) + '\n')
    print('File written successfully.')
except:
    print('Something went wrong writing the file.')
finally: #This part will always be obeyed. So here we want the file to close no matter the outcome of the try except functions.
    output_file.close()

input_file = open('test_2.txt', 'r')
total_contents = input_file.read()
print(total_contents)
input_file.close()


#The with construction can also be used to make the program automatically preform the exit behavior on the resource the with construction is managing. 


try:
    with open('test_2.txt', 'w') as output_file:
        for line in output_file:
            output_file.write(str(line) + '\n')
except:
    print('Something went wrong...')

