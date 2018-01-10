from name_function import get_formatted_name

QUIT_VALUE = 'q'

print(f"Enter '{QUIT_VALUE}' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == QUIT_VALUE:
        break

    last = input("Please give me a last name: ")
    if last == QUIT_VALUE:
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")
