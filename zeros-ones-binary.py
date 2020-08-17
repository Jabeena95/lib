# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 09:09:43 2020

@author: Lenovo
"""

#Write a program to count total zeros and ones in a binary number.

def countones(num):
    binary = bin(num)
    setbits = [ones for ones in binary[2: ] if ones=='1']
    
    print(len(setbits))

def countzeros(num):
    binary = bin(num)
    setbits = [zeros for zeros in binary[2:] if zeros=='0']
    print (len(setbits))
     
num = 18
countones(num)
countzeros(num)
