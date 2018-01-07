from restaurant import Restaurant, IceCreamStand

restaurant = Restaurant('KFC', 'chicken')
print(restaurant.name)
print(restaurant.cuisine_type)
restaurant.describe()
restaurant.open()

restaurants = [
    restaurant,
    Restaurant('Pizza Hut', 'italian'),
    Restaurant('Mr. Salmon', 'asian'),
]

for restaurant in restaurants:
    restaurant.describe()

print(f"Restaurant has served {restaurants[0].number_served} customers.")
restaurants[0].number_served = 42
print(f"Restaurant has served {restaurants[0].number_served} customers.")
restaurants[0].set_number_served(101)
print(f"Restaurant has served {restaurants[0].number_served} customers.")
restaurants[0].increment_number_served(898)
print(f"Restaurant has served {restaurants[0].number_served} customers.")

ice_cream_stand = IceCreamStand("Ice Bear", ['chocolate', 'plom-bear'])
ice_cream_stand.show_flavors()
