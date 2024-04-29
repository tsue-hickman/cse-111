import math 

num_items = int(input(f"Enter the number of items: "))
items_per_box = int(input(f"Enter the number of items per box: "))

num_boxes = math.ceil(num_items / items_per_box)

print()
print (f"For {num_items}, items, packing {items_per_box}" f" items in each box, you will need {num_boxes} boxes.") 



# items_manuf = input(f"Enter the number of the manufacturer: ")
# user_packing = input(f"Enter the number of the packing: ") 

# A manufacturing company needs a program that will 
# help its employees pack manufactured items into boxes for shipping.
#  Write a Python program named boxes.py that asks the user for two integers:
# the number of manufactured items
# the number of items that the user will pack per box
# Your program must compute and print the number of boxes 
# necessary to hold the items. This must be a whole number.
# Note that the last box may be packed with fewer items than
#  the other boxes.


