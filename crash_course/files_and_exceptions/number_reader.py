import json

filename = 'numbers.json'
with open(filename) as input_file:
    numbers = json.load(input_file)

print(numbers)