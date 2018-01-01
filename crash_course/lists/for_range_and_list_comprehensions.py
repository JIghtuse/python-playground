# for loop, range, and list comprehensions examples

for value in range(1, 21):
    print(value)

numbers = list(range(1, 1000001))
for number in numbers:
    print(number)

print(min(numbers))
print(max(numbers))
print(sum(numbers))

odd_numbers = list(range(1, 20, 2))
for number in odd_numbers:
    print(number)

threes = list(range(3, 31, 3))
for number in threes:
    print(number)

cubes = [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
for cube in cubes:
    print(cube)

cubes = [value**3 for value in range(1, 11)]
for cube in cubes:
    print(cube)

print(f"The first three items in the list are: {cubes[:3]}")
print(f"Three items from the middle of the list are: {cubes[2:5]}")
print(f"The last three items in the list are: {cubes[-3:]}")
