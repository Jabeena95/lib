# -*- coding: utf-8 -*-
"""
Created on Tue May 26 15:43:04 2020

@author: Lenovo
"""

#write a program to P,T,R and calculate simple interest?
p = float(input("enter principle amount:"))  #p is principle amount
t = float(input("enter time period"))   #t is timeperiod
r = float(input("enter rate"))          #r is rate
SI = (p*t*r)/100  #simple interest
print(SI)


#write a program to P,T,R and calculate compound interest
p = float(input("enter principle amount:"))
t = float(input("enter time period:"))
r = float(input("enter rate:"))
CI = p*(1+r/100)**t   #compound interest=p(1+1/r)^t
print(CI)