
"""
Exercise 2: Greetings 
Start with the list you used in Exercise 1, but instead of just

printing each person’s name, print a message to them. The text of each message should be the same, but each message should be

personalized with the person’s name.
"""
#The same list of names are stored then each are given a message through 'msg' to be printed as output.
namelist = ['Shek', 'Jeremiah', 'Esther', 'Eunice']
msg = f"Hello, {namelist[0].title()}!"
print(msg)

msg = f"Hello, {namelist[1].title()}!"
print(msg)

msg = f"Hello, {namelist[2].title()}!"
print(msg)

msg = f"Hello, {namelist[3].title()}!"
print(msg)

