
"""
Exercise 6: Shrinking Guest List 
You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.

•Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner.

•Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.

•Print a message to each of the two people still on your list, letting them know they’re still invited.

•Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.    
"""

invites = ['Jesus','Jeremiah','Shek','Esther','Eunice']

msg = f"{invites[0].title()} is invited to dinner."
print(msg)

msg = f"{invites[1].title()} is invited to dinner."
print(msg)

msg = f"{invites[2].title()} is invited to dinner."
print(msg)

msg = f"{invites[3].title()} is invited to dinner."
print(msg)

msg = f"{invites[4].title()} is invited to dinner."
print(msg)

msg = f"\nSorry {invites[1].title()} can't make it to dinner."
print(msg)

#Jeremiah can't make it to dinner
del(invites[1])
invites.insert(1, 'Chelsea')

#Print new list of invites
msg = f"\n{invites[0].title()} is invited to dinner."
print(msg)

msg = f"{invites[1].title()} is invited to dinner."
print(msg)

msg = f"{invites[2].title()} is invited to dinner."
print(msg)

msg = f"{invites[3].title()} is invited to dinner."
print(msg)

msg = f"{invites[4].title()} is invited to dinner."
print(msg)


#Oh no, the new table won't arrive. A message is printed.
print("\nSorry, We can only invite two people to dinner.") 

msg = invites.pop() #Three invites are removed using the function pop(). Each of the three are given a message of cancellation.
print(f"Sorry, {msg.title()} there is no room at the table.")

msg = invites.pop()
print(f"Sorry, {msg.title()} there is no room at the table.")

msg = invites.pop()
print(f"Sorry, {msg.title()} there is no room at the table.")

#Let's invite the two people left using 'title()'
print(f"\n{invites[0].title()} is invited to dinner.")
print(f"{invites[1].title()} is invited to dinner.")

#Empty the list using 'del'
del(invites[0])
del(invites[0])

#Prove the list is empty
print(invites)
