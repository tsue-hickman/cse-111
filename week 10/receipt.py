from datetime import datetime
import csv

PRODUCT_PRICE_INDEX = 1
PRODUCT_NAME_INDEX = 0

PRODUCT_ID_INDEX = 0
QUALITY_INDEX = 1

def read_product_info(product_file):
    product_dict = {}
    with open(product_file, "rt") as products:
        reader = csv.reader(products)
        next(reader) 
        for row in reader:
            product_dict[row[PRODUCT_NAME_INDEX]] = [row[PRODUCT_NAME_INDEX], float(row[PRODUCT_PRICE_INDEX])]
    
    return product_dict 

def read_request_info(request_file, product_dict):
    request_dict = {}
    with open(request_file, "rt") as requests:
        reader = csv.reader(requests)
        next(reader)
        for row in reader:
            product_id = row[PRODUCT_ID_INDEX]
            if product_id in product_dict:
                product_info = product_dict[product_id]
                quantity = int(row[QUALITY_INDEX])
                request_dict[product_id] = [product_info[0], product_info [1], quantity]
            else:
                raise KeyError(f"Error: unkown product ID in the {request_file} file\'{product_id}'")

    return request_dict

def print_receipt(product_dict, request_dict):
    total_items = 0
    subtotal = 0

    print("Inkom Emporium\n")
    for product_id, product_info in request_dict.items():
        name, price, quantity = product_info
        total = price * quantity
        print(f"{name}: {quantity} @ {price:.2f}")
        subtotal += total
        total_items += quantity

    print(f"\nNumber of Items: {total_items}")
    print(f"Subtotal: {subtotal:.2f}")

    sales_tax = subtotal * 0.06
    print(f"Sales Tax: {sales_tax:.2f}")

    total = subtotal + sales_tax
    print(f"Total: {total:.2f}\n")

    print("Thank you for shopping at the Inkom Emporium.")
    now = datetime.now()
    print(now.strftime("%c"))


    