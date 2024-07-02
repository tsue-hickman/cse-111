import random

personality_scores = {
    "extrovert": 0,
    "introvert": 0,
    "sensing": 0,
    "intuition": 0,
    "thinking": 0,
    "feeling": 0
}
 
questions = {
    "You prefer to spend time alone rather than in a group. (introvert/extrovert)",
    "You tend to think more about the present than the future. (sensing/intuition)",
    "You often make decisions based on logic rather than emotions. (thinking/feeling)",
    "You prefer to have a plan and follow it rather than being spontaneous. (judging/perceiving)",
    "You enjoy meeting new people and socializing. (extrovert/introvert)",
    "You have a vivid imagination and often think about hypothetical scenarios. (intuition/sensing)",
    "You value harmony and try to avoid conflicts. (feeling/thinking)",
    "You prefer to keep your options open and go with the flow. (perceiving/judging)",
    "You feel energized after spending time with a group of people. (extrovert/introvert)",
    "You tend to focus on the details and facts rather than the big picture. (sensing/intuition)",
    "You are more likely to make decisions based on your personal values. (feeling/thinking)",
    "You prefer to have a structured routine and dislike last-minute changes. (judging/perceiving)",
    "You enjoy being the center of attention in social situations. (extrovert/introvert)",
    "You often look for deeper meanings and connections in things. (intuition/sensing)",
    "You tend to be objective and analytical when making decisions. (thinking/feeling)",
    "You prefer to keep things open-ended and flexible. (perceiving/judging)",
    "You feel drained after prolonged social interactions. (introvert/extrovert)",
    "You tend to rely more on your intuition and hunches. (intuition/sensing)",
    "You value honesty and directness, even if it hurts someone's feelings. (thinking/feeling)",
    "You prefer to have a general plan but are open to spontaneity. (judging/perceiving)",
    "You enjoy socializing and meeting new people. (extrovert/introvert)",
    "You are more interested in theories and abstract ideas than practical applications. (intuition/sensing)",
    "You tend to make decisions based on logic and objective analysis. (thinking/feeling)",
    "You prefer to have a clear schedule and stick to it. (judging/perceiving)",
    "You feel recharged after spending time alone. (introvert/extrovert)",
    "You tend to focus on the big picture rather than the details. (intuition/sensing)",
    "You value empathy and try to consider others' feelings. (feeling/thinking)",
    "You prefer to go with the flow and be spontaneous. (perceiving/judging)",
    "You feel energized by being around others. (extrovert/introvert)",
    "You enjoy exploring new ideas and possibilities. (intuition/sensing)",
    "You tend to be blunt and straightforward in your communication. (thinking/feeling)",
    "You prefer to have a plan but are open to changing it if necessary. (judging/perceiving)",
    "You feel drained by large social gatherings. (introvert/extrovert)",
    "You tend to trust your instincts and impressions. (intuition/sensing)",
    "You value fairness and justice above personal feelings. (thinking/feeling)",
    "You prefer to have a clear schedule and stick to it. (judging/perceiving)",
    "You enjoy being the life of the party. (extrovert/introvert)",
    "You tend to focus on the practical and concrete rather than the abstract. (sensing/intuition)",
    "You value logic and objectivity over personal considerations. (thinking/feeling)",
    "You prefer to keep things open-ended and flexible. (perceiving/judging)",
    "You prefer a quieter, more reserved environment. (introvert/extrovert)",
    "You tend to see patterns and connections that others miss. (intuition/sensing)",
    "You value empathy and try to consider others' feelings. (feeling/thinking)",
    "You prefer to have a plan and follow it rather than being spontaneous. (judging/perceiving)",
    "You enjoy being the center of attention in social situations. (extrovert/introvert)",
    "You tend to focus on the details and facts rather than the big picture. (sensing/intuition)",
    "You value honesty and directness, even if it hurts someone's feelings. (thinking/feeling)",
    "You prefer to keep your options open and go with the flow. (perceiving/judging)",
    "You feel energized after spending time alone. (introvert/extrovert)",
    "You tend to trust your instincts and impressions. (intuition/sensing)",
    "You tend to make decisions based on logic and objective analysis. (thinking/feeling)",
    "You prefer to have a structured routine and dislike last-minute changes. (judging/perceiving)",
    "You enjoy meeting new people and socializing. (extrovert/introvert)",
    "You are more interested in theories and abstract ideas than practical applications. (intuition/sensing)",
    "You value empathy and try to consider others' feelings. (feeling/thinking)",
    "You prefer to have a general plan but are open to spontaneity. (judging/perceiving)",
    "You prefer to spend time alone rather than in a group. (introvert/extrovert)",
    "You tend to focus on the big picture rather than the details. (intuition/sensing)",
    "You value fairness and justice above personal feelings. (thinking/feeling)",
    "You prefer to keep things open-ended and flexible. (perceiving/judging)",
    "You feel energized by being around others. (extrovert/introvert)",
    "You enjoy exploring new ideas and possibilities. (intuition/sensing)",
    "You tend to be blunt and straightforward in your communication. (thinking/feeling)",
    "You prefer to have a clear schedule and stick to it. (judging/perceiving)",
    "You feel drained after prolonged social interactions. (introvert/extrovert)",
    "You tend to rely more on your intuition and hunches. (intuition/sensing)",
    "You value logic and objectivity over personal considerations. (thinking/feeling)",
    "You prefer to have a plan but are open to changing it if necessary. (judging/perceiving)",
    "You enjoy being the life of the party. (extrovert/introvert)",
    "You tend to see patterns and connections that others miss. (intuition/sensing)",
    "You value honesty and directness, even if it hurts someone's feelings. (thinking/feeling)",
    "You prefer to keep your options open and go with the flow. (perceiving/judging)",
    "You prefer a quieter, more reserved environment. (introvert/extrovert)",
    "You tend to focus on the practical and concrete rather than the abstract. (sensing/intuition)",
    "You value empathy and try to consider others' feelings. (feeling/thinking)",
    "You prefer to have a structured routine and dislike last-minute changes. (judging/perceiving)",
    "You enjoy socializing and meeting new people. (extrovert/introvert)",
    "You are more interested in theories and abstract ideas than practical applications. (intuition/sensing)",
    "You tend to make decisions based on logic and objective analysis. (thinking/feeling)",
    "You prefer to have a general plan but are open to spontaneity. (judging/perceiving)",
    "You feel energized after spending time alone. (introvert/extrovert)",
    "You tend to trust your instincts and impressions. (intuition/sensing)",
    "You value fairness and justice above personal feelings. (thinking/feeling)",
    "You prefer to keep things open-ended and flexible. (perceiving/judging)",
    "You enjoy being the center of attention in social situations. (extrovert/introvert)",
    "You tend to focus on the details and facts rather than the big picture. (sensing/intuition)",
    "You value logic and objectivity over personal considerations. (thinking/feeling)",
    "You prefer to have a clear schedule and stick to it. (judging/perceiving)",
    "You feel drained by large social gatherings. (introvert/extrovert)",
    "You tend to see patterns and connections that others miss. (intuition/sensing)",
    "You value empathy and try to consider others' feelings. (feeling/thinking)",
    "You prefer to have a plan but are open to changing it if necessary. (judging/perceiving)",
    "You prefer to spend time alone rather than in a group. (introvert/extrovert)",
    "You tend to focus on the practical and concrete rather than the abstract. (sensing/intuition)",
    "You tend to be blunt and straightforward in your communication. (thinking/feeling)",
    "You prefer to keep your options open and go with the flow. (perceiving/judging)",
    "You enjoy meeting new people and socializing. (extrovert/introvert)",
    "You are more interested in theories and abstract ideas than practical applications. (intuition/sensing)",
    "You value honesty and directness, even if it hurts someone's feelings. (thinking/feeling)",
    "You prefer to have a structured routine and dislike last-minute changes. (judging/perceiving)",
     }


