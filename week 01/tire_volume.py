# from math import pi

# w = float(input("Enter the width of the tire in mm: "))
# a = float(input("Enter the aspect ratio of the tire: "))
# d = float(input("Enter the diameter of the wheel in inches: "))

# v = (pi)*(w)**2*(a(w*a + 2540*d))/10,000,000,000

# print(f"The approximate volume of space inside the tire is {v:.2f} cubic inches.")


import math

def calculate_tire_volume():
    """
    Calculates the approximate volume of space inside a tire.
    """
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

# Call the function
calculate_tire_volume()