# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 15:30:44 2024

@author: jayiu
"""

import numpy as np
a = np.array([4, 5, 0, 1, 3, 6, 8, 7, 1, 2, 10, 11])
print(a)
print(type(a))
print(a.shape)
a.sort()
print(a)

b = np.array([-4.3, -2.3, 12.9, 8.99, 10.1, -1.2])
b.sort()
print(b)

c = np.array(['집', '가고', '싶다'])
print(c)
print(c.shape)

print(type(a), type(b), type(c))

dir(a)

help(a.sort)