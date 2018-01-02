favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print(f"Sarah's favorite language is {favorite_languages['sarah'].title()}.")

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print("People who took the poll:")
for name in favorite_languages:
    print(name.title())


friends = ['phil', 'sarah']

print("People who took the poll with our friends:")

for name in favorite_languages:
    print(name.title())

    if name in friends:
        print(f"  Hi {name.title()}"
              f", I see your favorite language is {favorite_languages[name].title()}!")


if 'erin' not in favorite_languages:
    print("Erin, please take our poll!")


# looping through keys in order

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")


# looping through values

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())


people_to_poll = ['sarah', 'voldemort', 'harry']
for people in people_to_poll:
    if people in favorite_languages:
        print(f"{people.title()}, thanks for response!")
    else:
        print(f"{people.title()}, please take our poll!")