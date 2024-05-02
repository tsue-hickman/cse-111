"""
You are required to comment your code according to the following guidelines. At
the top of your files include a comment that contains your name:

# Author: [Your Name]

If your assignment requires a demonstration video use a multiline comment instead:

'''
Author: [Your Name]
Demonstration: [Url]
'''

Note that I used triple single quotes because I am writing this inside a
multiline comment already and I cant reuse the same quotes.

Brother Keers

---

This file provides examples of how to comment functions in Python.
Commenting functions is important for documenting their purpose,
parameters, return values, and any other relevant information. Proper
comments make your code more readable and easier to maintain.

Claude AI
"""

# Example 1: Simple function with a one-line comment
def greet(name):
    """Print a greeting with the given name."""
    print(f"Hello, {name}!")


# Example 2: Function with multi-line comments
def calculate_area(length, width):
    """
    Calculate and return the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    area = length * width
    return area

# Example 3: Function with comments explaining complex logic
def is_palindrome(string):
    """
    Check if a given string is a palindrome.

    A palindrome is a string that reads the same backward as forward.

    Args:
        string (str): The string to be checked.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Remove whitespace and convert to lowercase
    string = string.replace(" ", "").lower()

    # Reverse the string
    reversed_string = string[::-1]

    # Check if the original and reversed strings are equal
    return string == reversed_string


# Example usage of the functions
print("Example 1:")
greet("Alice")  # Output: Hello, Alice!

print("\nExample 2:")
area = calculate_area(5.0, 3.0)
# Output: The area of the rectangle is: 15.0
print(f"The area of the rectangle is: {area}")

print("\nExample 3:")
is_palindrome_result = is_palindrome("A man a plan a canal Panama")
print(is_palindrome_result)  # Output: True

is_palindrome_result = is_palindrome("Hello World")
print(is_palindrome_result)  # Output: False
