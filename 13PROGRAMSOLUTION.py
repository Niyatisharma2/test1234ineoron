# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 19:54:32 2022

@author: NIYATI SHARMA
"""

#Q1.)Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated
# sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24

import math
c=50
h=30
value = []
items=[x for x in input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print(','.join(value))

#Q2.)Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The
# element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

from __future__ import print_function

user_input = raw_input("Enter values for row and column number: ")
rows, cols = user_input.split(",")
rows = int(rows)
cols = int(cols)

grid = []
for x in range(rows):
    row = []
    for y in range(cols):
        row.append(x * y)
    grid.append(row)
    print(row)

print()
print(grid)


#QUESTION 3.)  
# Write a program that accepts a comma separated sequence of words as input and prints the
# words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

tems=[x for x in input().split(',')]
items.sort()
print(','.join(items))


#Q4.)Write a program that accepts a sequence of whitespace separated words as input and prints

# the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world


while True:
    try:
        num = int(input("Enter a number: "))
        break
    except:
        print("Please Enter a valid number")

fact = 1
result = []

if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,num + 1):
        fact = fact*i
        result.append(fact)
print("Factorial of ",num,"is ",result)
