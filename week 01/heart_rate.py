# get the hearrate from the user, ask the user their age, calculate their maximum heart rate, and displays results for the user to see
"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

name = input("What is your name? ")
age = int(input("How old are you? "))
max_rate = 220 - age


rate = 0.65 * max_rate
print("Your max heart rate is ", max_rate,"bpm.")
print("Your heart rate should be between", rate, "and", rate * 0.85, "bpm.")

