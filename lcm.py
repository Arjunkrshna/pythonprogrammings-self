# -*- coding: utf-8 -*-
"""
Created on Fri May 14 14:34:35 2021

@author: ARJUN KRIHA
"""

# Python Program to find the L.C.M. of two input number

# define a function
def lcm(x, y):
   """This function takes two
   integers and returns the L.C.M."""

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result=lcm(num1, num2)

print("The L.C.M. of", num1,"and", num2,"is", result)