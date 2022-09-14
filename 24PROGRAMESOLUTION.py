# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 23:21:35 2022

@author: NIYATI SHARMA
"""
#Create a function that takes an integer and returns a list from 1 to the given number, where:
# Python3 Program to Create list
# with integers within given range

def createList(r1, r2):

	# Testing if range r1 and r2
	# are equal
	if (r1 == r2):
		return r1

	else:

		# Create empty list
		res = []

		# loop to append successors to
		# list until r2 is reached.
		while(r1 < r2+1 ):
			
			res.append(r1)
			r1 += 1
		return res
	
# Driver Code
r1, r2 = -1, 1
print(createList(r1, r2))

#Q2.)Create a function that takes a list of numbers and return the number that&#39;s unique.
def unique_list(numbers):
    unique = []
    for item in numbers :
        if item in unique == False:
            unique.append(item)
    return unique   



#3.)Your task is to create a Circle constructor that creates a circle with a radius provided by an
# argument. The circles constructed must have two getters getArea() (PIr^2) and
# getPerimeter() (2PI*r) which give both respective areas and perimeter (circumference).

class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14
    
    def perimeter(self):
        return 2*self.radius*3.14

NewCircle = Circle(8)
print(NewCircle.area())
print(NewCircle.perimeter())

#Q4.)Create a function that takes a list of strings and return a list, sorted from shortest to longest.

# another list Use of sorted()

def Sorting(lst):
	lst2 = sorted(lst, key=len)
	return lst2
	
# Driver code
lst = ["rohan", "amy", "sapna", "muhammad",
	"aakash", "raunak", "chinmoy"]
print(Sorting(lst))
