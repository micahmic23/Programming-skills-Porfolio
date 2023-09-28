
"""
Exercise 5: Change Guest List ☑️
You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.

•Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.

•Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.

•Print a second set of invitation messages, one for each person who is still in your list.
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

msg = f"\nSorry {invites[1].title()} can't make it to dinner." #The second invite is given a message of declining the invite and printed as output.
print(msg)

#Jeremiah can't make it to dinner
del(invites[1])
invites.insert(1, 'Chelsea') #The second invite 'Jeremiah' is replaced with a new invite 'chelsea' with the function 'insert'.

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