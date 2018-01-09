filename = 'alice.txt'

try:
    with open(filename) as input_file:
        contents = input_file.read()
except FileNotFoundError:
    print(f"Sorry, the file '{filename}' does not exist.")
else:
    # Count the approximate number of words in the file
    words = contents.split()
    print(f"The file '{filename}' has about {len(words)} words.")

