class User:
    def __init__(self, first_name, last_name, email, role):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.role = role
        self.login_attempts = 0

    def full_name(self):
        return f'{self.first_name.title()} {self.last_name.title()}'

    def describe(self):
        print(f'User {self.full_name()}; email: {self.email}; role: {self.role}')

    def greet(self):
        print(f'Welcome, {self.first_name.title()}!')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

