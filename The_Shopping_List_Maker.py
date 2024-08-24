# Objective: The aim of this assignment is to create a program that helps users make a shopping list.
# Note: The goal of this is to be a program. The recommendation is to use a while loop that will allow the user to continue to add, remove, 
# and print off their shopping list until they decide to "quit", also known as breaking the loop.
# Task 1: Write a function that lets the user add items to a list.
items = []

def add_item():
    item = input("What would you like to add to your shopping list?")
    return items.append(item)

# Task 2: Include a function to remove items from the list.

def remove_item():
    item = input("What item would you like to remove from your shopping list?")
    return items.remove(item)
    
# Task 3: Add a function that prints out the entire list in a formatted way.

def list_complete():
    print(f"Your shopping list includes: {items}")

while True:
    add_remove = input("Would you like to add or remove an item from your shopping list, yes or quit?")
    if add_remove == "yes":
        user_input = input("What would you like to do, add or remove?")
        if user_input == "add":
            add_item()
        elif user_input == "remove":
            remove_item()
    elif add_remove == "quit":
        list_complete()

