current_users = ['user', 'wheel', 'admin', 'john', 'samantha', 'harold']
new_users = ['jennifer', 'wheel', 'mike', 'user']

for user in new_users:
    if user.lower() in current_users:
        print(f"User {user} already exist. You need to enter a new username.")
    else:
        print(f"Username {user} is available.")
