def build_person(first_name, last_name, age=0):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musicians = [
    build_person('jimi', 'hendrix', 27),
    build_person('john', 'hooker'),
]

for musician in musicians:
    print(musician)
