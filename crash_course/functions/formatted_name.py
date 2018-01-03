# return values and function optional arguments example

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musicians = [
    get_formatted_name('jimi', 'hendrix'),
    get_formatted_name('john', 'hooker', 'lee'),
]

for musician in musicians:
    print(musician)
