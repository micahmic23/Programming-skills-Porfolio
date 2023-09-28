#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 15:32:41 2023

@author: geronimojo

Chapter 4 Exercise 5: Favorite Fruit ☑️
Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.

•Make a list of your three favorite fruits and call it favorite_fruits.

•Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block

should print a statement,such as You really like bananas!
"""

favorite_fruits=['Orange','Grape','Melon'] #A list of fruits are assigned to 'favorite_fruits'.

if 'Banana' in favorite_fruits: #if statements are used to check if the given fruits are inside the list to print the given statement as output.
    print("You really like banana")
if 'Grape' in favorite_fruits:
    print("You really like grape")
if 'Orange' in favorite_fruits:
    print("You really like orange")
if 'cherry' in favorite_fruits:
    print("You really like cherry")
if 'Melon' in favorite_fruits:
    print("You really like melon")

