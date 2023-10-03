#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 19:41:27 2023

@author: geronimojo

Exercise 1: Pizza Toppings ☑️
Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping,

print a message saying you’ll add that topping to their pizza.

"""
#The variable 'prompt' is assigned to the following statements.
prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

#While loop is used to repeatedly print the statements to input the user's toppings until 'quit' is done and is stopped.
while True: 
    topping = input(prompt)
    if topping != 'quit':
        print("  I'll add " + topping + " to your pizza.")
    else:
        break