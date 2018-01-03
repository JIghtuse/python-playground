# prompts for a number of people and reports whether their table is ready

number_of_people = input("Please enter how many people are in your dinner group: ")
number_of_people = int(number_of_people)

if number_of_people > 8:
    print("Please wait for a table.")
else:
    print("Your table is ready.")