#!/usr/bin/env python3
marvelchars = {
    "Starlord": {
        "real name": "peter quill",
        "powers": "dance moves",
        "archenemy": "Thanos"
    },
    "Mystique": {
        "real name": "raven darkholme",
        "powers": "shape shifter",
        "archenemy": "Professor X"
    },
    "Hulk": {
        "real name": "bruce banner",
        "powers": "super strength",
        "archenemy": "adrenaline"
    }
}

def get_user_input(prompt):
    return input(prompt).strip().capitalize()

def print_character_info(char_name, char_stat):
    try:
        value = marvelchars[char_name.lower()][char_stat.lower()]
        if char_stat.lower() == "real name":
            value = value.title()  # Capitalize the first letter of each word
        print(f"{char_name}'s {char_stat} is: {value}")
    except KeyError:
        print("Invalid character name or statistic.")

# Allow the user to try again without exiting the script
while True:
    char_name = get_user_input("Which character do you want to know about? (Starlord, Mystique, Hulk) ")
    char_stat = get_user_input("What statistic do you want to know about? (real name, powers, archenemy) ")
    print_character_info(char_name, char_stat)

    try_again = get_user_input("Do you want to try again? (yes/no) ")
    if try_again.lower() != 'yes':
        break

