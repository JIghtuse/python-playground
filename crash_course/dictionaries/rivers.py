rivers_to_countries = {
    'nile': 'egypt',
    'lena': 'russia',
    'volga': 'russia',
}

print("Data in dictionary:")
for river, country in rivers_to_countries.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("Rivers in dictionary:")
for river in rivers_to_countries:
    print(river.title())

print("Countries in dictionary:")
for country in set(rivers_to_countries.values()):
    print(country.title())