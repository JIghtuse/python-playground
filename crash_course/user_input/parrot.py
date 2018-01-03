# user input example program

QUIT_VALUE = 'quit'

PROMPT = f"""Tell me something, and I will repeat it back to you.
Enter '{QUIT_VALUE}' to end the program. """

active = True
while active:
    message = input(PROMPT)

    if message == QUIT_VALUE:
        active = False
    else:
        print(message)