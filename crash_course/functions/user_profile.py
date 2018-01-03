# passing arbitrary number of keyword arguments example

def build_profile(first_name, last_name, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {
        'first_name': first_name,
        'last_name': last_name,
    }
    profile.update(user_info)
    return profile

user_profiles = [
    build_profile('albert', 'einstein',
                  location='princeton',
                  field='physics'),
    build_profile('john', 'reese',
                  location='new-york',
                  field='security',
                  strength='high')
]

for user_profile in user_profiles:
    print(user_profile)