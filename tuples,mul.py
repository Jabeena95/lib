# -*- coding: utf-8 -*-
"""
Created on Tue May 26 15:58:34 2020

@author: Lenovo
"""

#Create a dictionary with following tuples (1,2), (2,3), (3,4).
a = ((1,2), (2,3), (3,4))
print(dict(x,y) for x,y in a)
print(a)

#Create a list with 5 elements, then insert 2020 at index 2.
def  main():
    list = ["what", "where", "when", "who", "which"]
    list.insert(2,2020)
    print(list)
main()

#List1=[1,2,3,4,5,6,7,8,9], reverse the list in single line code
List1=[1,2,3,4,5,6,7,8,9]
print(list(reversed(List1)))


#Create a tuple (1,2,3,4,5,6), then remove element 5 from it.
x = (1,2,3,4,5,6)
print(x)
y = list(x)
print(y)
print(type(y))
y.remove(5)
print(y)

#Write code create a list of even numbers (2 to 20) with list comprehension.
[i for i in range(2,21) if i%2==0]

# Create a list and remove last element from it.
list = ["india", "us", "uae", "china" ]
list.remove("china")
print(list)

#Print all 3 multiples from 1 to 100 using for while loop.
i=1
while i<=100:
    mul=i*3
    print(i, "3=", mul)
    i = i+1
        









