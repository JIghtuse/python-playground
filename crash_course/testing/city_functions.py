def make_formatted_name(city, country, population=None):
    if population is None:
        return f"{city.title()}, {country.title()}"
    else:
        return f"{city.title()}, {country.title()} - population {population}"
