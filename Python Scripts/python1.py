# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 14:50:27 2020

@author: Lenovo
"""

#Write a program to perform input/output of all basic data types
x=3 #x is int
y=4.8 #y is float
z="jabeena" #z is string
a=7j #a is complex
b=["java","python","angular"] #b is list
c=("java","python","angular") #c is tuple
d={"java","python","angular"} #d is set
e=range(5) #e is range
f=bool(2) #f is boolen
print(x,y,z,a,b,c,d,e,f)
print(type(x),type(y),type(z),type(a),type(b),type(c),type(d),type(e),type(f))

#write a program to enter two numbers and their sum
x=4
y=8
z=x-y #used '-' operator
print(z)

#write a program to enter two numbers and perform all arithemetic operations
a=9
b=4

#Addition of numbers
add = a+b

#Subtraction of numbers
sub = a-b
 
#Multiplication of numbers
mul = a*b

#Division(float) of numbers
div1 = a/b

#Division(floor) of numbers
div2 = a//b

#Modulo of both numbers
mod = a%b

#print results
print(add)
print(sub)
print(mul)
print(div1)
print(div2)
print(mod)

#write a program to enter length and breadth of rectangle and find its perimeter
l=float(input("enter length value:"))
b=float(input("enter breath value:"))
p=(2*l)+(2*b) #p is perimeter
print(p)

#write a program to enter length and breadth of rectangle and find its area
l=float(input("enter length value:"))
b=float(input("enter breath value:"))
a=l*b #a is area
print(a)

#write a program to enter radius of circle and find its diameter,circumference,and area
r=float(input("enter radius of the circle:"))
d=2*r #d is diameter
c=2*3.14*r #c is circumference
a=3.14*(r**2) #a is area
print(d)
print(c)
print(a)

#wite a program to length in centimeter and convert into meter and kilometer
cm=float(input("enter value:")) #cm is centimeter
m=cm/100                        #m is meter
km=cm/(1000*100)                #km is kilometer
print(m)
print(km)

#write a program to enter temperature in celcius and convert into fahrenheit
c=float(input("enter temperature in celcius:")) #c is celcius
f=(c*1.8)+32 #f is farenheit
print(f)

#write a program to enter temperature in fahrenheit and convert into celcius
f=float(input("enter temperature in fahrenheit:")) 
c=(f-32)/1.8
print(c)

#write a program to convert days into years, weeks and days
d=float(input("enter no.of days:")) #d is days
y=d/365 #  y is years
w=d/7 #w is weeks
print(y)
print("years=",y,"weeks=",w,"days=",d)

#write a program to find power of any number
x= float(input("enter base number:"))
y=float(input("enter power:"))
z=x**y
print(z)

#write a program to enter any number and calcute its square root
x=float(input("enter number:"))
y=x**0.5
print("squre root of number is",y)

#write a program to enter two angles of triangle and find third angle
a=float(input("enter first angle value:"))
b=float(input("enter second angle value:"))
c=180-(a+b)
print("thrid angle is:",c)

#write a program to enter base and height of atraingle and find its area
h=float(input("enter height value:"))
b=float(input("enter base value:"))
a=(b*h)/2
print("area:",a)

#write a program to calculate area of an equilateral triangle
import maths
x=float(input("enter side value:"))
y=(maths.sqrt(3)/4)*(x**2)
print("area of equilateral triangle:",y)

#write a program to enter marks of five subjects and calculate total,average and percentage
a=float(input("enter social marks:"))
b=float(input("enter physics marks:"))
c=float(input("enter botany marks:"))
d=float(input("enter chemistry marks:"))
e=float(input("enter zoology marks:"))
t=a+b+c+d+e
avg=t/5
per=(t/500)*100
print("total:",t,"average",avg,"percentage%:",per)

#write a program to P,T,R and calculate simple interest
p=float(input("enter principle amount:"))
t=float(input("enter time period:"))
r=float(input("enter rate:"))
SI=(p*t*r)/100 #simple interest=(P*T*R)/100
print("simple interest:",SI)

#write a program to P,T,R and calculate compound interest
p=float(input("enter principle amount:"))
t=float(input("enter time period:"))
r=float(input("enter rate:"))
CI=p*(1+r/100)**t #compound interest=P(1+1/r)^t
print("compound interest:",CI)

