def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

def make_great(magicians):
    for i, magician in enumerate(magicians):
        magicians[i] = "the Great " + magician
    return magicians

magicians = [
    'merlin',
    'harry potter',
    'albus dumbledore',
]

great_magicians = make_great(magicians[:])
show_magicians(magicians)
show_magicians(great_magicians)
