#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 09:58:07 2023

@author: geronimojo

Exercise 2: Glossary ☑️
A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store
their meanings as values.

Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print
the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between

each word-meaning pair in your output.    

"""
#The variable 'glossary' uses a dictionary to assign terms and its definitions.
glossary={'Operator':'Symbols used to perform operations on values and variables.',
          'Data types':'The categorization of data items.',
          'User Input':'The function that inputs data from the user and stores it in a variable.',
          'Conditional Statement':'An essential programming concept that allows the user to control the code output based on the decisions made.',
          'Variable':'A container for storing data values.',
          }

word='Operator' #The variable 'word' assigns the string 'Operator'.
print("\n"+ word.title() ,":" , glossary[word]) #The term and its meaning is printed.

word='Data types' #The variable 'word' assigns the string 'Data types'.
print("\n"+ word.title() ,":", glossary[word]) #The term and its meaning is printed.

word='User Input' #The variable 'word' assigns the string 'User Input'.
print("\n"+ word.title(), ":", glossary[word]) #The term and its meaning is printed.

word='Conditional Statement' #The variable 'word' assigns the string 'Conditional Statement'.
print("\n"+ word.title(), ":", glossary[word]) #The term and its meaning is printed.

word='Variable' #The variable 'word' assigns the string 'Variable'.
print("\n"+ word.title(), ":", glossary[word]) #The term and its meaning is printed.

