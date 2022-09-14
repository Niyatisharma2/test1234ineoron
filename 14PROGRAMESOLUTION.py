# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 20:20:12 2022

@author: NIYATI SHARMA
"""

#Q1.)Please write a program using generator to print the numbers which can be divisible by 5 and
# 7 between 0 and n in comma separated form while n is input by console.
# Example:
# If the following n is given as input to the program:
# 100
# Then, the output of the program should be:
# 0,35,70


def NumGen(n):
     
    # iterate from 0 to N
    for j in range(1, n+1):
 
        # Short-circuit operator is used
        if j % 5 == 0 or j % 7 == 0:
            yield j
 
# Driver code
if __name__ == "__main__":
       
    # input goes here
    N = 50
 
    # Iterating over generator function
    for j in NumGen(N):
        print(j, end = " ")
        
#Q2.) Please write a program using generator to print the even numbers between 0 and n in comma
# separated form while n is input by console.
# Example:
# If the following n is given as input to the program:
# 10
# Then, the output of the program should be:
# 0,2,4,6,8,10

a = [3, 4, 6, 10, 11, 18]
b = [1, 5, 7, 12, 13, 19, 21]
c = []

#Q3.)The Fibonacci Sequence is computed based on the following formula:
# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n&gt;1
    
#     if a[0] < b[0]:
#         c.append(a.pop(0))
#     else:
#         c.append(b.pop(0))
#         (
# # either a or b could still be non-empty
# print(c + a + b)


# #Q3.)

def f(n):
    if n == 0:
        return 0
    return f(n-1) + 100

n = int(input())
print(f(n))
n = int(input())
f = lambda x: f(x-1)+100 if x > 0 else 0
print(f(n))

#Q4.)Assuming that we have some email addresses in the &quot;username@companyname.com&quot; format,
# please write program to print the user name of a given email address. Both user names and
# company names are composed of letters only.
# Example:
# If the following email address is given as input to the program:
# john@google.com

import re
emailAddress = input()
pat2 = "(\w+)@(\w+)\.(com)"
r2 = re.match(pat2,emailAddress)
print(r2.group(2))


#Q5.)Define a class named Shape and its subclass Square. The Square class has an init function
# which takes a length as argument. Both classes have a area function which can print the area
# of the shape where Shape&#39;s area is 0 by default.

class Shape(object):
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.length = l
    def area(self):
        return self.length*self.length
aSquare= Square(3)
print (aSquare.area())