import random

def main():
    print("Here are six sentences:\n")
    make_sentence(1, "past")     # a. single, past
    make_sentence(1, "present")  # b. single, present
    make_sentence(1, "future")   # c. single, future
    make_sentence(2, "past")     # d. plural, past
    make_sentence(2, "present")  # e. plural, present
    make_sentence(2, "future")   # f. plural, future

def make_sentence(quantity, tense):
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    sentence = f"{determiner.capitalize()} {noun} {verb}."
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
#  chosen word. All the functions that you must 
#  write for this milestone assignment are described 
#  in the Steps section below."""


# import random
# import os   

# def main():
#     print("Hello. I am thinking of a sentence.")    

#     make_sentence()


# def make_sentence():
#     # get determiner
#     det = get_determiner(3)
#     # get noun
#     noun = get_noun(5)
#     # get verb
#     verb = get_verb(5, "past")
#     # get adjective
#     adj = get_adjective(5)                  

#     print(f"{det} {noun} {verb} {adj}.")            

#     # get random number between 1 and 5

# def get_determiner(quantity):
#     """Return a randomly chosen determiner. A determiner is
#     a word like "the", "a", "one", "two", "some", "many".
#     If quantity is 1, this function will return either "a", "one",              
#     or "the". Otherwise this function will return either "some" or "many".
#     """
#     if quantity == 1:
#         words = ["a", "one", "the"]
#     else:
#         words = ["some", "many"]

#     # Randomly choose and return a determiner.
#     word = random.choice(words)

#     return word

# def get_noun(quantity):
#     """Return a randomly chosen noun.
#     """
#     if quantity == 1:
#         word = "bird"
#     else:
#         word = "birds"

#     return word 


# def get_verb(quantity, tense):
#     """Return a randomly chosen verb. If tense is "past", this
#     function will return one of the past tense verbs. Otherwise
#     this function will return one of the present tense verbs.
#     """
#     if tense == "past":
#         if quantity == 1:
#             word = "drank"
#         else:
#             word = "drunk"
#     else:
#         if quantity == 1:
#             word = "drinks"
#         else:
#             word = "drink"

#     return word     


# def get_adjective(quantity):
#     """Return a randomly chosen adjective.
#     """
#     if quantity == 1:
#         word = "happy"
#     else:
#         word = "sad"

#     return word

# def get_preposition():
#     """Return a randomly chosen preposition
#     """
#     word = "on"
#     return word 

# def get_prepositional_phrase(quantity):
#     """Return a randomly chosen prepositional phrase.
#     """
#     if quantity == 1:
#         word = "a"
#     else:
#         word = "some"

#     return word

# def get_prepositional_phrase(quantity):
#     """Return a randomly chosen prepositional phrase.
#     """
#     if quantity == 1:
#         word = "a"
#     else:
#         word = "some"

#     return word     




    main()