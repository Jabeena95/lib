# -*- coding: utf-8 -*-
"""
Created on Tue May 26 14:41:21 2020

@author:jabeena
"""

#write a program to enter temperature in celcius and convert into fahrenheit?
c = float(input("enter temperature in celcius:"))
f = (c*1.8)+ 32
print(f)

#write a program to enter temperature in fahrenheit and convert into celcius?
f = float(input("enter temperature in fahrenheit:"))
c = (f-32)/1.8
print(c)