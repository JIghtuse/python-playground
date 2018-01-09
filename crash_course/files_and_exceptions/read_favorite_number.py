import json

filename = 'favorite_number.json'
with open(filename) as input_file:
    number = json.load(input_file)

print(f"I know your favorite number! It's {number}.")
