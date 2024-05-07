def main():
    """Get an odometer value in U.S. miles from the user."""
    odometer_value = float(input("Enter an odometer value in miles: "))

    """Get another odometer value in U.S. miles from the user."""
    end_odometer_value = float(input("Enter another odometer value in miles: "))

    """Get a fuel amount in U.S. gallons from the user."""
    fuel_amount = float(input("Enter a fuel amount in U.S gallons: "))

    """Call the miles_per_gallon function and store the result in a variable named mpg."""
    mpg = miles_per_gallon(odometer_value, end_odometer_value, fuel_amount)

    """Call the lp100k_from_mpg function to convert the miles per gallon to liters per 100 kilometers and store the result in a variable named lp100k."""
    lp100k = lp100k_from_mpg(mpg)

    """Display the results for the user to see."""
    print(f"Miles per gallon: {mpg:.2f}")
    print(f"Liters per 100 kilometers: {lp100k:.2f}")

def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles that a vehicle traveled per gallon of fuel.
    Parameter start_miles: The initial odometer value in miles.
    Parameter end_miles: The final odometer value in miles.
    Parameter amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """
    distance = end_miles - start_miles
    mpg = distance / amount_gallons
    return mpg

def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100 kilometers and return the converted value.
    Parameter mpg: A value in miles per gallon.
    Return: The converted value in liters per 100 kilometers.
    """
    lp100km = 235.215 / mpg
    return lp100km

# Call the main function to start the program
main()