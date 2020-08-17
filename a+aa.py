# -*- coding: utf-8 -*-
"""
Created on Thu May 28 12:29:40 2020

@author: Lenovo
"""

#write a program that computes the values of a+aa+aaa+aaaa with a given digit as value of a.
a = input("enter value:")

n1 = a*1
n2 = a*2
n3 = a*3
n4 = a*4
total = int(n1)+int(n2)+int(n3)+int(n4)
print(total)
