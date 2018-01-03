# break (exiting loop) example

QUIT_VALUE = 'quit'

PROMPT = f"""
Please enter the name of a city you have visited.
(Enter '{QUIT_VALUE}' when you are finished.) """

while True:
    city = input(PROMPT)

    if city == QUIT_VALUE:
        break
    else:
        print(f"I'd love to go to {city.title()}!")
