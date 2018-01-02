crookshanks = {
    'kind': 'cat',
    'owner': 'hermione',
}

scabbers = {
    'kind': 'rat',
    'owner': 'ron',
}

pigwidgeon = {
    'kind': 'owl',
    'owner': 'harry',
}

pets = [ crookshanks, scabbers, pigwidgeon ]

for pet in pets:
    print(f"{pet['owner'].title()} has a {pet['kind']}.")