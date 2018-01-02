person = {
    'first_name': 'John',
    'last_name': 'Reese',
    'age': 40,
    'city': 'New-York',
}

people = [
    person,
    {
        'first_name': 'Harold',
        'last_name': 'Finch',
        'age': 42,
        'city': 'New-York',
    },
    {
        'first_name': 'Harry',
        'last_name': 'Potter',
        'age': 11,
        'city': 'London',
    },
]

print(f"Person: {person['first_name'].title()} {person['last_name'].title()}"
      f", {person['age']}, {person['city']}.")

for person in people:
    print(f"Person: {person['first_name'].title()} {person['last_name'].title()}"
          f", {person['age']}, {person['city']}.")
