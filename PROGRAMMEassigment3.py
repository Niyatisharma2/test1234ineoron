# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 14:17:01 2022

@author: NIYATI SHARMA
"""

#Q1>Write a Python Program to Check if a Number is Positive, Negative or Zero?##
n=int(input("enter the number"))
if n>0:
     print("the number is positive")
elif n<0:
     print("print the negative number")
else: 
     print("zero")

#Q2.>Write a Python Program to Check if a Number is Odd or Even?###
n=int(input("enter the numbers"))
if n%2==0:
    print("even")
else:
    print("odd")

#Q3.>Write a Python Program to Check Leap Year?###
l=int(input("enter the value of leapyear"))
result ="leap_year"
if l%400==0:
    print("leap year")
else:
    print("non leap year")
    print(result)
    
    
#Q4.>Write a Python Program to Check Prime Number?####
num = int(input("Enter a number: "))

# If number is greater than 1
if num > 1:
   # Check if factor exist  
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           break
   else:
       print(num,"is a prime number")
       
# Else if the input number is less than or equal to 1
else:
   print(num,"is not a prime number")

#Q5.>Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
lower = 1
upper = 10000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num >=1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
               print(num)