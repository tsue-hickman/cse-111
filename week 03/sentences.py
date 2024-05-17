# """Write a Python program named sentences.py
#  that generates simple English sentences. During 
#  this prove milestone, you will write functions 
#  that generate sentences with three parts:"""

# """a determiner (sometimes known as an article)
# a noun
# a verb
# For example:

# A cat laughed.
# One man eats.
# The woman will think.
# Some girls thought.
# Many dogs run.
# Many men will write.
# For this milestone, your program must include at least these five functions:

# main


# make_sentence
# get_determiner
# get_noun
# get_verb
# You may add other functions if you want.
# The functions get_determiner, get_noun,
# and get_verb, must randomly choose a word 
# from a list of words and return the randomly
#  chosen word. 
import random

def main():
    print("Here are six sentences:\n")
    make_sentence(0, "past")     # a. single, past
    make_sentence(0, "present")  # b. single, present
    make_sentence(0, "future")   # c. single, future
    make_sentence(1, "past")     # d. plural, past
    make_sentence(1, "present")  # e. plural, present
    make_sentence(1, "future")   # f. plural, future


def get_preposition():
    """Return a randomly chosen preposition from list"""
    prepositions = [
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"
    ]
    return random.choice(prepositions)

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three words"""
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    return f"{preposition} {determiner} {noun}"

def get_adjective(quantity): 
    """Return a randomly chosen adjective"""
    if quantity ==1:
        adjectives = ["happy", "cute", "small", "big", "bright"]
    else: 
        adjectives = ["happy", "cute", "small", "big", "bright"]

    return random.choice(adjectives)


def make_sentence(quantity, tense):
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional_phrase = get_prepositional_phrase(quantity)
    sentence = f"{determiner.capitalize()} {adjective} {noun} {verb} {prepositional_phrase}."
    print(sentence)

def get_determiner(quantity):
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    return random.choice(words)

def get_noun(quantity):
    single_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    plural_nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    if quantity == 1:
        return random.choice(single_nouns)
    else:
        return random.choice(plural_nouns)

def get_verb(quantity, tense):
    past_verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    present_singular_verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    present_plural_verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    future_verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    if tense == "past":
        return random.choice(past_verbs)
    elif tense == "present" and quantity == 1:
        return random.choice(present_singular_verbs)
    elif tense == "present" and quantity != 1:
        return random.choice(present_plural_verbs)
    else:
        return random.choice(future_verbs)

if __name__ == "__main__":


