import csv

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    """
    # Create an empty dictionary
    dictionary = {}

    # Open the CSV file for reading
    with open(filename, "r") as csv_file:
        csv_reader = csv.reader(csv_file)

        # Skip the first line (header)
        next(csv_reader)

        # Read the remaining rows
        for line in csv_reader:
            # Use the column specified by key_column_index as the key
            key = line[key_column_index]

            # Store the remaining columns as the value
            value = [column.strip() for column in line[:key_column_index] + line[key_column_index + 1:]]

            # Add the key-value pair to the dictionary
            dictionary[key] = value

    return dictionary

def main():
    # Read the dictionary from the CSV file
    students_dict = read_dictionary("students.csv", 0)

    # Get the I-Number from the user
    i_number = input("Please enter an I-Number (xxxxxxxxx): ")

    # Remove dashes from the I-Number (Stretch Challenge 1)
    i_number = i_number.replace("-", "")

    # Validate the I-Number (Stretch Challenge 2)
    if len(i_number) != 9:
        print(f"Invalid I-Number: {'too few' if len(i_number) < 9 else 'too many'} digits")
    elif not i_number.isdigit():
        print("Invalid I-Number")
    # Check if the I-Number exists in the dictionary
    elif i_number in students_dict:
        # Print the corresponding name
        name = " ".join(students_dict[i_number])
        print(name)
    else:
        print("No such student")

if __name__ == "__main__":
    main()