"""Exercise 3: Stripping Names 
Tidy up the code to make it easier to understand

Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, “\t” and “\n”, at least once.

Print the name once, so the whitespace around the name is displayed.

Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().
"""

name = "\tJoseph\n" #The variable name stores the name with the functions \t and \n

print('Unmodified:') #The variable 'name' is printed to set 'Joseph' as output
print(name)

print("\nWith lstrip:") #The string 'Joseph' is printed using the function lstrip() for left
print(name.lstrip())

print("\nWith rstrip:") #the string is printed using rstrip() to be displayed on the right
print(name.rstrip())

print("\nWith strip:") #The string is printed using strip() to the left
print(name.strip())