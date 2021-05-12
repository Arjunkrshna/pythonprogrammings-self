# -*- coding: utf-8 -*-
"""
Created on Thu May  6 14:33:01 2021

@author: ARJUN KRIHA
"""

#python program to find the largest of among the three number
num1 = float(input("enter the first number:"))
num2 = float(input("enter the second number:"))
num3 = float(input("enter the third number:"))
if(num1 > num2) and (num1 > num3):
    largest =num1
elif(num2 > num1) and (num2 > num3):
    largest =num2
else:
    largest=num3
print("the largest number is",largest)    