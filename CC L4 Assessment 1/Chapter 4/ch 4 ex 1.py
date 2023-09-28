#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 12:21:31 2023

@author: geronimojo
Chapter 4 Exercise 1: Alien color1
Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.

•Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.

•Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)

"""
#User input is done using alien_color to store the string 'green'. 

alien_color= 'green'

if alien_color=='green': #An if statement is used with the relational operator '==' to make sure the color given is equal to green.
    print("You just earned 5 points") #alien_color is equal to green that is why the player has earned 5 points as the output.
    
    
#User input is done for alien_color to assign the string 'red'.
alien_color='red'

if alien_color=='green':
    print("You just earned 5 points")

#No output is shown.