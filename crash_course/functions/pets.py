# function arguments examples

def describe_pet(pet_name, animal_type='cat'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# positional arguments
describe_pet('harry', 'hamster')

# keyword arguments
describe_pet(animal_type='dog', pet_name='willie')
describe_pet(pet_name='marceline', animal_type='cat')

# using default values
describe_pet(pet_name='cheesecake')
describe_pet('pikachu')
