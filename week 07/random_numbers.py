import random

def append_random_numbers(numbers_list, quantity=1):
    """
    Appends `quantity` random numbers to the `numbers_list`.
    Each random number is between 0 and 100, and is rounded to one decimal place.

    Args:
        numbers_list (list): The list to which the random numbers will be appended.
        quantity (int, optional): The number of random numbers to append. Defaults to 1.

    Returns:
        None
    """
    for _ in range(quantity):
        random_number = round(random.uniform(0, 100), 1)
        numbers_list.append(random_number)

def append_random_words(words_list, quantity=1):
    """
    Appends `quantity` random words to the `words_list`.

    Args:
        words_list (list): The list to which the random words will be appended.
        quantity (int, optional): The number of random words to append. Defaults to 1.

    Returns:
        None

    This function appends `quantity` random words to the `words_list`. The words are 
    randomly chosen from a predefined list of words. 
    """
    # The list of words from which the random words are chosen
    word_choices = ['join', 'love', 'smile', 'cloud', 'head', 'sun', 'moon', 'star']
    
    # Append `quantity` random words to the `words_list`
    for _ in range(quantity):
        # Choose a random word from `word_choices`
        random_word = random.choice(word_choices)
        # Append the random word to the `words_list`
        words_list.append(random_word)

def main():
    # Original part
    numbers = [16.2, 75.1, 52.3]
    print("numbers", numbers)
    append_random_numbers(numbers)
    print("numbers", numbers)
    append_random_numbers(numbers, 3)
    print("numbers", numbers)
    
    # Stretch challenge part
    words = ['join', 'love', 'smile']
    append_random_words(words, 3)
    print("words", words)

if __name__ == "__main__":
    main()

















# As a team, write a Python program named random_numbers.py that creates a list of numbers, 
# appends more numbers onto the list, and prints the list. 
# The program must have two functions named main and append_random_numbers as follows:

import random
# main
def main():
    numbers = [16.2, 75.1, 52.3]
# Creates a list named numbers like this:
    append_random_numbers(numbers, 1)
# Prints the numbers list
    print(numbers)
# Calls the append_random_numbers function with only one argument to add one number to numbers
    append_random_numbers(numbers, 3)
# Prints the numbers list
    print(numbers)
   
# Calls the append_random_numbers function again with two arguments to add three numbers to numbers
# Prints the numbers list
# append_random_numbers
# Has two parameters: a list named numbers_list and an integer named quantity. \
# The parameter quantity has a default value of 1
# Computes quantity pseudo random numbers by calling the random.uniform function.
# Rounds the quantity pseudo random numbers to one digit after the decimal.
# Appends the quantity pseudo random numbers onto the end of the numbers_list.
# At the bottom of your program, write an if statement that calls the main function. Then run your program and verify that your program works correctly.

# Core Requirements
# Your program includes two functions named main and append_random_numbers. The append_random_numbers function has two parameters named numbers_list and quantity, and quantity has a default value of 1.
# The main function calls append_random_numbers twice, first with one argument and second with two arguments.
# The append_random_numbers function includes a loop that appends quantity random numbers at the end of numbers_list.