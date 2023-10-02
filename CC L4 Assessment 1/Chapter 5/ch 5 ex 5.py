#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 14:52:59 2023

@author: geronimojo

Exercise 5: Pets ☑️
Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the

owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about

each pet
"""
#An empty list is created to store the pets information.
pets=[]

#Individual dictionary of pets information are made.
pet={'Animal type':'Dog','Name':'Benji','Age':'2','Owner':'Micah'}

pets.append(pet)

pet={'Animal type':'Cat','Name':'Minnie','Age':'1','Owner':'Jeremiah'}

pets.append(pet)

pet={'Animal type':'Bunny','Name':'Clover','Age':'3','Owner':'Sofia'}

pets.append(pet)

#for loop is used to display each list of the pets information.
for pet in pets:
    print("\nHere's what I know about", pet['Name'].title() , ":")
    for key, value in pet.items():
        print("\t" + key +":" , value)

