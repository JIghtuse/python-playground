# list copying examples

my_foods = ['pizza', 'burger', 'hot dog']
friend_foods = my_foods[:]

my_foods.append('pancakes')
friend_foods.append('ice cream')

print(f"My favorite foods are:\n{my_foods}")
print(f"\nMy friend's favorite foods are:\n{friend_foods}")

print("My favorite foods are:")
for food in my_foods:
    print(food)
print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)
