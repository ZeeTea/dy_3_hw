# Ask the user four bits of input: Do you want to : Show/Add/Delete or Quit?

amazon_shopping_cart = {}

while True:
    consumer = input("Do you want to Show, Add, Delete or Quit? ").lower()
    if consumer == "show":
        print(amazon_shopping_cart)
    elif consumer == "add":
        item = input("What item would you like to add? ")
        if item in amazon_shopping_cart:
            amazon_shopping_cart[item] += 1
        else:
            amazon_shopping_cart[item] = 1
    elif consumer == "delete":
        item = input("What item would you like to delete? ")
        if item in amazon_shopping_cart:
            amazon_shopping_cart.pop(item)
        else:
            print(f"{item} not found in cart.")
    elif consumer == "quit":
        print("Exiting Shopping Cart.")
        break
    else:
        print("Invalid input. Please try again.")

print("Final shopping cart:")
print(amazon_shopping_cart)

#Create a Module in VS Code and Import It into jupyter notebook
#Module should have the following capabilities:

#1) Has a function to calculate the square footage of a house
#Reminder of Formula: Length X Width == Area

#2) Has a function to calculate the circumference of a circle

#Program in Jupyter Notebook should take in user input and use imported functions to 
# calculate a circle's circumference or a houses square footage

from math_funtctions import square_footage

length = int(input("Enter the length of the house: "))
width = int(input("Enter the width of the house: "))
print("The square footage of the house is: ", square_footage(length, width))