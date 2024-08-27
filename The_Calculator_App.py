# Objective: The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.
# Task 1: Create functions for each arithmetic operation.
# Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.
# Task 3: Ensure your code can handle division by zero and other potential errors. So if you divide by 0, there is error handling 
# set up to prevent an error from showing in the console.

def add_numbers(a, b):
    return (int(a) + int(b))

def subtract_numbers(a, b):
    return (int(a) - int(b))

def multiply_numbers(a, b):
    return (int(a) * int(b))

def divide_numbers(a, b):
    try:
        return (int(a) / int(b))
    except ZeroDivisionError:
        print("You cannot divide by zero, please try again.")
    
while True:
    math = input("What type of calculation would you like to perform? You can choose from Addition, Subtraction, Multiplication, or Division: ").lower()
    if math == "addition":
        a = input("What is the first number you want to add?")
        b = input("What is the number you want to add to the first number?")
        result = add_numbers(a, b)
        print(result)
    elif math == "subtraction":
        a = input("What is the first number you want to subtract?")
        b = input("What is the number you want to subtract from the first number?")
        result = subtract_numbers(a, b)
        print(result)
    elif math == "multiplication":
        a = input("What is the first number you want to multiply?")
        b = input("What is the number you want to multiply the first number by?")
        result = multiply_numbers(a, b)
        print(result)
    elif math == "division":
        a = input("What is the first number you want to divide?")
        b = input("What is the number you want to divide the first number by?")
        result = divide_numbers(a, b)
        print(result)
    else:
        print("I'm sorry, I don't understand. Please start from the beginning.")
    
    continue_input = input("Would you like to perform another calulation? (yes/no): ").lower()
    if continue_input != "yes":
        break