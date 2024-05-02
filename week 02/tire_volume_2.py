# # from math import pi

# # w = float(input("Enter the width of the tire in mm: "))
# # a = float(input("Enter the aspect ratio of the tire: "))
# # d = float(input("Enter the diameter of the wheel in inches: "))

# # v = (pi)*(w)**2*(a(w*a + 2540*d))/10,000,000,000

# # print(f"The approximate volume of space inside the tire is {v:.2f} cubic inches.")


# import math

# def calculate_tire_volume():
#     """
#     Calculates the approximate volume of space inside a tire.
#     """
#     # Input validation
#     while True:
#         try:
#             width = float(input("Enter the width of the tire in mm: "))
#             aspect_ratio = float(input("Enter the aspect ratio of the tire: "))
#             diameter = float(input("Enter the diameter of the wheel in inches: "))
#             break
#         except ValueError:
#             print("Invalid input. Please enter a number.")

#     # Calculation
#     volume = (math.pi * width ** 2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

#     # Output
#     print(f"The approximate volume of space inside the tire is {volume:.2f} cubic inches.")

# # Call the function
# calculate_tire_volume()


# # Gets the current date from the computer’s operating system.
# # Opens a text file named volumes.txt for appending.
# # Appends to the end of the volumes.txt file one line of text that contains the following five values:
# # current date
# # width of the tire
# # aspect ratio of the tire
# # diameter of the wheel
# # volume of the tire
# import datetime
# import os
# import math
# import time

# # Get the current date
# now = datetime.datetime.now () 

# # Open the volumes.txt file for appending
# with open("volumes.txt", "a") as volumes_file:
#     volumes_file.write(f"{now} {tire_width} {tire_aspect_ratio} {wheel_diameter} {tire_volume}\n")
#     volumes_file.close()

# # Calculate the approximate volume of space inside a tire
# def calculate_tire_volume():
#     """
#     Calculates the approximate volume of space inside a tire.
#     """
#     # Input validation
#     while True:
#         try:
#             width = float(input("Enter the width of the tire in mm: "))
#             aspect_ratio = float(input("Enter the aspect ratio of the tire: "))
#             diameter = float(input("Enter the diameter of the wheel in inches: "))
#             break
#         except ValueError:
#             print("Invalid input. Please enter a number.")

#     # Calculation
#     volume = (math.pi * width ** 2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

#     # Output
#     print(f"The approximate volume of space inside the tire is {volume:.2f} cubic inches.")



# tire_width = float(input("Enter the width of the tire in mm: "))
# tire_aspect_ratio = float(input("Enter the aspect ratio of the tire: "))
# wheel_diameter = float(input("Enter the diameter of the wheel in inches: "))
# tire_volume = (math.pi * tire_width ** 2 * tire_aspect_ratio * (tire_width * tire_aspect_ratio + 2540 * wheel_diameter))

# # Output
# print(f"The approximate volume of space inside the tire is {tire_volume :. 2f} cubic inches.")
#  # Tire prices for four or more tire sizes online.
# # Add a set of if…elif…else statements in your program 
# # that use the tire width, tire aspect ratio, and 
# # wheel diameter that the user enters to find a 
# # price and then print the price.    



import math
import datetime
import os

def calculate_tire_volume():
    """Calculates the approximate volume of space inside a tire."""
    # Input validation
    while True:
        try:
            width = float(input("Enter the width of the tire in mm: "))
            aspect_ratio = float(input("Enter the aspect ratio of the tire: "))
            diameter = float(input("Enter the diameter of the wheel in inches: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Calculation
    volume = (math.pi * width ** 2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

    # Output
    print(f"The approximate volume of space inside the tire is {volume:.2f} cubic inches.")

    # Tire prices for different sizes
    tire_prices = {
        (185, 50, 14): 89.99,
        (205, 60, 15): 99.99,
        (225, 65, 16): 109.99,
        (245, 70, 17): 119.99
    }

    tire_dimensions = (int(width), int(aspect_ratio), int(diameter))
    if tire_dimensions in tire_prices:
        tire_price = tire_prices[tire_dimensions]
        print(f"The price for tires with dimensions {width}/{aspect_ratio}R{diameter} is ${tire_price:.2f}")
    else:
        print("Sorry, we don't have pricing information for those tire dimensions.")

    # Ask if the user wants to buy tires
    buy_tires = input("Do you want to buy tires with these dimensions? (yes/no): ").lower()
    if buy_tires == "yes":
        phone_number = input("Please enter your phone number: ")

        # Get the current date
        now = datetime.datetime.now()

        # Open the volumes.txt file for appending
        with open("volumes.txt", "a") as volumes_file:
            volumes_file.write(f"{now}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}, {phone_number}\n")
    else:
        # Get the current date
        now = datetime.datetime.now()

        # Open the volumes.txt file for appending
        with open("volumes.txt", "a") as volumes_file:
            volumes_file.write(f"{now}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}\n")

# Call the function
calculate_tire_volume()
