from datetime import datetime
import csv

PRODUCT_ID_INDEX = 0     # "Product #" in both CSV files
PRODUCT_NAME_INDEX = 1   # "Name" in products.csv
PRODUCT_PRICE_INDEX = 2  # "Price" in products.csv
QUANTITY_INDEX = 1       # "Quantity" in request.csv


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip the header row
        for row in reader:
            key = row[key_column_index]
            dictionary[key] = row
    return dictionary

def main():
    try:
        products_dict = read_dictionary("products.csv", 0)
        
        print("Inkom Emporium\n")
        
        total_items = 0
        subtotal = 0
        
        with open("request.csv", "rt") as request_file:
            reader = csv.reader(request_file)
            next(reader)  # Skip the header row
            for row in reader:
                product_number = row[0]
                quantity = int(row[1]) 
                
                if product_number not in products_dict:
                    raise KeyError(f"Error: unknown product ID in the request.csv file '{product_number}'")
                
                product = products_dict[product_number]
                name = product[1]
                price = float(product[2])
                
                print(f"{name}: {quantity} @ {price}")
                
                total_items += quantity
                subtotal += price * quantity
        
        sales_tax = subtotal * 0.06
        total = subtotal + sales_tax
        
        print(f"\nNumber of Items: {total_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {total:.2f}")
        
        print("\nThank you for shopping at the Inkom Emporium.")
        print(datetime.now().strftime("%a %b %d %H:%M:%S %Y"))
        
    except FileNotFoundError as e:
        print(f"Error: missing file\n{e}")
    except KeyError as e:
        print(e)

if __name__ == "__main__":
    main()