# fitness.py

import datetime

def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input("Enter your gender: ")
    birth_str = input("Enter your birthdate in this format: YYYY-MM-DD: ")
    weight_lb = float(input("Enter your weight in U.S. pounds: "))
    height_in = float(input("Enter your height in U.S. inches: "))

    # Convert weight and height to metric units.
    weight_kg = kg_from_lb(weight_lb)
    height_cm = cm_from_in(height_in)

    # Compute age, BMI, and BMR.
    age = compute_age(birth_str)
    bmi = body_mass_index(weight_kg, height_cm)
    bmr = basal_metabolic_rate(gender, weight_kg, height_cm, age)

    # Print the results for the user to see.
    print(f"Your age is {age} years, weight is {weight_kg:.2f} kg, height is {height_cm:.2f} cm, BMI is {bmi:.2f}, and BMR is {bmr:.2f} kcals/day.")

def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    birthdate = datetime.datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.datetime.now()
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or (birthdate.month == today.month and birthdate.day > today.day):
        years -= 1

    return years

def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    return pounds * 0.45359237

def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    return inches * 2.54

def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters:
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    return weight / ((height / 100) ** 2)

def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters:
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    if gender.lower() == "male":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    return bmr

# Call the main function to start the program.
if __name__ == "__main__":
    main()
