# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 21:28:56 2022

@author: NIYATI SHARMA
"""

#Q1.)Create a function that takes a string and returns a string in which each character is repeated
#once.
# Python program to find the first
# repeated character in a string

def firstRepeatedChar(str):

	h = {} # Create empty hash

	# Traverse each characters in string
	# in lower case order
	for ch in str:

		# If character is already present
		# in hash, return char
		if ch in h:
			return ch;

		# Add ch to hash
		else:
			h[ch] = 0

	return ''


# Driver code
print(firstRepeatedChar("workisworkship"))



#Q2.)Create a function that reverses a boolean value and returns the string &quot;boolean expected&quot;
#if another variable type is given.

def fuctionName(int, bool):
    if int in range(...):
        if bool == True:
            return False
        else:
            return True


#Q3.)Create a function that returns the thickness (in meters) of a piece of paper after folding it n
#number of times. The paper starts off with a thickness of 0.5mm.

def num_layers(a):
    Sum = 0
    for i in range(-1, 100):
        for k in range(1, a+1):
            Sum += 2**i
            if k == a+1:
                break
    return (Sum)/1000

#Q4.) Create a function that takes a single string as argument and returns an ordered list containing
#the indices of all capital letters in the string.
 
# initializing string
test_str = 'MyNameiS'

# printing original string
print("The original string is : " + str(test_str))

# Uppercase check using isupper()
res = [idx for idx in range(len(test_str)) if test_str[idx].isupper()]

# printing result
print("Uppercase elements indices : " + str(res))
