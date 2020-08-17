# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 15:04:54 2020

@author: Lenovo
"""

"""
Create a variable
"""
x = 5
y ="john"
print(x)
print(y)

x = 5   #x is of type  int
x ="john"  #x is of type string
print(x)

#String variable
x = "John" #Double quotes are the same as single quotes
x = 'John' 
print(x)

#Assign value to multiple variables
x, y, z = "orange", "banana", "mango"
print(x)
print(y)
print(z)


x=y=z = "orange" #we cn assign the values to same variables
print(x)
print(y)
print(z)

#Output variable
x ="awesome"
print("python is " +x )

x = "python is "
y = "awesome"
z = x + y
print(z)

#Global variables
x ="awesome"

def myfunc():
    print("python is " +x)
    
myfunc()


x ="awesome"

def myfunc():
    x = "fantastic"
    print("python is " +x)
    
myfunc()
print("python is " +x)


def myfunc():
    global x
    x = "fantastic"
    
myfunc()
print("python is " +x)














