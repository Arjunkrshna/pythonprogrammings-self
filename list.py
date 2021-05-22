# -*- coding: utf-8 -*-
"""
Created on Fri May 14 11:40:27 2021

@author: ARJUN KRIHA
"""

a = [1,1,2,3,5,4,2,1,67,89,954,34,21]
b = [1, 2, 3, 4, 33, 21, 44, 21, 34, 570, 32, 1001, 1050, 231, 12]
#b = [1,1,2,3,5,4,2,1,67,89,954,34,21]
#a = [1, 2, 3, 4, 33, 21, 44, 21, 34, 570, 32, 1001, 1050, 231, 12]

c=[]
n1=len(a)
n2=len(b)

if n1<n2:
    print ('a')
    for i in range(n1):
        if a[i] in b:
            if a[i] not in c:
                c.append(a[i])
                
else:
    print ('b')
    for i in range(n2):
        if b[i] in a:
            if b[i] not in c:
                c.append(b[i])


print (c)