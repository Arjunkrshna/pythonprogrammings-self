# -*- coding: utf-8 -*-
"""
Created on Fri May 14 14:06:27 2021

@author: ARJUN KRIHA
"""

# Python program to find the H.C.F of two input number

# define a function
def HCF(x, y):

# choose the smaller number
    if x > y:
        smallNo = y
    else:
        smallNo = x
    for i in range(1, smallNo+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
            
    return hcf

num1 = int(input('enter first Number'))
num2 = int(input('enter first Number'))

result=HCF(num1, num2)

print("The H.C.F. of", num1,"and", num2,"is", result)