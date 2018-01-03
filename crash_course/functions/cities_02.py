def city_country(city, country):
    return f"{city.title()}, {country.title()}"

cities = [
    city_country('santiago', 'chilie'),
    city_country('moscow', 'russia'),
    city_country('novosibirsk', 'russia'),
    city_country('new-york', 'usa')
]

for city in cities:
    print(city)

