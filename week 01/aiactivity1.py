# Data Types
# Python has several built-in data types

# Numbers
x = 5       # Integer
y = 3.14    # Float
z = 3 + 4j  # Complex

# Strings
name = "John Doe"  # String
multiline_str = """This is
a multiline
string."""

# Boolean
boolean_true = True
boolean_false = False

# Sequence Types
# Lists
my_list = [1, 2, 3, 4, 5]  # List of integers
mixed_list = [1, "two", 3.0, True]  # List with mixed data types

# Tuples (immutable lists)
my_tuple = (1, 2, 3, 4, 5)

# Ranges
my_range = range(10)  # Range from 0 to 9

# Mapping Type
# Dictionaries (key-value pairs)
my_dict = {"name": "John Doe", "age": 30, "city": "New York"}

# Variables
# Variables are used to store data
x = 5  # Integer
y = "Hello"  # String
print(x)  # Output: 5
print(y)  # Output: Hello

# Expressions
# Expressions are combinations of values, variables, operators, and calls to functions
x = 5 + 3  # Addition
y = 10 - 2  # Subtraction
z = 4 * 2  # Multiplication
a = 8 / 2  # Division
b = 5 // 2  # Integer division (returns integer part of the quotient)
c = 5 % 2  # Modulus (returns remainder of division)
d = 2 ** 3  # Exponentiation

# Conditionals
# Conditionals are used to control the flow of execution based on certain conditions
x = 10
if x > 5:
    print("x is greater than 5")  # This will be printed
elif x < 5:
    print("x is less than 5")
else:
    print("x is equal to 5")

# Loops
# Loops are used to iterate over sequences (like lists or strings)

# For loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # This will print each fruit on a new line

# While loop
count = 0
while count < 5:
    print(count)  # This will print 0, 1, 2, 3, 4
    count += 1

# Lists
# Lists are ordered, mutable collections of items
my_list = [1, 2, 3, 4, 5]
print(my_list[0])  # Output: 1 (indexing starts at 0)
print(my_list[-1])  # Output: 5 (negative indexing means counting from the end)
my_list.append(6)  # Adds 6 to the end of the list
my_list.remove(2)  # Removes the first occurrence of 2 from the list

# Dictionaries
# Dictionaries are unordered collections of key-value pairs
my_dict = {"name": "John Doe", "age": 30, "city": "New York"}
print(my_dict["name"])  # Output: John Doe
my_dict["age"] = 31  # Updates the value associated with the "age" key
del my_dict["city"]  # Removes the key-value pair with the key "city"

# Input/Output
name = input("Enter your name: ")  # Prompts the user for input
print("Hello, " + name)  # Outputs a string with the user's input

# Reading/Writing to a File
# Open a file for writing
file = open("example.txt", "w")  # "w" mode for writing, creates a new file
file.write("This is some text.")
file.close()

# Open a file for reading
file = open("example.txt", "r")  # "r" mode for reading
content = file.read()
print(content)
file.close()