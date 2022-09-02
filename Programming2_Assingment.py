# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 13:46:00 2022

#@author: NIYATI SHARMA
"""

#Q1.>Write a Python program to convert kilometers to miles?###
kilometre_1 = float (input ("Please enter the speed of car in Kilometre as a unit: "))  
conversion_ratio_1 = 0.621371  
miles_1 = kilometre_1 * conversion_ratio_1  
print ("The speed value of car in Miles: ", miles_1)  

#Q2.>Write a Python program to convert Celsius to Fahrenheit?####

celsius_1 = float(input("Temperature value in degree Celsius: " ))  
  
# For Converting the temperature to degree Fahrenheit by using the above  
# given formula  
Fahrenheit_1 = (celsius_1 * 1.8) + 32  
    
# print the result  
print('The %.2f degree Celsius is equal to: %.2f Fahrenheit'  
      %(celsius_1, Fahrenheit_1))  
  
print("----OR----")  
celsius_2 = float (input("Temperature value in degree Celsius: " ))  
Fahrenheit_2 = (celsius_2 * 9/5) + 32  
    
# print the result  
print ('The %.2f degree Celsius is equal to: %.2f Fahrenheit'  
      %(celsius_2, Fahrenheit_2))  
  
#Q3.>Write a Python program to display calendar?####
#importing calendar module
import calendar

yy = 2022  # year
mm = 8    # month

# To take month and year input from the user
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))

#Q4.>Write a Python program to solve quadratic equation?###
# import complex math module
import cmath
a = 5
b = 6
c = 8
# calculate the discriminant
d = (b**2) - (4*a*c)
# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print('The solution are {0} and {1}'.format(sol1,sol2))

#Q5.>Write a Python program to swap two variables without temp variable?###
x = 10
y = 7
 
print ("Before swapping: ")
print("Value of x : ", x, " and y : ", y)
 
# code to swap 'x' and 'y'
x, y = y, x
 
print ("After swapping: ")
print("Value of x : ", x, " and y : ", y)