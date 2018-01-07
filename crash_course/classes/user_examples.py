from admin import Admin
from user import User


users = [
    Admin('root', 'root', 'root@localhost', ["can ban user"]),
    User('john', 'reese', 'john@ree.se', 'user'),
    Admin('harold', 'finch', 'harold@fin.ch', ["can add post", "can delete post", "can ban user"]),
]

for user in users:
    user.describe()
    user.greet()

users[0].increment_login_attempts()
users[0].increment_login_attempts()
users[0].increment_login_attempts()
users[0].increment_login_attempts()

print(f"User {users[0].full_name()} number of login attempts: {users[0].login_attempts}")
users[0].reset_login_attempts()
print(f"User {users[0].full_name()} number of login attempts: {users[0].login_attempts}")
users[-1].show_privileges()
