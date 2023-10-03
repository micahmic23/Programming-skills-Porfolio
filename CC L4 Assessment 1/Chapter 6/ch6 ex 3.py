#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 20:22:41 2023

@author: geronimojo

Exercise 3: Infinity ☑️
Write a loop that never ends, and run it. (To end the loop, press ctrl-C or close the window displaying the output.)
"""
#While loop is used to repeatedly run the program asking the user's age to check ticket amount.
while True:
    age=input("How old are you?")
    
    age=int(age)
    
    if age<3:
       print("The ticket is free.")
    elif age>=3 and age<=12:
        print("The ticket is $10.")
    else:
        print("The ticket is $15.")