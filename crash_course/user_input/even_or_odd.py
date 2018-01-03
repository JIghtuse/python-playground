number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    characteristic = "even"
else:
    characteristic = "odd"

print(f"\nThe number {number} is {characteristic}.")