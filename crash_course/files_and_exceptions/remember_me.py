import json


def get_stored_username(username_storage_filename):
    """Get stored username if available"""
    try:
        with open(username_storage_filename) as input_file:
            username = json.load(input_file)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username(username_storage_filename):
    """Prompt for a new username."""
    username = input("What is your name? ")
    with open(username_storage_filename, 'w') as output_file:
        json.dump(username, output_file)
    return username


def greet_user(username_storage_filename):
    """Greet the user by name."""
    username = get_stored_username(username_storage_filename)

    if username is not None:
        is_correct_username = input(f"Are you {username}? [y/n] ")
        if is_correct_username == 'y':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username(username_storage_filename)
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username(username_storage_filename)
        print(f"We'll remember you when you come back, {username}!")

greet_user(username_storage_filename='username.json')