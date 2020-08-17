# -*- coding: utf-8 -*-
"""
Created on Tue May 26 15:33:03 2020

@author: Lenovo
"""

#write a program to enter marks of five subjects and calculate total,average and percentage?
a = float(input("enter english marks:"))
b = float(input("enter maths marks:"))
c = float(input("enter physics marks"))
d = float(input("enter chemistry marks"))
e = float(input("enter science marks"))
t = a+b+c+d+e
avg = t/5
per=(t/500)*100
print("total=",t ,"average=",avg, "percentage=",per)
