# asks for age of users and reports movie ticket prices for them

QUIT_VALUE = 'quit'

PROMPT = f"""
Please enter age of the next viewer in years.
(Enter '{QUIT_VALUE}' when you are finished.) """

running = True
while running:
    age = input(PROMPT)

    if age == QUIT_VALUE:
        running = False
    else:
        age = int(age)

        print(age)

        if age < 3:
            price = 0
        elif age <= 12:
            price = 10
        else:
            price = 15

        message = f"${price}" if price else "free"
        print(message)
