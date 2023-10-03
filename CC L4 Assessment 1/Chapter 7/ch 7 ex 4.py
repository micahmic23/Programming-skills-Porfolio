#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 21:15:54 2023

@author: geronimojo

Exercise 4: Large Shirts ☑️
Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a

medium shirt with the default message, and a shirt of any size with a different message.

"""

#'make_shirt' function assigns a t-shirt's size and message to be made. 
def make_shirt(size='large', message='I love Python'):
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')

#The function is called three times to set as three different t-shirts.
make_shirt()
make_shirt(size='medium')
make_shirt(message="I love Javascript.", size='small')