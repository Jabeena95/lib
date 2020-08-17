# -*- coding: utf-8 -*-
"""
Created on Thu May 28 13:10:43 2020

@author: Lenovo
"""

'''
Write a program which accepts a sequence of words 
 by whitespace as input to print the words composed of
 digits only
'''
words = input("enter words: ").split(' ')

for i in words:
    if i.isdigit()==True :
        print(i, end=',')











