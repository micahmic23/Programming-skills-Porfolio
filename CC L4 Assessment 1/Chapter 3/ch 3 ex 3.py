"""Exercise 3: Your Own List 
Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list

to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”
"""
#The variable 'transpolist' stores a list of vehicles. Each vehicle is given a statement and printed as output.
transpolist = ['car','bus','train']

statement = f"I would like to own a ferrari {transpolist[0].title()}."
print(statement)

statement = f"I would like to ride the rta {transpolist[1].title()}."
print(statement)

statement = f"I would like to own a thomas {transpolist[2].title()}."
print(statement)


