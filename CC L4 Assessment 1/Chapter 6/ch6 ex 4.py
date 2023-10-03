#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 20:27:33 2023

@author: geronimojo

Exercise 4: Deli ☑️
Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches.

Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made,

move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.

"""
#'sandwich_orders' list assigns various sandwiches while 'finished_sandwiches' list is made empty.
sandwich_orders= ['Grilled cheese', 'Philadelphia','Club sandwich','Veggie']
finished_sandwiches=[]

#While loop used to repeatedly print each list item as a statement the list items are then added to the empty list 'finished_sandwiches'.
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

#For loop is then used to print each sandwich in a statement on repeat.
print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")

