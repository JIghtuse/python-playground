def describe_city(city, country='Russia'):
    print(f"{city.title()} is in {country.title()}.")

describe_city('reykjavik', 'iceland')
describe_city('moscow')
describe_city(city='novosibirsk')
describe_city(country='usa', city='new-york')
