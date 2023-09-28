
"""
Exercise 7: Seeing the World ☑️
Think of at least five places in the world you’d like to visit. • Store the locations in a list. Make sure the list is not in alphabetical order.

• Print your list in its original order. Don’t worry about printing the list neatly,just print it as a raw Python list.

• Use sorted() to print your list in alphabetical order without modifying the actual list.

• Show that your list is still in its original order by printing it.

• Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.

• Show that your list is still in its original order by printing it again.

• Use reverse() to change the order of your list. Print the list to show that its order has changed.

• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.

• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.

• Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.
"""

#The variable 'locations' stores a list of places to go to and prints the list in different orders.
locations = ['Paris','Tokyo','Seoul','Sydney','London']

print("Original order:") #Printed in its original order
print(locations)

print("\nAlphabetical order:") #Printed in alphabetical order using 'sorted()'
print(sorted(locations))

print("\nOriginal order:")
print(locations)

print("\nReverse Alphabetical order:") #Printed in reversed alphabetical order using 'sorted('',reverse=True'))
print(sorted(locations, reverse=True))
      
print("\nOriginal order:")
print(locations)

print("\nReversed order:") #Printed in reversed order using 'reversed()'
locations.reverse()
print(locations)

print("\nOriginal order:") #Printed in original again using 'reverse()'
locations.reverse()
print(locations)

print("\nAlphabetical order:") #Printed in alphabetical order using 'sort()'
locations.sort()
print(locations)

print("\nReversed Alphabetical order:") #Printed in reversed alphabetical order using 'sort(reverse=True)'
locations.sort(reverse=True)
print(locations)
