# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 17:05:21 2022

@author: NIYATI SHARMA
"""


#Q1.). In the interactive interpreter, import the zoo module as menagerie and call its hours() function.

import zoo as menagerie
menagerie.hours()


#Q2.) Using the interpreter, explicitly import and call the hours() function from zoo.

import zoo as menagerie
menagerie.hours()

#Q3.)
from zoo import hours as info
info()


#Q4.) Create a plain dictionary with the key-value pairs 'a': 1, 'b': 2, 'c': 3, and print it out.

plain = {'a': 1, 'b': 2, 'c': 3}
print(plain)

#Q5.) Make an OrderedDict called fancy from the same pairs listed in 5 and print it. Did it print in the same order as plain?
from collections import OrderedDict
fancy = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
fancy