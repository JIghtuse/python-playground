QUIT_VALUE = 'quit'

PROMPT = f"""
Please enter your name.
(Enter '{QUIT_VALUE}' when you are finished.)
> """

while True:
    name = input(PROMPT)

    if name == QUIT_VALUE:
        break

    print(f"Hello, {name}!")

    with open('guest_book.txt', 'a') as output_file:
        output_file.write(name)
        output_file.write('\n')
