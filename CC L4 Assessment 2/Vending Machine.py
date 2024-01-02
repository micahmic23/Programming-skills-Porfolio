#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 17:52:42 2023

@author: geronimojo

Vending Machine Program
"""
"""A menu is created using a dictionary that displays 
the food and drink items each with their code, name and price."""
jihanki_menu = [
              {"code" : 0,
               "name" : "Burger",
               "price" : 5,},
              
              {"code" : 1,
               "name" : "Fries",
               "price" : 3,},
              
              {"code" : 2,
               "name" : "Sandwich",
               "price" : 4,},
              
              {"code" : 3,
               "name" : "Pizza",
               "price" : 6,},
              
              {"code" : 4,
               "name" : "Fried Chicken",
               "price" : 5,},
              
              {"code" : 5,
               "name" : "Shawarma",
               "price" : 4,},
              
              {"code" : 6,
               "name" : "Rice Balls",
               "price" : 2,},
              
              {"code" : 7,
               "name" : "Sushi",
               "price" : 5,},
              
              {"code" : 8,
               "name" : "Fried Rice",
               "price" : 4,},
              
              {"code" : 9,
               "name" : "Water",
               "price" : 1,},
              
              {"code" : 10,
               "name" : "Coke",
               "price" : 2,},
              
              {"code" : 11,
               "name" : "Sprite",
               "price" : 2,},
             
              {"code" : 12,
               "name" : "Iced Tea",
               "price" : 1,}, 
              
              {"code" : 13,
               "name" : "Karak",
               "price" : 1,},
              
              {"code" : 14,
               "name" : "Fruit Juice",
               "price" : 2,},
              
              {"code" : 15,
               "name" : "Coffee",
               "price" : 2,},
              ]


# A list is created for the user's items to be stored here.
jihanki = []

# The variable 'receipt' is used to create the receipt for the user's purchase.
receipt = """
\t\t☆☆こんにちは! Welcome to 'Jihanki' Box!( ͡~ ͜ʖ ͡°)☆☆
-------------------------------------------------------------------
         ☆PRODUCT.......................PRICE☆
        
         """     

# The variable 'runny_nose' stores the 'True' data type to activate the loop and to end it. 
runny_nose = True

# Comments are displayed to introduce the vending machine.
print("------------こんにちは! Welcome to 'Jihanki' Box!(♡´౪`♡)-------------\n\n")
print("--------------------'Jihanki' Box Menu ♥◟(´౪`)◞♥--------------------\n\n")

# for loop used to display the food and drink items all at once.
for x in jihanki_menu:
    print(f"Item: {x['name']} --- Price: {x['price']} --- Code: {x['code']}")
    


print("        ")

print("--------------------------------------------------------------------")  

print("        ")  

# define function 'sum_item' used to calculate the sum of the total items bought by the user(jihanki) through for loop.
def sum_item(jihanki):
    sum_item = 0
    
    for x in jihanki:
        sum_item+= x["price"]
        
    return sum_item

# define function 'foodbox' used to input the user's items which is later then added to the 'jihanki' list.
def foodbox(jihanki_menu, runny_nose, jihanki):
    while runny_nose:
        item_bought = int(input("Enter your desired item code to acquire:"))
        
# if, elif and else conditions allows messages to be displayed each time a user inputs an item to their list.
        if item_bought == 0:
            print("Tasty Burger comin' right up!૮ ˶ᵔ ᵕ ᵔ˶ ა\n")
            jihanki.append(jihanki_menu[item_bought])
        
        elif item_bought == 1:
            print("Crispy Fries comin' right up!૮ ˶ᵔ ᵕ ᵔ˶ ა\n")
            jihanki.append(jihanki_menu[item_bought])
        
        elif item_bought == 2:
            print("Scrumptious Sandwich comin' right up!૮ ˶ᵔ ᵕ ᵔ˶ ა\n")
            jihanki.append(jihanki_menu[item_bought])
            
        elif item_bought == 3:
            print("Pipin' Hot Pizza comin' right up!૮ ˶ᵔ ᵕ ᵔ˶ ა\n")
            jihanki.append(jihanki_menu[item_bought])
        
        elif item_bought == 4:
            print("Juicy Fried Chicken comin' right up!૮ ˶ᵔ ᵕ ᵔ˶ ა\n")
            jihanki.append(jihanki_menu[item_bought])
            
        elif item_bought == 5:
            print("Smokin' Hot Shawarma comin' right up!૮ ˶ᵔ ᵕ ᵔ˶ ა\n")
            jihanki.append(jihanki_menu[item_bought])
            
        elif item_bought == 6:
            print("Fresh Hot Rice balls comin' right up!૮ ˶ᵔ ᵕ ᵔ˶ ა\n")
            jihanki.append(jihanki_menu[item_bought])
            
        elif item_bought == 7:
            print("Mouth-watering Sushi comin' right up!૮ ˶ᵔ ᵕ ᵔ˶ ა\n")
            jihanki.append(jihanki_menu[item_bought])
            
        elif item_bought == 8:
            print("Savory Fried Rice comin' right up!૮ ˶ᵔ ᵕ ᵔ˶ ა\n")
            jihanki.append(jihanki_menu[item_bought])
            
        elif item_bought == 9:
            print("Water comin' right up!૮ ˶ᵔ ᵕ ᵔ˶ ა\n")
            jihanki.append(jihanki_menu[item_bought])
            
        elif item_bought == 10:
            print("Coke comin' right up!૮ ˶ᵔ ᵕ ᵔ˶ ა\n")
            jihanki.append(jihanki_menu[item_bought])
            
        elif item_bought == 11:
            print("Sprite comin' right up!૮ ˶ᵔ ᵕ ᵔ˶ ა\n")
            jihanki.append(jihanki_menu[item_bought])
            
        elif item_bought == 12:
            print("Iced Tea comin' right up!૮ ˶ᵔ ᵕ ᵔ˶ ა\n")
            jihanki.append(jihanki_menu[item_bought])
            
        elif item_bought == 13:
            print("Karak comin' right up!૮ ˶ᵔ ᵕ ᵔ˶ ა\n")
            jihanki.append(jihanki_menu[item_bought])
            
        elif item_bought == 14:
            print("Fruit Juice comin' right up!૮ ˶ᵔ ᵕ ᵔ˶ ა\n")
            jihanki.append(jihanki_menu[item_bought])
            
        elif item_bought == 15:
            print("Coffee comin' right up!૮ ˶ᵔ ᵕ ᵔ˶ ა\n")
            jihanki.append(jihanki_menu[item_bought])
            
        else:
            print("Sorry, Invalid code! Try Again! >_<\n")
            
# 'add_items' lets the user either add more items or to finish.           
        add_items = input("Press any key to add more items and press e to exit:")
        if add_items == "e":
            
# 'runny_nose' holds the value 'False' to end the loop here.
            runny_nose = False

# 'bill_choice' lets the user choose to either print the receipt or the total sum.            
    bill_choice = int(input("Press 1 to print the receipt or Press 2 to only print the total sum:"))
    if bill_choice == 1:
        print(make_receipt(jihanki, receipt))
    elif bill_choice == 2:
        print("Your total amount to pay is AED", sum_item(jihanki))
    else:
        print("INVALID ENTRY! >_<")
    

# define function 'make_receipt' creates a digital receipt of the items bought and the total sum.           
def make_receipt(jihanki, receipt):
    
    for x in jihanki:
        receipt += f"""
        \t☆{x["name"]}.......................AED {x['price']}☆
        """
        
    receipt += f"""
       \t☆Total.......................AED {sum_item(jihanki)}☆
       
       \n"""
       
    import datetime
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))               
       
    return receipt  

# define function 'foodbox' is returned for the program to function.
foodbox(jihanki_menu, runny_nose, jihanki)

# 'total' stores the total sum of items bought from the variable 'jihanki'.
total = sum_item(jihanki)

# This stores the amount of money the user will place.
total_payment = 0

# Gives messages to inform the user regarding purchase.
print("\nPlease place money to obtain items.\n")
print("5, 10, 20, and 50 bills are considered! AED 5 minimum!")
print("All coins are allowed.\n")

# 'payment' stores the money received into 'total_payment'.
payment = float(input("Please place money here ฅ^•ﻌ•^ฅ:"))
total_payment += payment

# while loop allows the user to pay again if the amount placed is less by subtracting the total sum to the amount given.
while total_payment < total:
    print("Your payment isn't enough! AED", total-total_payment ,"is remaining.")
    payment = float(input("\nPlease place balance here ฅ^•ﻌ•^ฅ:"))
    total_payment += payment
    
# if condition is used when the amount placed is equal or more than the total displayed. The loop is then stopped after.
    if total_payment >= total:
        print("Wonderful!\ (•◡•) / You have placed an amount of AED", total_payment,".\n")
        break
# when the balance amount given is less is sends a message to insert a new amount.    
    else:
        print("\nInserted amount is not accepted. Try again ┐(´-｀)┌\n")
        print("\nPlease place money to obtain items.\n")
        print("5, 10, 20, and 50 bills are considered! AED 5 minimum!")
        print("All coins are allowed.\n")
        
        payment = float(input("Please place money here ฅ^•ﻌ•^ฅ:"))
        total_payment += payment
        
# another while loop is added for instances when the balance is still less.          
        while total_payment < total:
            print("Your payment isn't enough! AED", total - total_payment ,"is remaining.")
            payment = float(input("Please place balance here ฅ^•ﻌ•^ฅ:"))
            total_payment += payment

# the change is calculated by subtracting the payment with the total sum.        
loose_change = total_payment - total

# if the amount given is exact or if the change is equal to 0 a message is sent for no change.
if loose_change <= 0:
    print("Great! You have zero change!(๑✪ᆺ✪๑)\n")
    print("ありがとう ございます! Thank you for purchasing at 'Jihanki' Box! 🫶")
    
# another condition is met when there is remaining change. The change is then displayed.
else:
    print("You have a change of AED", loose_change,".\n")
    print("ありがとう ございます! Thank you for purchasing at 'Jihanki' Box! 🫶")
    
    



           

              
            
              
              
              
