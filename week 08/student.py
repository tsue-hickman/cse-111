import csv
def read_dictionary(filename, key_column_index):
    """
    Reads a CSV file containing student data and returns a dictionary
    with the student ID as the key and the corresponding student name as the value.

    Returns:
        dictionary: A dictionary mapping student IDs to student names.
    """
    # Create an empty dictionary to store the student data
    dictionary = {}


    with open("../week 08/students.csv", "rt")as csv_file:

        reader = csv.reader(csv_file)

        # Skip the header row
        next(reader)

        # Read the data
        for row in reader:
            # Get the student ID and name from the current row
            if len(row) != 0:

                key = row[key_column_index]

                dictionary[key] = row

    # Return the dictionary containing the student data
    return dictionary

def main():

    i_number = input("Please enter your i-number: ")



    students = read_dictionary("students.csv", 0)

    if i_number in students:

        name = students[i_number][1]
        print(f"Hello, {name}!")

    else:

        print("Your i-number is not found in the student database.")

if __name__ == "__main__":
    main()