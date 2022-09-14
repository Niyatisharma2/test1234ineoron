# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 21:03:50 2022

@author: NIYATI SHARMA
"""

#Q1.)hCreate a function that takes a list of non-negative integers and strings and return a new list
#without the strings.

def larger_string(str, n):
   result = ""
   for i in range(n):
      result = result + str
   return result

print(larger_string('XYZ', 5))
print(larger_string('.py', 7))

#Q2.)The &quot;Reverser&quot; takes a string as input and returns that string in reverse order, with the
#opposite case.

def reverse(s):
	str = ""
	for i in s:
		str = i + str
	return str

s = "hellogoogle"

print("The original string is : ", end="")
print(s)

print("The reversed string(using loops) is : ", end="")
print(reverse(s))


#Q3.)You can assign variables from lists like this:
# lst = [1, 2, 3, 4, 5, 6]
# first = lst[0]
# middle = lst[1:-1]
# last = lst[-1]
# print(first) ➞ outputs 1
# print(middle) ➞ outputs [2, 3, 4, 5]
# print(last) ➞ outputs 6
# With Python 3, you can assign variables from lists in a much more succinct way. Create
# variables first, middle and last from the given list using destructuring assignment
# (check the Resources tab for some examples), where:
# first ➞ 1
# middle ➞ [2, 3, 4, 5]
# last ➞ 6

def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,3,4,5,6])) 


#Q4.)Write a function that calculates the factorial of a number recursively.
# Examples
# factorial(5) ➞ 120
# factorial(3) ➞ 6
# factorial(1) ➞ 1
# factorial(0) ➞ 1

def factorial(n):
	
	# Checking the number
	# is 1 or 0 then
	# return 1
	# other wise return
	# factorial
	if (n==1 or n==0):
		
		return 1
	
	else:
		
		return (n * factorial(n - 1))

# Driver Code
num =10;
#print("number : ",num)
print("Factorial : ",factorial(num))




#Q5.)Write a function that moves all elements of one type to the end of the list....

# Python3 code to demonstrate working of
# Shift sublist in list
# Using insert() + pop() + loop

# function to perform the task
def shift_sublist(test_list, strt_idx, no_ele, shft_idx):
	for ele in range(no_ele):
		test_list.insert(shft_idx + 1, test_list.pop(strt_idx))
	return test_list

# initializing list
test_list = [4, 5, 6, 7, 3, 8, 10, 1, 12, 15, 16]

# printing original list
print("The original list is : " + str(test_list))

# Using insert() + pop() + loop
# Shift sublist in list
res = shift_sublist(test_list, 2, 3, 6)

# Printing result
print("The list after shift of sublist : " + str(res))