def get_answer(question):
    answer = input(question + " ").upper()
    while answer not in ["extrovert", "introvert", "sensing", "intuition", "thinking", "feeling"]:
        answer = input("Invalid response. Please enter extrovert, introvert, sensing, intuition, thinking, or feeling: ").upper()
    return answer

def update_personality_scores(answer):
    if answer == "extrovert":
        personality_scores["extrovert"] += 1
        personality_scores["introvert"] -= 1
    elif answer == "introvert":
        personality_scores["introvert"] += 1
        personality_scores["extrovert"] -= 1
    elif answer == "sensing":
        personality_scores["sensing"] += 1
        personality_scores["intuition"] -= 1
    elif answer == "intuition":
        personality_scores["intuition"] += 1
        personality_scores["sensing"] -= 1
    elif answer == "thinking":
        personality_scores["thinking"] += 1
        personality_scores["feeling"] -= 1
    elif answer == "feeling":
        personality_scores["feeling"] += 1
        personality_scores["thinking"] -= 1

def get_personality_type():
    personality_type = ""
    personality_type += "Extrovert" if personality_scores["Extrovert"] >= personality_scores["Introvert"] else "Introvert"
    personality_type += "Intuitive" if personality_scores["Intuitive"] >= personality_scores["Sensing"] else "Sensing"
    personality_type += "Feeling" if personality_scores["Feeling"] >= personality_scores["Thinking"] else "Thinking"
    personality_type += "Judging" if personality_scores["Judging"] >= personality_scores["Perceptive"] else "Perceptive"
    return personality_type

