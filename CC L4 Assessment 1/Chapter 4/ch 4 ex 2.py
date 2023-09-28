#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 09:16:06 2023

@author: geronimojo
Chapter 4 Exercise 2: Alien Colors #2 ☑️
Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.

•If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.

•If the alien’s color isn’t green, print a statement that the player just earned 10 points.

•Write one version of this program that runs the if block and another that runs the else block.

"""

#the variable alien_color is assigned to the string 'green'.
alien_color='green'

if alien_color=='green': #if statement is used to make sure alien_color is equal to 'green'.
    print("You just earned 5 points") #If its equal to green 5 points are given.
else:
    print("You just earned 10 points") #else statement is used when alien_color is another color that gives 10 points as output.