def print_number_of_occurences(filename, word):
    """Print number of occurences of word in filename."""

    try:
        with open(filename) as input_file:
            contents = input_file.read()
    except FileNotFoundError:
        print(f"Sorry, the file '{filename}' does not exist.")
    else:
        occurences = contents.lower().count(word)
        print(f"Word '{word}' occured in '{filename}' {occurences} times.")


filenames = ['alice.txt', 'pride_and_prejudice.txt']
for filename in filenames:
    print_number_of_occurences(filename, 'the')
