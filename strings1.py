# -*- coding: utf-8 -*-
"""
Created on Sun May 10 11:17:06 2020

@author: Lenovo
"""

#strings

a = "Hello, World!"
print(a[1])

#slicing
b = "Hello, World!"
print(b[2:5])

#Negitive indexing
b = "Hello, World!"
print(b[-5:-2])

#string length
a = "Hello, India!"
print(len(a))

#string methods: python has set of built-in methods that u can use on strings
#strip() method removes any whitespace from the beginning or the end
a = "hello, friends!"
print(a.strip())

#lower() method returns the string in lower case
a = "Hello, India!"
print(a.lower())  #the output in small letters

#upper() method returns the string in upper case
a = "Hello, World!"
print(a.upper())   #the output will be capital letters

#replace()  method  replaces a string with another string
a = "Hello, World"
print(a.replace("H", "J"))

#split() method splits the string into substrings if it find instsnces of the
#separator
a = "Hello, World!"
print(a.split(","))

#check string: to check if a certain pharse or character is present in a string,
#we can use this keywords in or not in
txt = "the rain in spain stays mainly in the plain"
x = "ain" in txt    #pharse 'ain' is present 
print(x)

txt = "the rain in spain stays mainly in the plain"
x = "ain" not in txt
print(x)

#String Cocatenation(+)
a = "Hello "
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b    #to add space between a and b
print(c)

#String format
#As we learned in variable we cannot combine strings and numbers
age = 24
txt = "My name is jabeena, I am" + age
print(txt)

#by using format() method we can add strings and numbers
#format() method takes the passes arguments, formats them, and place them in a
#string where the placeholder{} are
age = 24
txt = "My name is Jabeena, and  I am {}"
print(txt.format(age))

#format method takes unlimited arguments, and are placed into the respective placeholderrs
quantity = 3
itemno = 568
price = 49.95
myorder ="I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#index numbers{0}
quantity = 3
itemno = 568
price = 49.95
myorder ="I want {2} dollars  for {0} pieces of item {1}"
print(myorder.format(quantity, itemno, price))

x = "india"
print(x)

x = 'india'
print(x)
type(x)






