# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 20:56:30 2022

@author: NIYATI SHARMA
"""

#Q1.)Question1. Create a function that takes three arguments a, b, c and returns the sum of the
#numbers that are evenly divided by c from the range a, b inclusive.

# Function to find the sum of numbers
# divisible by M in the given range
def sumDivisibles(A, B, M):

	# Variable to store the sum
	sum = 0

	# Running a loop from A to B and check
	# if a number is divisible by i.
	for i in range(A, B + 1):

		# If the number is divisible,
		# then add it to sum
		if (i % M == 0):
			sum += i

	# Return the sum
	return sum

# Driver code
if __name__=="__main__":
	
	# A and B define the range
	# M is the dividend
	A = 6
	B = 15
	M = 3

	# Printing the result
	print(sumDivisibles(A, B, M))
    
#Q2.)Create a function that returns True if a given inequality expression is correct and
#False otherwise.....
# definition  

# inequality function 

def check(s):

    regex=eval(s)

    if regex:

        return True

    else:

        return False 

# printing result 

print(check("2 < 7 < 15"))

print(check("30 > 45 > 21 > 9"))

print(check("4 < 7 < 8< 12 > 2"))


#Q3.)Create a function that replaces all the vowels in a string with a specified character.....
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
input_str = "THIS IS STRING"

# specified character
K = "#"

# printing input
print("Given String:", input_str)
print("Given Specified Character:", K)

# printing output
print("After replacing vowels with the specified character:",
	replaceVowelsWithK(input_str, K))

#Q4.)Write a function that calculates the factorial of a number recursively.....?

# Function to find factorial of given number
def factorial(n):
	
	if n == 0:
		return 1
	
	return n * factorial(n-1)

# Driver Code
num = 5;
print("Factorial of", num, "is",
factorial(num))


	
