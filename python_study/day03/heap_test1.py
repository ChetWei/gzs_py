# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 09:03:53 2018

@author: Administrator
"""

from heapq import *
from random import shuffle

data = [1,2,3,4,5,6,7,8]



heap=[]

for n in data:
    heappush(heap,n)

print(heap)

#将前两位弹出
for i in range(2):
    heappop(heap)
print(heap)

heappush(heap,5)
print(heap)