"""Exercise 5: USB Shopper 
A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each.

Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.

You will to use the arithmetic operators to complete this exercise.
"""

girl_money = 50 #the variables 'girl_money' and 'Usb_price' assign the integers 50 and 6 from the problem given above
Usb_price = 6

noof_usbsticks_bought = int(girl_money/Usb_price) #The given variable assigns the two variables divided with the arithmetic operator /
print("The girl can buy", (noof_usbsticks_bought),"USB sticks.") #The variable is printed to reveal the no. of usb sticks bought

girls_balance = int(girl_money-noof_usbsticks_bought*Usb_price) #The variable assigns the above variables to multiply the second variable to the third and then subtracted with the first variable with * and -.
print("The girl has £",(girls_balance) , "left.") #The calculated value is then printed using the variable girls_balance.