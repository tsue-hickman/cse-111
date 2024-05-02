# Work as a team to write a Python program named discount.py
#  that gets a customer’s subtotal as input and gets the current 
# day of the week from your computer’s operating system. Your program
# must not ask the user to enter the day of the week. Instead, it must 
# get the day of the week from your computer’s operating system.

# If the subtotal is $50 or greater and today is Tuesday or Wednesday,
#  your program must subtract 10% from the subtotal. Your program must
# then compute the total amount due by adding sales tax of 6% to the subtotal. 
# Your program must print the discount amount if applicable, the sales tax 
# amount, and the total amount due.

import datetime

# Get the current day of the week (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
day_of_week = datetime.datetime.now().weekday()

# Input the subtotal
subtotal = float(input("Enter the subtotal: "))

# Check if the subtotal is >= 50 and if it's Tuesday (1) or Wednesday (2)
if subtotal >= 50 and (day_of_week == 1 or day_of_week == 2):
    # Calculate the 10% discount
    discount = subtotal * 0.1
    print("Discount amount: $", discount)
else:
    # No discount
    discount = 0

# Calculate the sales tax (6%)
sales_tax = subtotal * 0.06

# Calculate the total
total = subtotal - discount + sales_tax

# Print the sales tax and total
print("Sales tax: $", sales_tax)
print("Total: $", total)
