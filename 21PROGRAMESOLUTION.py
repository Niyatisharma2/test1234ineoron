# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 22:29:21 2022

@author: NIYATI SHARMA
"""

#Q1.)Write a function that takes a list and a number as arguments. Add the number to the end of
# the list, then remove the first element of the list. The function should then return the updated
# list.

myList = ["Bran",11,33,"STRESS",22,33,11]
 
myList.remove(22)
 
print(myList)
 

#Q2.)Create the function that takes a list of dictionaries and returns the sum of people&#39;s budgets...
# the sum of values of dictionary
# with same keys in list of dictionary

import collections, functools, operator

# Initialising list of dictionary
ini_dict = [{'a':6, 'b':12, 'c':90},
			{'a':35, 'b':75},
			{'a':80, 'c':5}]


# printing initial dictionary
print ("initial dictionary", str(ini_dict))

# sum the values with same keys
result = dict(functools.reduce(operator.add,
		map(collections.Counter, ini_dict)))

print("resultant dictionary : ", str(result))

#Q3.)Create a function that takes a string and returns a string with its letters in alphabetical order.

# Program to sort alphabetically the words form a string provided by the user

my_str = "Hello this Is an Example With ALPHABETICAL letters"

# To take input from the user
#my_str = input("Enter a string: ")

# breakdown the string into a list of words
words = [word.lower() for word in my_str.split()]

# sort the list
words.sort()

# display the sorted words

print("The sorted words are:")
for word in words:
   print(word)
   
   
 #Q4.)Write a function that takes a list of elements and returns only the integers.
def runningSum(aList):
    theSum = 0
    for i in aList:
        theSum = theSum + i
    return theSum

