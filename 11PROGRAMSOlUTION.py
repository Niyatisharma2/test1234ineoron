# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 23:31:45 2022

@author: NIYATI SHARMA
"""

#Q1.)Write a Python program to find words which are greater than given length k?..
def word_k(k, s):    
    # split the string where space comes
    word = s.split(" ")
    # iterate the loop for every word
    for x in word:
        # if length of current word
        if len(x)>k:
          # greater than k then
          print(x)
k = 3
s ="WELCOME BEST"
word_k(k, s)
#Q2.)Write a Python program for removing i-th character from a string?...

# Removes character at index i
def remove(string, i):

	# Characters before the i-th indexed
	# is stored in a variable a
	a = string[ : i]
	
	# Characters after the nth indexed
	# is stored in a variable b
	b = string[i + 1: ]
	
	# Returning string after removing
	# nth indexed character.
	return a + b
	
# Driver Code
if __name__ == '__main__':
	
	string = "geeksFORgeeks"
	
	# Remove nth index element
	i = 5
	
	# Print the new string
	print(remove(string, i))
    
#Q3.)Write a Python program to split and join a string?
str1=input("Enter first String with space :: ")
print(str1.split())    #splits at space

str2=input("Enter second String with (,) :: ")
print(str2.split(','))    #splits at ','

str3=input("Enter third String with (:) :: ")
print(str3.split(':'))    #splits at ':'

str4=input("Enter fourth String with (;) :: ")
print(str4.split(';'))    #splits at ';'

str5=input("Enter fifth String without space :: ")
print([str5[i:i+2]for i in range(0,len(str5),2)])    #splits at position 2

#Q4.)Write a Python to check if a given string is binary string or not?...
stringA = '0110101010101'
b = {'0','1'}
t = set(stringA)

if b == t or t == {'0'} or t == {'1'}:
        print("StringA is a binary string.")
else:
            print("StringA is not a binary string.")

stringB = '0120101010111'
u = set(stringB)

if b == u or u == {'0'} or u == {'1'}:
        print("StringB is a binary string.")
else:
        print("StringB is not a binary string.")

