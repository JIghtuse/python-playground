# asks for pizza toppings user wants and confirms they will be added

QUIT_VALUE = 'quit'

PROMPT = f"""
Please enter pizza toppings you want.
(Enter '{QUIT_VALUE}' when you are finished.) """

running = True
while running:
    topping = input(PROMPT)

    if topping == QUIT_VALUE:
        running = False
    else:
        print(f"We'll add {topping} to your pizza.")
