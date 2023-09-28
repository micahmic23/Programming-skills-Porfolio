#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 09:48:03 2023

@author: geronimojo

Chapter 4 Exercise 3: Alien Colors #3 ☑️
Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.

• If the alien is green, print a message that the player earned 5 points.

• If the alien is yellow, print a message that the player earned 10 points.

• If the alien is red, print a message that the player earned 15 points.

• Write three versions of this program, making sure each message is printed for the appropriate color alien.

"""

#the variable alien_color is assigned to the string 'red'.
alien_color='red'

if alien_color=='green': #if statement is used to make sure alien_color is equal to 'green'.
    print("You just earned 5 points") #If its equal to green 5 points are given.
    
elif alien_color=='yellow': #An elif statement is used to check whether alien_color is equal to 'yellow'.
    print("You just earned 10 points") #else statement is used when alien_color is equal to 'yellow' that gives 10 points as output.
    
else:                              #else statement used for other conditions when alien_color is a different color which primts 15 points.
    print("You just earned 15 points")