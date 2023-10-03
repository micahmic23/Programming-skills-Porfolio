#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 20:42:26 2023

@author: geronimojo

Exercise 5: No Pastrami ☑️
Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code

near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all

occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

"""
#'sandwich_orders' list assigns various sandwiches while 'finished_sandwiches' list is made empty.
sandwich_orders= ['Grilled cheese', 'Philadelphia','Club sandwich','Veggie','Pastrami']
finished_sandwiches=[]

#Pastrami has run out. While loop is used to remove 'Pastrami' from the list.
print("I'm sorry, we're all out of pastrami today.")
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

#While loop used to repeatedly print each list item as a statement the list items are then added to the empty list 'finished_sandwiches'.
print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

#For loop is then used to print each sandwich in a statement on repeat.
print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")
    

