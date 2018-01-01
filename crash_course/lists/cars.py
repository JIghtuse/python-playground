cars = ['bmw', 'audi', 'toyota', 'subaru']


# Sorting a list permanently

cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)


# Sorting a list temporaryliy

cars = ['bmw', 'audi', 'toyota', 'subaru']
print()
print(f"Here is the original list:\n{cars}")
print(f"Here is the sorted list:\n{sorted(cars)}")
print(f"Here is the original list again:\n{cars}")


# Reversing a list

cars = ['bmw', 'audi', 'toyota', 'subaru']
print()
print(cars)
cars.reverse()
print(f"Reversed:\n{cars}")


# Finding the Length of a list

print(f"There are {len(cars)} cars: {cars}")
