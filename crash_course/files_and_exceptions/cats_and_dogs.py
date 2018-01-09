def print_file_contents(filename):
    """Print the approximate number of words in a file."""

    try:
        with open(filename) as input_file:
            contents = input_file.read()
    except FileNotFoundError:
        pass
    else:
        print(contents)


filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    print_file_contents(filename)
