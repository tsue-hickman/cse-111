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
    valid_answers = ["extrovert", "introvert", "sensing", "intuition", "thinking", "feeling", "judging", "perceiving"]
    answer = input(question + " ").lower()
    while answer not in valid_answers:
        answer = input("Invalid response. Please enter a valid trait: ").lower()
    return answer

def update_personality_scores(scores, answer):
    opposites = {
        "extrovert": "introvert", "introvert": "extrovert",
        "sensing": "intuition", "intuition": "sensing",
        "thinking": "feeling", "feeling": "thinking",
        "judging": "perceiving", "perceiving": "judging"
    }
    scores[answer] += 1
    scores[opposites[answer]] -= 1

def get_personality_type(scores):
    personality = ""
    personality += "E" if scores["extrovert"] >= scores["introvert"] else "I"
    personality += "S" if scores["sensing"] >= scores["intuition"] else "N"
    personality += "T" if scores["thinking"] >= scores["feeling"] else "F"
    personality += "J" if scores["judging"] >= scores["perceiving"] else "P"
    return personality

def get_type_mapping():
    return {
        "ISTJ": {"house": "Hufflepuff", "element": "Earth", "animal": "Beaver"},
        "ISTP": {"house": "Ravenclaw", "element": "Air", "animal": "Wolf"},
        "ISFJ": {"house": "Hufflepuff", "element": "Earth", "animal": "Retriever"},
        "ISFP": {"house": "Gryffindor", "element": "Fire", "animal": "Dolphin"},
        "INTJ": {"house": "Ravenclaw", "element": "Air", "animal": "Owl"},
        "INTP": {"house": "Ravenclaw", "element": "Air", "animal": "Chameleon"},
        "INFJ": {"house": "Gryffindor", "element": "Water", "animal": "Dolphin"},
        "INFP": {"house": "Hufflepuff", "element": "Water", "animal": "Deer"},
        "ESTJ": {"house": "Slytherin", "element": "Earth", "animal": "Lion"},
        "ESTP": {"house": "Gryffindor", "element": "Fire", "animal": "Cheetah"},
        "ESFJ": {"house": "Hufflepuff", "element": "Earth", "animal": "Labrador"},
        "ESFP": {"house": "Gryffindor", "element": "Fire", "animal": "Otter"},
        "ENTJ": {"house": "Slytherin", "element": "Air", "animal": "Eagle"},
        "ENTP": {"house": "Ravenclaw", "element": "Air", "animal": "Monkey"},
        "ENFJ": {"house": "Gryffindor", "element": "Water", "animal": "Horse"},
        "ENFP": {"house": "Gryffindor", "element": "Fire", "animal": "Butterfly"}
    }

def get_type_attributes(personality_type, type_mapping):
    return type_mapping.get(personality_type, {"house": "Unknown", "element": "Unknown", "animal": "Unknown"})

def initialize_personality_scores():
    return {
        "extrovert": 0, "introvert": 0,
        "sensing": 0, "intuition": 0,
        "thinking": 0, "feeling": 0,
        "judging": 0, "perceiving": 0
    }

def get_questions():
    return questions  


def run_personality_test():
    print("Welcome to the personality test!")
    scores = personality_scores.copy()
    questions = get_questions()
    selected_questions = random.sample(list(questions), 20)

    for question in selected_questions:
        answer = get_answer(question)
        update_personality_scores(scores, answer)

    personality_type = get_personality_type(scores)
    type_mapping = get_type_mapping()
    type_attributes = get_type_attributes(personality_type, type_mapping)

    print(f"\nYour personality type is: {personality_type}")
    print(f"Harry Potter House: {type_attributes['house']}")
    print(f"Element: {type_attributes['element']}")
    print(f"Animal: {type_attributes['animal']}")

def main():
    run_personality_test()

if __name__ == "__main__":
    main()