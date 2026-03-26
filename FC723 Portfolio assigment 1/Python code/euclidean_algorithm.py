#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 14:59:35 2026

@author: bu3li
"""

def find_GCD(Num1,Num2): # Function with 2 args, Num1 and Num2 to caluclate the Euclidean algorthim
     # Looping through the code until the Num2 is equal to 0
    while Num2 != 0:
        reminader = Num1 % Num2 # Here is where we calculate the reminader 
        Num1 = Num2  # We switch here from Num1 to Num2
        Num2 = reminader # and here from Num2 to remainder
    return Num1 # Returning GCD 


# Random valued variables
n1 = 12
n2 = 4

code = find_GCD(n1, n2) # Fetching the GCD
print(f"The GCD is >> {code}")  # Displaying the GCD here