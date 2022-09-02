# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 21:43:04 2022

@author: NIYATI SHARMA
"""

#Q1.>Write a Python Program to Display Fibonacci Sequence Using Recursion?##
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))
       
#   Q2.>Write a Python Program to Find Factorial of Number Using Recursion?###
def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num = 7

# check if the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))
   
#Q3.>Write a Python Program to calculate your Body Mass Index?
weight=float(input("Enter the weight of person in KG : "))
height=float(input("Enter the height of person in meter : "))
bmi=weight/(height*height)
print("BMI of person is : ",bmi)

#Q4.>Write a Python Program to calculate the natural logarithm of any number?###
import math
print ("math.log(100.12) : ", math.log(100.12))
print ("math.log(100.72) : ", math.log(100.72))
print ("math.log(math.pi) : ", math.log(math.pi))

#Q5.>Write a Python Program for cube sum of first n natural numbers?##
n=5
s=0
# iterating loop up to given number n
for i in range(1,n+1):
    # adding cube sum using pow() function
    s=s+pow(i,3)
print(s)  
