story = {
    'start': ('You wake up in a dark room.', ['Go left', 'Go right'], 'left_room', 'right_room'),
    'left_room': ('You enter a room with a chest.', ['Open chest', 'Leave room'], 'open_chest', 'start'),
    # Add more scenes here...
}


def display_scene(scene):
    description, choices, next_scene1, next_scene2 = story[scene]
    print(description)
    print('\nWhat would you like to do?')
    for choice in choices:
        print(choice)

def get_user_choice():
    choice = input('> ')
    return choice.lower()


def play_game():
    current_scene = 'start'
    while current_scene:
        display_scene(current_scene)
        choice = get_user_choice()
        description, choices, next_scene1, next_scene2 = story[current_scene]
        if choice == choices[0].lower():
            current_scene = next_scene1
        elif choice == choices[1].lower():
            current_scene = next_scene2
        else:
            print('Invalid choice. Try again.')

if __name__ == '__main__':
    play_game()