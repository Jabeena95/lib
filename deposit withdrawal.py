# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 08:53:11 2020

@author: Lenovo
"""

'''  Write a program that computes the net amount 
of a bank account based a transaction log from console
 input. The transaction log format is shown as
 following: D 100 W 200 D means deposit while W means
 withdrawal. Suppose the following input is supplied
 to the program: D 300 D 300 W 200 D 100 Then, the
 output should be: 500  '''
lst = input("enter trnsactions:").split(" ")
print(lst)
 
deposit=[]
wdw=[]
 
for i in range(len(lst)):
    if lst[i]== 'D':
        deposit.append(int(lst[i+1]))
    elif lst[i]== 'w':
        wdw.append(int(lst[i+1]))
    else:
        pass
print("deposit :", deposit)
print("withdrawal :", wdw)

total_deposit= sum(deposit)
print("total deposit :", total_deposit)

total_wdw= sum(wdw)
print("total withdrawal :", total_wdw)
    
net_amount = total_deposit - total_wdw
print("net amount Rs: ", net_amount )


