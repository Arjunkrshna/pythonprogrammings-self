# -*- coding: utf-8 -*-
"""
Created on Thu May 13 18:34:31 2021

@author: ARJUN KRIHA
"""

def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('google.com')) 