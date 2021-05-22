# -*- coding: utf-8 -*-
"""
Created on Fri May 14 13:05:19 2021

@author: ARJUN KRIHA
"""

dict={1:10,2:20,3:30,4:40}
n=len(dict)
result=1
for i in range(1,n+1):
    result=result*dict[i]

print (result)