# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 22:06:59 2022

@author: NIYATI SHARMA
"""

# Q1.)  Make a class called Thing with no contents and print it. Then, create an object called example
# from this class and also print it. Are the printed values the same or different?.....................
# Python program to demonstrate
# object printing


# Defining a class
class Test:
	def __init__(self, a, b):
		self.a = a
		self.b = b
	
	def __repr__(self):
		return "Test a:% s b:% s" % (self.a, self.b)
	
	def __str__(self):
		return "From str method of Test: a is % s, " \
			"b is % s" % (self.a, self.b)

# Driver Code		
t = Test(1234, 5678)

# This calls __str__()
print(t)

# This calls __repr__()
print([t])

#Q2.)  Create a new class called Thing2 and add the value &#39;abc&#39; to the letters class attribute. Letters
#should be printed.
class Thing2:
    letters = 'abc'
print(Thing2.letters)





#3. Make yet another class called, ofMake a dictionary with these keys and values: &#39;name&#39;: &#39;Hydrogen&#39;, &#39;symbol&#39;: &#39;H&#39;, &#39;number&#39;: 1. Then,
#create an object called hydrogen from class Element using this dictionary. course, Thing3. This time, assign the value &#39;xyz&#39; to an instance
#(object) attribute called letters. Print letters. Do you need to make an object from the class to do this?...........
class Thing3:
    def __init__(self):
        self.letters = 'xyz'
        
#Q4) Create an Element class with the instance attributes name, symbol, and number. Create a class
#object with the values &#39;Hydrogen,&#39; &#39;H,&#39; and 1.........

class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
hydrogen = Element('Hydrogen', 'H', 1)

#Q5.) Make a dictionary with these keys and values: 'name': 'Hydrogen', 'symbol': 'H', 'number': 1. Then, create an object called hydrogen from class Element using this dictionary.
#Starting with the dictionary:
el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
#Creating object called hydrogen from class Element using el_dict
hydrogen = Element(el_dict['name'], el_dict['symbol'], el_dict['number'])
hydrogen.name
hydrogen = Element(**el_dict)
hydrogen.name
