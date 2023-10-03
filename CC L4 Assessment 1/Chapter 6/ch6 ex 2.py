#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 19:50:58 2023

@author: geronimojo

Exercise 2: Movie Tickets: ☑️
A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if

they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their

age, and then tell them the cost of their movie ticket

"""
#The variable 'prompt' is assigned to the following statements.
prompt = "How old are you?"
prompt += "\nEnter 'quit' when finished."

#while loop is used to repeatedly print the statements until the user ends the loop with 'quit'.
while True:
    age = input(prompt)
    if age =='quit':
        break
    age = int(age)

#The the nested if statements check whether the age falls into the given conditions to see the ticket amount.
    if age<3:
       print("The ticket is free.")
    elif age>=3 and age<=12:
        print("The ticket is $10.")
    else:
        print("The ticket is $15.")
        
        
        