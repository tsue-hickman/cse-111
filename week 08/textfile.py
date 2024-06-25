import csv

with open('test.csv', 'r') as file:
    csv_data = csv.reader(file)
    
    for line in file:
        print(line)