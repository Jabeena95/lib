# -*- coding: utf-8 -*-
"""
Created on Thu May 28 12:51:22 2020

@author: Lenovo
"""

"""
Assuming that we have some email addresses in the "username@companyname.com" format,
 please write program to print the company name of a given email address. 
 Both user names and company names are composed of letters only. 
 Example: If the following email address is given as input to the 
program: john@google.com Then, the output of the program should be: google
"""
email = input("enter your email")
print("email", email)
print("company name",email[email.index('@')+1: -4])
