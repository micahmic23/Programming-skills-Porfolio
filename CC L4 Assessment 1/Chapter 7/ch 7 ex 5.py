#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 21:20:32 2023

@author: geronimojo

Exercise 5: Cities
Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence,

such as Reykjavik is in Iceland. Give the parameter for the country a default value.

Call your function for three different cities, at least one of which is not in the default country.

"""
#'describe_city' function assigns a city and a country including the default 'Korea'. A statement is printed to be displayed.
def describe_city(city, country='Korea'):
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

#'describe_city' function is called three times to display different cities.
describe_city('Seoul')
describe_city('Osaka', 'Japan')
describe_city('Itaewon')