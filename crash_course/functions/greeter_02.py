QUIT_VALUE = 'q'

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name.")
    print(f"(enter '{QUIT_VALUE}' at any time to quit)")

    first_name = input("First name: ")
    if first_name == QUIT_VALUE:
        break

    last_name = input("Last name: ")
    if last_name == QUIT_VALUE:
        break

    print(f"\nHello, {get_formatted_name(first_name, last_name)}!")
