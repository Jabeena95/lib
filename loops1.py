# -*- coding: utf-8 -*-
"""
Created on Wed May 20 14:45:15 2020

@author: Lenovo
"""
#break and continue

#break statement inside loop
for val in "string":
    if val == "i":
        break
    print(val)
    
print("the end")

n=5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
    print('loop ended')



n=5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
    print('loop ended')


n = 5
while n > 0:
    n -= 1
    print(n)
else:
    print('loop done')


#use of continue statement inside loops
for val in "string":
    if val == "i":
        continue
    print(val)
    
print("the end")

#used to construct loop
n = 5 
while n > 0:
    n -= 1
    print(n)
    
n = 0
while n > 0:    #0  is already false
    n -= 1
    print(n)
    
#using pop() function
a =["hello",'python' ,'java']
while a:
    print(a.pop(-1))     
     
    

#While loop
x = 1
while x<=5:
    if x == 3:
        x = x+1
        continue
    else:
        print(x)
        x = x+1

#infinite while loop
x = 1
while x< 10:
    print(x)
    x = x + 1
    i=1
    while True:
        if i*3 ==0:
            break
        print(i)
        i= i+1


a = ['hi', 'hello', 'world', 'of' , 'python']
s = 'awesome'

i =0
while i < len(a):
    if a[i] == s:
        break
    i += 1
else:
    print(s, 'not found in list')


a = ['hi', 'hello', 'world', 'of' , 'python']
s = 'awesome'

if s in a:
    print(s, 'found in list.')
else:
    print(s, 'not found in list.')



try:
    print(a.index('awesome'))
except ValueError:
    print(s, 'not found in list')
        
#using while loop and for loop
i = "banglore"    
j = 5
while j< 8:
  for x in i:
      print(j,x)
j = j+1
if x == 'a':
    print(x)
    
    
    
av = 10    
x = int(input("How many candies do u want?"))
i = 1
while i<=x:    
    if i > av:
        print("out of stock")
        break
        print("candy")
    i+=1
    
print("Bye")

num = 1  #loop will repeat itself as long as num < 10 remains true
while num > 10:
    print(num)
    num = num + 3
        
"""
#Nested while loop
#when a while loop is present inside another while loop then it is called nested
while loop   
"""
i = 1
j = 5
while i < 4:
    while j < 8:
        print(i , ",", j)
        j = j + 1
        i = i + 1
    
    
#while loop with else block
num = 10
while num > 6:
    print(num)
    num = num - 1
else:
    print("loop is finished")

#using else statement
counter = 0
while counter < 3:
    print("inside loop")
    counter = counter + 1
else:
    print("inside else")


a = ['foo', 'bar', 'baz']
while True:
    if not a:
        break
    print(a.pop(-1))

#using for loop
programming_languages = ["python", "java","html"]
print('programming_languages')
type(programming_languages )

programming_language = ["python","java", "html"]
for language in programming_language:
    print(programming_language)
    
    
for i in range(10):
    print(i)
    

for i in range(10,20):
    print(i)


for i in range(1,21):
    if i%5==0:       
        continue
    print(i)
         
for i in range(1,21):
    if i%5==0:  #it print only with 5multiples
        print(i)

languages = ["c", "C++", "Python" ]
for x in languages:
    print(x)

edibles = ["cashew", "nuts", "dates","eggs", "jagerry"]
for food in edibles:
    if food == "nuts":
        print("No more nuts please!")
        break
    print("great, delicious " + food)
else:
    print("I am so glad: No nuts!")
print("Finally, I finished stuffing myself")

#
for i in range(5):
    if i == 5:
        break
    else:
        print(i)
else:
     print('here')
      
x =  "function"
dir(x)

x = "list"
dir(x)

x = "tuples"
dir(x)


fruits = ['banana','mango','apple']
for index in range(len(fruits)):
    print('current fruits:', fruits[index])
    print("good bye")

for letter in 'Python':
     print('current letter:', letter)


fruits = ['banana', 'apple', 'mango']
for fruit in fruits:
     print('current fruit:', fruit)
     print("good bye")

for num in range(10 , 20):      #to iterate b\n 10 to 20
    for i  in range(2, num):    #to iterate on th factors of the numbers
        if num % i == 0:  #to determine the first factor
            j = num % i #to calculate the second factor
            print('%d equals %d * %d' % (num,i,j))
            break
        else:
            print(num , 'is a prime number')

#list of integer numbers
number = [1, 2, 3, 4, 6, 11]
sq = 0
for val in number:
    sq = val * val
    print(sq)

for val in range(5):
   print(val)
else:
     print("the loop has completed execution")
 
#Nested for loop
     
for num1 in range(3):
    for num2 in range(10 , 14):
        print(num1,",", num2)

count = 0
while(count < 5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))
#print out 1 , 2,  3, 4
for i in range(1, 10):
     if(i%5 == 0):
         break
     print(i)
else:
     print("this is not printed because for loop is terminated because of break but not due to fail in condition")

           
