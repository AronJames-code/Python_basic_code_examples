# -*- coding: utf-8 -*-
"""
Title: Python Sets

Date: 8-15-2024

Author: Aron James
"""

#Sets are similar to lists in that a set is a collection of values
#Unlike a list however, each value in a set in unique

set1 = set()
print(set1)

#Things can be added similar to how things are appended in a list
set1.add(1)
print(set1)

#Trying to add 1 again to the set will leave the set unchanged. 
set1.add(1)
print(set1)

#We can also add multiple items at once 
set2 = {2, 3, 4, 5, 6}
print(set2)

#The difference method will return all of the values in one set that aren't in the argument's set
print(set1.difference(set2))
print(set2.difference(set1))

#The union method returns all of the elements that are contained in both sets
print(set1.union(set2))
#The intersection returns the elements that both sets have in common
print(set1.intersection(set2))

#The isdisjoint method returns True if the two sets have no elements in common
print(set1.isdisjoint(set2))

#The issubset returns True if one set is a subset of the other set
print(set1.issubset(set2))


