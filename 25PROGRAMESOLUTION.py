# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 23:33:17 2022

@author: NIYATI SHARMA
"""

#Q1.) Create a function that takes three integer arguments (a, b, c) and returns the amount of
#integers which are of equal value.

def sum_three(x, y, z):
    if x == y or y == z or x==z:
        sum = 0
    else:
        sum = x + y + z
    return sum
print(sum_three(2, 1, 2))
print(sum_three(3, 2, 2))
print(sum_three(2, 2, 2))
print(sum_three(1, 2, 3))

#Q2.) Write a function that converts a dictionary into a list of keys-values tuples.
# Python code to convert dictionary into list of tuples

# Initialization of dictionary
dict = { 'Geeks': 10, 'for': 12, 'Geek': 31 }

# Converting into list of tuple
list = [(k, v) for k, v in dict.items()]

# Printing list of tuple
print(list)

#Q3.) Write a function that creates a dictionary with each (key, value) pair being the (lower case,
#upper case) versions of a letter, respectively.


# Character and Value as Words Starting with that Character

# Driver Code

# Declaring String Data
string_input = '''GeeksforGeeks is a Computer Science portal for geeks.
	It contains well written, well thought and well explained
	computer science and programming articles, quizzes etc.'''

# Storing words in the input as a list
words = string_input.split()

# Declaring empty dictionary
dictionary = {}

for word in words:

	# If key is not present in the dictionary then we
	# will add the key and word to the dictionary.
	if (word[0] not in dictionary.keys()):

		# Creating a sublist to store words with same
		# key value and adding it to the list.
		dictionary[word[0]] = []
		dictionary[word[0]].append(word)

	# If key is present then checking for the word
	else:

		# If word is not present in the sublist then
		# adding it to the sublist of the proper key
		# value
		if (word not in dictionary[word[0]]):
			dictionary[word[0]].append(word)

# Printing the dictionary
print(dictionary)

#Q4.)Write a function, that replaces all vowels in a string with a specified vowel.

# Function to Replace each vowel in
# the string with a specified character
def replaceVowelsWithK(test_str, K):

	# string of vowels
	vowels = 'AEIOUaeiou'

	# iterating to check vowels in string
	for ele in vowels:

		# replacing vowel with the specified character
		test_str = test_str.replace(ele, K)

	return test_str



# Driver Code
# input string
input_str = "Geeks for Geeks"

# specified character
K = "#"

# printing input
print("Given String:", input_str)
print("Given Specified Character:", K)

# printing output
print("After replacing vowels with the specified character:",
	replaceVowelsWithK(input_str, K))

