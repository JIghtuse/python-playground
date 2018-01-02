favorite_numbers = {
    'jen': 42,
    'sarah': 7,
    'edward': 23,
    'phil': 19,
    'john': 7,
}

print(f"Jen's favorite number is {favorite_numbers['jen']}.")
print(f"Sarah's favorite number is {favorite_numbers['sarah']}.")
print(f"Edward's favorite number is {favorite_numbers['edward']}.")
print(f"Phil's favorite number is {favorite_numbers['phil']}.")
print(f"John's favorite number is {favorite_numbers['john']}.")

favorite_numbers = {
    'jen': [3, 42],
    'sarah': [11, 7],
    'edward': [23],
    'phil': [19, 39, 115],
    'john': [7, 12, 2, 4],
}

for person, numbers in favorite_numbers.items():
    print(f"{person.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")
