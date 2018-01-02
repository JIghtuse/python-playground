cities = {
    'london': {
        'country': 'united kingdom',
        'population': 8.788,
        'fact': 'Capital of England',
    },
    'moscow': {
        'country': 'russia',
        'population': 11.92,
        'fact': 'Capital of Russia',
    },
    'novosibirsk': {
        'country': 'russia',
        'population': 1.511,
        'fact': 'Bisected by the Ob river',
    },
}

for city, city_info in cities.items():
    city_name = city.title()
    country = city_info['country'].title()

    print(f"{city_name} is in {country}."
          f" Its population has about {city_info['population']} millions."
          f" {city_info['fact']}.")
