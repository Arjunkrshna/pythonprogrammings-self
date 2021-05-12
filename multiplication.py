# -*- coding: utf-8 -*-
"""
Created on Thu May  6 15:09:04 2021

@author: ARJUN KRIHA
"""

#factorial of a number
num=int(input("enter the no."))
#user number
fact=1
for i in range(1,num+1):
    fact=fact*i
    print("factorial of",num,"is",fact)
    