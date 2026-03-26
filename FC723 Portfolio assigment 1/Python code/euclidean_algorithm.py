#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 14:59:35 2026

@author: bu3li
"""

def Find_gcd(num1,num2): # Function with 2 args, Num1 and Num2 to caluclate the Euclidean algorthim
     # Looping through the code until the Num2 is equal to 0
    while num2 != 0:
        reminader = num1 % num2 # Here is where we calculate the reminader 
        num1 = num2  # We switch here from Num1 to Num2
        num2 = reminader # and here from Num2 to remainder
    return num1 # Returning GCD 



try: # Error handling
    
    # local inputs asked by user for first and second number MAKING them integers
    number_1 = int(input("Enter a first number >> "))
    number_2 = int(input("Enter a second number >> "))

    if number_1 <= 0 or number_2 <= 0: # If statement that detects whether the input is positive or negative
        print("Please enter a positive number !") # If negative prints out this
        exit() # And exists out from here.
except ValueError: # This expects errors especially "ValueError" if the value is not an integer rather a string it would detect it
    print("Please enter a valid number value.") # And then print it out
    exit() # THen exists!
else:
    code = Find_gcd(number_1, number_2) # Fetching the GCD
    print(f"The GCD is >> {code}")  # Displaying the GCD here
    if code == 1:
        print("the numbers are prime numbers")
    else:
        print("the numbers arent prime numbers")