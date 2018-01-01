pizzas = ['pepperoni', 'italia', 'hawaii']
friend_pizzas = pizzas[:]

pizzas.append('cheesy chicken')
friend_pizzas.append('beefy beef')

for pizza in pizzas:
    print(f"I like {pizza} pizza")
print("I really love pizza!")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
