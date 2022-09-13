# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 22:33:22 2022

@author: NIYATI SHARMA
"""

#Q1.) Write a Python program to check if the given number is a Disarium Number?....

def calculateLength(n):    
    length = 0;    
    while(n != 0):    
        length = length + 1;    
        n = n//10;    
    return length;    
     
num = 175;    
rem = sum = 0;    
len = calculateLength(num);   
n = num;     
while(num > 0):    
    rem = num%10;    
    sum = sum + int(rem**len);    
    num = num//10;    
    len = len - 1;    
     
#Checks whether the sum is equal to the number itself    
if(sum == n):    
    print(str(n) + " is a disarium number");    
else:    
    print(str(n) + " is not a disarium number");    


#Q2.) Write a Python program to print all disarium numbers between 1 to 100?....
def calculateLength(n):    
    length = 0;    
    while(n != 0):    
        length = length + 1;    
        n = n//10;    
    return length;    
     
#sumOfDigits() will calculates the sum of digits powered with their respective position    
def sumOfDigits(num):    
    rem = sum = 0;    
    len = calculateLength(num);    
        
    while(num > 0):    
        rem = num%10;    
        sum = sum + (rem**len);    
        num = num//10;    
        len = len - 1;    
    return sum;    
      
result = 0;    
     
#Displays all disarium numbers between 1 and 100    
print("Disarium numbers between 1 and 100 are");    
for i in range(1, 101):    
    result = sumOfDigits(i);    
        
    if(result == i):    
        print(i)
        
  #Q3.)Write a Python program to check if the given number is Happy Number?
def isHappyNumber(n):
    st=set()
    while (1):
        n = numSquareSum(n)
        if (n == 1):
            return True
        if n not in st:
            return False
        st.insert(n)
        
#Q4.)Write a Python program to print all happy numbers between 1 and 100?...
def isHappyNumber(num):    
    rem = sum = 0;    
        
    #Calculates the sum of squares of digits    
    while(num > 0):    
        rem = num%10;    
        sum = sum + (rem*rem);    
        num = num//10;    
    return sum;    
            
#Displays all happy numbers between 1 and 100    
print("List of happy numbers between 1 and 100: ");    
for i in range(1, 101):    
    result = i;    
        
    #Happy number always ends with 1 and     
    #unhappy number ends in a cycle of repeating numbers which contains 4    
    while(result != 1 and result != 4):    
        result = isHappyNumber(result);    
        
    if(result == 1):    
        print(i)    
        print(" ")
        
#Q5.)Write a Python program to print all pronic numbers between 1 and 100?...
def isPronicNumber(num):    
    flag = False;    
        
    for j in range(1, num+1):    
        #Checks for pronic number by multiplying consecutive numbers    
        if((j*(j+1)) == num):    
            flag = True;    
            break;    
    return flag;    
     
#Displays pronic numbers between 1 and 100    
print("Pronic numbers between 1 and 100: ");    
for i in range(1, 101):    
    if(isPronicNumber(i)):    
        print(i)   
        print(" ")   

