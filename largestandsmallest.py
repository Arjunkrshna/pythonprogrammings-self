# -*- coding: utf-8 -*-
"""
Created on Thu May  6 14:44:04 2021

@author: ARJUN KRIHA
"""

m1=int(input("enter the first number"))
m2=int(input("enter the second number"))
m3=int(input("enter the third number"))
m4=int(input("enter the fourth number"))
m5=int(input("enter the fifth number"))
large= m1
small=m2
if m2>large:
    large=m2
if m3>large:
    large=m3
if m4>large:
    large=m4
if m5>large:
    large=m5
print("largest no. is=",large)
if m2<small:
    small=m2
if m3<small:
    small=m3
if m4<small:
    small=m4
if m5<small:
    small=m5
print("smallest no. is =",small)