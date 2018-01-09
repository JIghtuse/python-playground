import json

filename = 'favorite_number.json'

try:
    with open(filename) as input_file:
        number = json.load(input_file)
except FileNotFoundError:
    number = input("Please enter your favorite number: ")
    number = int(number)

    with open(filename, 'w') as output_file:
        json.dump(number, output_file)
else:
    print(f"I know your favorite number! It's {number}.")
