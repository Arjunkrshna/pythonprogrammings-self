# -*- coding: utf-8 -*-
"""
Created on Thu May  6 15:31:57 2021

@author: ARJUN KRIHA
"""

a=int(input("enter a number"))
print("enter the number",a)
rev=0

while a>0 :
        rem=a%10
        rev=(rev*10)+rem
        a=a//10        
        
        print("reverse number is",rev)