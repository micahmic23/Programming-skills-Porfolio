#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 14:26:48 2023

@author: geronimojo

Exercise 4: Rivers ☑️
Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.

Use a loop to print a sentence about each river, such as The Nile runs through Egypt.

Use a loop to print the name of each river included in the dictionary.

Use a loop to print the name of each country included in the dictionary.

"""
#The variable 'rivers' uses a dictionary to store river names and its country.
rivers= {'Yangtze':'China','Nile':'Egypt','Fraser':'Canada','Missisipi':'United States','Kuskokwim':'Alaska'}

for river, country in rivers.items(): #for loop is used to automatically print a sentence for each river item.
    print("The", river.title(), "flows through the", country.title() +".")
    
print("\n" +"The following rivers are included in this data set:") 
for river in rivers.keys():   #for loop is used to automatically print each river all at once.
    print("-" , river.title())
    
print("\n" +"The following countries are included in this data set:")
for country in rivers.values(): #for loop is used to automatically print each country all at once.
    print("-" , country.title())