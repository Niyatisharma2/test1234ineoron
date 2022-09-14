# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 22:43:12 2022

@author: NIYATI SHARMA
"""

#Q1.) Create a function that takes three parameters where:
#  x is the start of the range (inclusive).
#  y is the end of the range (inclusive).
#  n is the divisor to be checked against.
# Return an ordered list with numbers in the range that are divisible by the third parameter n.
# Return an empty list if there are no numbers that are divisible by n.Create a function that takes three parameters where:
#  x is the start of the range (inclusive).
#  y is the end of the range (inclusive).
#  n is the divisor to be checked against.
# Return an ordered list with numbers in the range that are divisible by the third parameter n.
# Return an empty list if there are no numbers that are divisible by n.


# Utility function to find sum of
# all divisor of number up to 'n'
def divisorSum( n ):
	sum = 0
	
	for i in range(1, n + 1):
		
		# Find all divisors of i
		# and add them
		j = 1
		while j * j <= i:
			if i % j == 0:
				if i / j == j:
					sum += j
				else:
					sum += j + i / j
			j = j + 1
	return int(sum)

# Driver code
n = 4
print( divisorSum(n))
n = 5
print( divisorSum(n))

# #Q2.)Create a function that takes in two lists and returns True if the second list follows the first list
# by one element, and False otherwise. In other words, determine if the second list is the first
# list shifted to the right by 1.
  
def common_data(list1, list2):
     result = False
     for x in list1:
         for y in list2:
             if x == y:
                 result = True
                 return result
print(common_data([1,2,3,4,5], [5,6,7,8,9]))
print(common_data([1,2,3,4,5], [6,7,8,9]))



#Q3.)A group of friends have decided to start a secret society. The name will be the first letter of
# each of their names, sorted in alphabetical order.
# Create a function that takes in a list of names and returns the name of the secret society.


# contain the first character of each word
# of another string.

# Function to find string which has first
# character of each word.
def firstLetterWord(str):

	result = ""

	# Traverse the string.
	v = True
	for i in range(len(str)):
		
		# If it is space, set v as true.
		if (str[i] == ' '):
			v = True

		# Else check if v is true or not.
		# If true, copy character in output
		# string and set v as false.
		elif (str[i] != ' ' and v == True):
			result += (str[i])
			v = False

	return result

# Driver Code
if __name__ == "__main__":
	
	str = "geeks for geeks"
	print(firstLetterWord(str))

#Q4.)An isogram is a word that has no duplicate letters. Create a function that takes a string and
# returns either True or False depending on whether or not it&#39;s an &quot;isogram&quot;.
def check_isogram(str1):
    return len(str1) == len(set(str1.lower()))

print(check_isogram("website"))
print(check_isogram("workr"))
print(check_isogram("Python"))
print(check_isogram("Java"))
