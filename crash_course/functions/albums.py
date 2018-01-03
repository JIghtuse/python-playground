QUIT_VALUE = 'q'

def make_album(artist, title, number_of_tracks=0):
    album = {'artist': artist, 'title': title}
    if number_of_tracks:
        album['number_of_tracks'] = number_of_tracks
    return album

def read_album():
    print("\nPlease tell me your name.")
    print(f"(enter '{QUIT_VALUE}' at any time to quit)")

    artist = input("Artist: ")
    if artist == QUIT_VALUE:
        return ''

    title = input("Title: ")
    if title == QUIT_VALUE:
        return ''

    return make_album(artist, title)

albums = [
    make_album('nautilus pompilius', 'razluka'),
    make_album('muse', 'black holes and revelations'),
    make_album('muse', 'absolution'),
    make_album('beatles', "a hard day's night", 13),
]

while True:
    album = read_album()
    if not album:
        break

    albums.append(album)

for album in albums:
    print(album)