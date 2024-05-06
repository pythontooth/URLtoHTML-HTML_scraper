import sys
import os
import time
from config import products, users, name_dayincome, income_tax, after_tax,         name_transactions, disc0, disc1, pin, pin_enabled, pin_tries, tax_percentage, command_end, clear_command, viewproducts_command

# Made by pythontooth. Check config.py for settings.

# Lastest update: 05/05/2024

# Function to clear the terminal
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

# Pin login
def pin_security():
    global pin
    global pin_enabled
    global pin_tries
    cls()
    # Check if pin is enabled
    while pin_enabled:
        askforPIN = input("Enter your PIN: ")
        if askforPIN == pin:
            pin_enabled = False
            print("PIN correct.")
            time.sleep(1)
            cls()
            return
        elif askforPIN != pin:
            pin_enabled = True
            pin_tries -= 1
            print(f"Incorrect PIN. Please try again. {pin_tries} left!")
            if pin_tries == 3:
                sys.exit()

# Get current date
date = time.strftime("%d/%m/%Y")
print(date)

# User login function
nameofSeller = "N/A"  # Define the global variable outside any function

def login():
    global nameofSeller  # Declare the variable as global
    
    print("Users:")
    for name, number in users.items():
        print(f"{number}: {name}")

    # Prompt user to select a number
    selected_number = input("Select a number: ")

    # Check if the selected number is in the dictionary values
    for name, number in users.items():
        if str(number) == selected_number:
            print(f"You selected {name}.")
            
            nameofSeller = name  # Assign the value to the global variable
            break
    else:
        print("User not found.")


###########################################################


# Function to calculate total income for the day
def calculateIncome(totalEarned):
    global name_dayincome
    global date
    global income_tax
    global after_tax

    
    with open(name_dayincome, 'a') as f:
        f.write(f"""
        |----- {date} -----|
        |Total earned: {totalEarned}$|
        |Tax({tax_percentage}%): {totalEarned * income_tax}$|
        |After tax: {totalEarned * after_tax}$|
        |------------------|
        """)

# Main function to handle product input
def enterProducts():
    # globals
    global products
    global date
    global nameofSeller
    global name_transactions
    global disc0
    global disc1

    
    total = 0
    totalSold = 0
    totalEarned = 0
    x = True
    cls()
    while x:
        time.sleep(1)
        askforProduct = input("Select product: ").lower()
        if str(askforProduct).lower() in products:
            cls()
            time.sleep(0.1)
            askforAmount = int(input(f"Select {askforProduct} amount:"))
            total = total + (products[askforProduct] * int(askforAmount)) * disc0
            totalEarned = totalEarned + (products[askforProduct] *                             int(askforAmount)) * disc0
            totalSold = totalSold + askforAmount
            print("Anything else?")
            y = input("Y/n:")
            if y.lower() == "n":
                # End of customer session
                cls()
                print("Total: " + str(total))
                print(f"""
                Applied {disc1} discount
                """)
                print("Total sold: " + str(totalSold))
                print("Seller: " + nameofSeller)
                input("Press enter to continue...")
                # Write sales data to a txt file
                with open(name_transactions, 'a') as f:
                    f.write("|--------------------|\n")
                    f.write(str(date) + "\n")
                    f.write(f"|Total: {total}$\n")
                    f.write("|Total units sold: " + str(totalSold) + "\n")
                    f.write("|Discount: " + str(disc1) + "\n")
                    f.write("|Seller: " + nameofSeller + "\n")
                    f.write("|--------------------|\n")
                    f.write("\n")
                cls()
                x = True
                total = 0
                totalSold = 0
        elif askforProduct == command_end:
            cls()
            x = False  # End the loop
            calculateIncome(totalEarned)
            print(f"The data has been saved in {name_dayincome}!")
            
        elif askforProduct == viewproducts_command:
            # Print all products and their prices
            for key, value in products.items():
                print(f"{key}: {value}")

        elif askforProduct == clear_command:
            cls()
        else:
            print("Product not found :(")
            continue


# Functions from start to end.
pin_security()
login()
enterProducts()