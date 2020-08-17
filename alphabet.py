# -*- coding: utf-8 -*-
"""
Created on Thu May 28 13:01:17 2020

@author: Lenovo
"""
'''
Write a program that accepts a comma separated sequence 
of words as input and prints the words in a comma-separated
 sequence after sorting them alphabetically.  Suppose the 
 following input is supplied to the program:
     without,hello,bag,world Then, the output should be: 
         bag,hello,without,world'
 '''
 
txt = input("Enter words: ").split(',')
print(txt)

txt.sort()   #alphabetical order

print(txt)

for i in txt:
    print(i, end= ',')






