#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 21:08:34 2023

@author: geronimojo

Exercise 3: T-Shirt ☑️
Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function

should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional

arguments to make a shirt. Call the function a second time using keyword arguments.
"""
#'make_shirt' function assigns a t-shirt's size and message to be made. 
def make_shirt(size, message):
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')

#The function is called to be set as output.
make_shirt('large', 'Save trees!')
make_shirt(message="Eat more meat.", size='medium')