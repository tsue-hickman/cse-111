def get_response(prompt):

    """ Get the user's response to a prompt.
    
    Args : 
        prompt (str): The prompt to display to the user.
        
    Returns
        str: The user's response (D, d, a, or A)."""
    
    response = input(prompt)

    while response.upper() not in ["D", "A"]:
        response = input("Invalid response. Please enter D, d, a, or A:")
    return response.upper()

print("""This program is an implementation of the Rosenburg""")

"""Self-Esteem Scale. This program will show you ten
statements that you could possibly apply to yourself.
Please rate how much you agree with each of the
statements by responding with one of these four letters:

D means you strongly disagree with the statement.
d means you disagree with the statement.
a means you agree with the statement.
A means you strongly agree with the statement.
"""

statements = [
    "I feel that I am a person of worth, at least on an equal plane with others.",
    "I feel that I have a number of good qualities.",
    "All in all, I am inclined to feel that I am a failure.",
    "I am able to do things as well as most other people.",
    "I feel I do not have much to be proud of.",
    "I take a positive attitude toward myself.",
    "On the whole, I am satisfied with myself.",
    "I wish I could have more respect for myself.",
    "I certainly feel useless at times.",
    "At times I think I am no good at all."
]

def score_positive(response):
    """Score a positive statement based on the user's response.
    
    Args:
        response (str): The user's response (D, d, a, or A).
        
    Returns:
        int: The score for the positive statement. """
    
    if response == "D":
        return 0 
    elif response == "d":
        return 1
    elif response == "a":
        return 2 
    else: 
        return 3 
    
def score_negative(response):
    """Score a negative statement based on the user's response. 
    
    Args:
        response (str): The user's response (D, d, a, or A).
        
    Returns:
        int: The score for the negative statement. """
    
    if response == "D":
        return 3 
    elif response == "d":
        return 2 
    elif response == "a":
        return 1 
    else:
        return 0 
    
    score = 0 
    for i, statement in enumerate (statement, start=1):
        print(f"{i}. {statement}")
        response = get_response("  Enter D, d, a, or A:")
        if i in [3, 5, 8, 9, 10]:
            score += score_negative(response)
        else: 
            score += score_positive(response)

    print(f"\nYour score is {score}.")
    if score < 15:
        print("A score below 15 may indicate problematic low self-esteem.")

    