print("Welcome to the personality test!")

for question in questions:
    answer = get_answer(question)
    update_personality_scores(answer)

personality_type = get_personality_type()
print(f"Your personality type is:", {personality_type})



 



# # Dictionary mapping personality types to houses, elements, and animals
# type_mapping = {
#     "ISTJ": {"house": "Hufflepuff", "element": "Earth", "animal": "Beaver"},
#     "ISTP": {"house": "Ravenclaw", "element": "Air", "animal": "Wolf"},
#     # ... add more mappings here ...
# }

# # Function to get the corresponding house, element, and animal
# def get_type_attributes(personality_type):
#     if personality_type in type_mapping:
#         return type_mapping[personality_type]
#     else:
#         return {"house": "Unknown", "element": "Unknown", "animal": "Unknown"}

# # ... (your existing MBTI test code) ...

# # After determining the user's personality type
# personality_type = get_personality_type()
# type_attributes = get_type_attributes(personality_type)

# print(f"Your personality type is: {personality_type}")
# print(f"Harry Potter House: {type_attributes['house']}")
# print(f"Element: {type_attributes['element']}")
# print(f"Animal: {type_attributes['animal']}")


# Sure, here's the `type_mapping` dictionary with all 16 MBTI types mapped to a Harry Potter house, element, and animal:

# ```python
# type_mapping = {
#     "ISTJ": {"house": "Hufflepuff", "element": "Earth", "animal": "Beaver"},
#     "ISTP": {"house": "Ravenclaw", "element": "Air", "animal": "Wolf"},
#     "ISFJ": {"house": "Hufflepuff", "element": "Earth", "animal": "Retriever"},
#     "ISFP": {"house": "Gryffindor", "element": "Fire", "animal": "Dolphin"},
#     "INTJ": {"house": "Ravenclaw", "element": "Air", "animal": "Owl"},
#     "INTP": {"house": "Ravenclaw", "element": "Air", "animal": "Chameleon"},
#     "INFJ": {"house": "Gryffindor", "element": "Water", "animal": "Dolphin"},
#     "INFP": {"house": "Hufflepuff", "element": "Water", "animal": "Deer"},
#     "ESTJ": {"house": "Slytherin", "element": "Earth", "animal": "Lion"},
#     "ESTP": {"house": "Gryffindor", "element": "Fire", "animal": "Cheetah"},
#     "ESFJ": {"house": "Hufflepuff", "element": "Earth", "animal": "Labrador"},
#     "ESFP": {"house": "Gryffindor", "element": "Fire", "animal": "Otter"},
#     "ENTJ": {"house": "Slytherin", "element": "Air", "animal": "Eagle"},
#     "ENTP": {"house": "Ravenclaw", "element": "Air", "animal": "Monkey"},
#     "ENFJ": {"house": "Gryffindor", "element": "Water", "animal": "Horse"},
#     "ENFP": {"house": "Gryffindor", "element": "Fire", "animal": "Butterfly"}
# }
# ```

# # These mappings are based on general personality traits associated with each MBTI type, but you can certainly modify them to better fit your preferences or interpretations.

# # Here's a brief explanation of the choices:

# # - **House**:
# #   - Hufflepuff: Loyal, hardworking, dedicated
# #   - Ravenclaw: Intelligent, analytical, curious
# #   - Gryffindor: Brave, adventurous, passionate
# #   - Slytherin: Ambitious, strategic, resourceful

# # - **Element**:
# #   - Earth: Practical, grounded, stable
# #   - Air: Intellectual, curious, logical
# #   - Fire: Energetic, passionate, adventurous
# #   - Water: Emotional, compassionate, intuitive

# # - **Animal**:
# #   - The animals chosen represent typical characteristics associated with each personality type, such as loyalty, intelligence, bravery, or adaptability.

# # Feel free to adjust these mappings as you see fit for your personality project.





# # Function to get the corresponding house, element, animal, and parent god
# def get_type_attributes(personality_type):
#     if personality_type in type_mapping:
#         return type_mapping[personality_type]
#     else:
#         return {"house": "Unknown", "element": "Unknown", "animal": "Unknown", "parent_god": "Unknown"}

# # ... (your existing MBTI test code) ...

# # After determining the user's personality type
# personality_type = get_personality_type()
# type_attributes = get_type_attributes(personality_type)

# print(f"Your personality type is: {personality_type}")
# print(f"Harry Potter House: {type_attributes['house']}")
# print(f"Element: {type_attributes['element']}")
# print(f"Animal: {type_attributes['animal']}")
# print(f"Parent God (if a demigod): {type_attributes['parent_god']}")