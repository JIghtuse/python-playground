QUIT_VALUE = 'q'

print("Give me two numbers, and I'll add them.")
print(f"Enter '{QUIT_VALUE}' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == QUIT_VALUE:
        break

    second_number = input("\nFirst number: ")
    if second_number == QUIT_VALUE:
        break

    try:
        answer = int(first_number) + int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    except ValueError:
        print("Please enter two numbers.")
    else:
        print(answer)
