# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 23:04:42 2022

@author: NIYATI SHARMA
"""

#Q1.)Write a Python program to find sum of elements in list?...
SUM = 0
 
# creating a list
list1 = [2,5,6,2,15,145]
 
# Iterate each element in list
# and add them in variable total
for ele in range(0, len(list1)):
    SUM = SUM + list1[ele]
 
# printing total value
print("Sum of all elements in given list: ", SUM)

#Q2.)Write a Python program to Multiply all numbers in the list?..
MUL=1
list =[5,6,23,2]
for i in range(0,len(list)):
    MUL =MUL*list[i]
print("multiplication of list ", MUL)


#Q3.)Write a Python program to find smallest number in a list?

List=[5,23,36,3,6]
List.sort()
print("the smallest number is " , List[0])


#Q.)4. Write a Python program to find largest number in a list?
List1=[2,25,36,658,23]
print("the largest number is  ", max(List1))

#Q5.)Write a Python program to find second largest number in a list?...
List2=[25,35,69,23]
List2.sort()
print("the second largest number is ", List2[-2])

#Q6.)Write a Python program to find N largest elements from a list?....
l = [1000,298,3579,100,200,-45,90]
n = 4

l.sort()
print(l[-n:])




