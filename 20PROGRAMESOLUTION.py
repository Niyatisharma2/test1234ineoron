# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 22:14:32 2022

@author: NIYATI SHARMA
"""

#Q1.) Create a function that takes a list of strings and integers, and filters out the list so that it
#returns a list of integers only.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# returns True if number is even
def check_even(number):
    if number % 2 == 0:
          return True  

    return False

# Extract elements from the numbers list for which check_even() returns True
even_numbers_iterator = filter(check_even, numbers)

# converting to list
even_numbers = list(even_numbers_iterator)

print(even_numbers)


#Q2.)Given a list of numbers, create a function which returns the list but with each element&#39;s
# index in the list added to itself. This means you add 0 to the number at index 0, add 1 to the
# number at index 1, etc...

# Creating a List
List = []
print("Blank List: ")
print(List)

# Creating a List of numbers
List = [10, 20, 14]
print("\nList of numbers: ")
print(List)

# Creating a List of strings and accessing
# using index
List = ["Geeks", "For", "Geeks"]
print("\nList Items: ")
print(List[0])
print(List[2])


#Q3.)Create a function that takes the height and radius of a cone as arguments and returns the
#volume of the cone rounded to the nearest hundredth. See the resources tab for the formula.

height=40 
radius=36  
pie=3.14285714286  
volume=pie*(radius*radius)*height/3  
print("volume of the cone="+str(volume))  

#Q4.)Create a function that takes a list of numbers between 1 and 10 (excluding one number) and
#returns the missing number.
# Function to find the missing element
def getMissingNo(arr, n):
	total = (n + 1)*(n + 2)/2
	sum_of_A = sum(arr)
	return total - sum_of_A

# Driver code
if __name__ == '__main__':
	arr = [1, 2, 3, 5]
	N = len(arr)
	
	# Function call
	miss = getMissingNo(arr, N)
	print(miss)
	
