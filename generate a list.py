# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 09:24:00 2020

@author: Lenovo
"""

# write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.

def Rand(start, end, num): 
    res = [] 
  
    for j in range(num): 
        res.append(Rand.rand(int(start, end))) 
    if j%2==0:
  
        return res 
num = 5
start = 100
end = 200
print(Rand(start, end, num))
