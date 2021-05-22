# -*- coding: utf-8 -*-
"""
Created on Thu May 13 19:00:16 2021

@author: ARJUN KRIHA
"""

from datetime import datetime
now = datetime.now()
print (now)

mytime = now.strftime("%d-%m-%y")

date = now.strftime("%d=%a=%b=%Y")
print (mytime)
print (date)