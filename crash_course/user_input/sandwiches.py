sandwich_orders = ['tuna', 'pastrami', 'pastrami', 'cheese', 'grilled', 'pastrami']
finished_sandwiches = []

print("We run out of pastrami, sorry.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("Sandwiches made:")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich} sandwich")