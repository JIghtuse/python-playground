QUIT_VALUE = 'quit'

PROMPT = f"""
Please enter age of the next viewer in years.
(Enter '{QUIT_VALUE}' when you are finished.) """

age = ""
while age != QUIT_VALUE:
    age = input(PROMPT)

    if age != QUIT_VALUE:
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
