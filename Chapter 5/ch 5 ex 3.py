#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 14:00:00 2023

@author: geronimojo

Exercise 3: Glossary 2 ☑️
Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()

calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms

to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.

   
"""
#The variable 'glossary' uses a dictionary to store terms and its definition.
glossary={'Operator':'Symbols used to perform operations on values and variables.',
          'Data types':'The categorization of data items.',
          'User Input':'The function that inputs data from the user and stores it in a variable.',
          'Conditional Statement':'An essential programming concept that allows the user to control the code output based on the decisions made.',
          'Variable':'A container for storing data values.',
          'String':'A series of characters.',
          'Float':'A number with a decimal component.',
          'Boolean':'Data of choices, e.g:- True or False.',
          'Integer':'A numerical value.',
          'List':'A collection of values.',
          }

for word, definition in glossary.items(): #For loop is used to automatically print all terms and definitons as output.
    print("\n" + word.title() , ":" , definition)