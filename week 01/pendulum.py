import math

"""
This program calculates the time it takes for a pendulum to swing from one end to the other
The time in seconds that a pendulum takes to swing back and
forth once is given by this formula:
             ____
            / h
    t = 2π / ----
          √  9.81

t is the time in seconds,
π is the constant PI, which is the ratio of the circumference
    of a circle divided by its diameter (use math.pi),
h is the length of the pendulum in meters.

Write a program that prompts a user to enter the length of a
pendulum in meters and then computes and prints the time in
seconds that it takes for that pendulum to swing back and forth."""
# this is my pendulum code not as a function 

h = float(input("Enter the height of the pendulum in meters: "))
t = (2*math.pi)*math.sqrt(h/9.81)
print(f"It takes your pendulum for {t:.2f} seconds to swing from one end to the other.")




# this is my pendulum code as a function
def swingofPendulum(): 
    h = float(input("Enter the height of the pendulum in meters: "))
    t = (2*math.pi)*math.sqrt(h/9.81)
    print(f"It takes your pendulum for {t:.2f} seconds to swing from one end to the other.")

swingofPendulum()










