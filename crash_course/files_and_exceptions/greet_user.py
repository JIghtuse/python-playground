import json

filename = 'username.json'

with open(filename) as input_file:
    username = json.load(input_file)
    print(f"Welcome back, {username}!")
