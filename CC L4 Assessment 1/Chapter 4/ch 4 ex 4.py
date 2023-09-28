#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 12:18:34 2023

@author: geronimojo

Chapter 4 Exercise 4: Stages of Life ☑️
Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:

•If the person is less than 2 years old, print a message that the person is a baby.

•If the person is at least 2 years old but less than 4, print a message that the person is a toddler.

•If the person is at least 4 years old but less than 13, print a message that the person is a kid.

•If the person is at least 13 years old but less than 20, print a message that the person is a teenager.

•If the person is at least 20 years old but less than 65, print a message that the person is an adult.

•If the person is age 65 or older, print a message that the person is an elder.

"""
age=17 #17 in assigned to the variable 'age'

if age<2:  #if statement used to check if age is less than 2 to print as baby.
    print("You are a baby")
    
elif age<4: #elif used to check if age is less then 4 to print as toddler.
    print("You are a toddler")
    
elif age<13: #elif used to check if age less than 13 to be printed as kid.
    print("You are a kid")
    
elif age<20: #elif used to check if age less than 20 to be printed as teenager.
    print("You are a teenager")
    
elif age<65: #elif used to check if age is less than 65 to be printed as adult.
    print("You are an adult")
    
else:        #else used to print output as elder if age greater than 65.
    print("You are an elder")