# prompts for a number and prints whether it is multiple of 10 or not

number = input("Please enter a number: ")
number = int(number)

if number % 10 == 0:
    message = "Your number is a multiple of 10."
else:
    message = "Your number is not a multiple of 10."

print(message)
