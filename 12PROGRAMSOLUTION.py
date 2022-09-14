# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 19:12:44 2022

@author: NIYATI SHARMA
"""

#Q1.) Write a Python program to Extract Unique values dictionary values?...
test_dict = {"Gfg" : [6, 7, 4, 6],
             "is" : [8, 9, 5],
             "for" : [2, 5, 3, 7],
             "Geeks" : [6, 8, 5, 2]}
 
# printing original dictionary
print("The original dictionary is : " + str(test_dict))
 
# list to memorize elements and insert result
res = []
for sub in test_dict:
    for ele in test_dict[sub]:
         
        # testing for existence
        if ele not in res:
            res.append(ele)
 
# printing result
print("Extracted items : " + str(res))

#Q2.)Write a Python program to find the sum of all items in a dictionary?....
d={'A':100,'B':540,'C':239}
print("Total sum of values in the dictionary:")
print(sum(d.values()))

#Q3.)Write a Python program to Merging two Dictionaries?.....
dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}
print(dict_1 | dict_2)

#Q3) Write a Python program to convert key-values list to flat dictionary?...
from itertools import product

my_dict = {'month_num' : [1, 2, 3, 4, 5, 6], 'name_of_month' : ['Jan', 'Feb', 'March', 'Apr', 'May', 'June']}

print("The dictionary is : ")
print(my_dict)

my_result = dict(zip(my_dict['month_num'], my_dict['name_of_month']))
print("The flattened dictionary is: ")
print(my_result)

#Q4.) Write a Python program to convert key-values list to flat dictionary?.....
from itertools import product
my_dict = {'month_num' : [1, 2, 3, 4, 5, 6], 'name_of_month' : ['Jan', 'Feb', 'March', 'Apr', 'May', 'June']}

print("The dictionary is : ")
print(my_dict)

my_result = dict(zip(my_dict['month_num'], my_dict['name_of_month']))

print("The flattened dictionary is: ")
print(my_result)

#Q5.)Write a Python program to insertion at the beginning in OrderedDict?...
from collections import OrderedDict

my_ordered_dict = OrderedDict([('Will', '1'), ('James', '2'), ('Rob', '4')])
print("The dictionary is :")
print(my_ordered_dict)
my_ordered_dict.update({'Mark':'7'})
my_ordered_dict.move_to_end('Mark', last = False)

print("The resultant dictionary is : ")
print(my_ordered_dict)

#Q6.)Write a Python program to check order of character in string using OrderedDict()?..

from collections import OrderedDict
def check_order(my_input, my_pattern):
   my_dict = OrderedDict.fromkeys(my_input)
   pattern_length = 0
   for key,value in my_dict.items():
      if (key == my_pattern[pattern_length]):
         pattern_length = pattern_length + 1

      if (pattern_length == (len(my_pattern))):
         return 'The order of pattern is correct'

   return 'The order of pattern is incorrect'

my_input = 'Hi Mark'
input_pattern = 'Ma'
print("The string is ")
print(my_input)
print("The input pattern is ")
print(input_pattern)
print(check_order(my_input,input_pattern))



#Q7.)Write a Python program to sort Python Dictionaries by Key or Value?
key_value={}

key_value[5] = 10      
key_value[3] = 8
key_value[6] = 77
key_value[4] = 23
key_value[2] = 9     
key_value[1] = 43
 
print("sorting on the basis of keys")

for i in sorted(key_value) :
    print ((i, key_value[i]), end =" ")