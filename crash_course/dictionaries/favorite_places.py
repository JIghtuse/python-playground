favorite_places = {
    'jen': ['new-york', 'london', 'boston'],
    'sarah': ['rome'],
    'phil': ['moscow', 'paris'],
}

for person, places in favorite_places.items():
    print(f"{person.title()}'s favorite places:")
    for place in places:
        print("\t" + place.title())
