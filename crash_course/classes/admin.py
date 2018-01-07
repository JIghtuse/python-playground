from user import User

class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show(self):
        return ', '.join(self.privileges)

class Admin(User):
    def __init__(self, first_name, last_name, email, privileges):
        super().__init__(first_name, last_name, email, 'admin')
        self.privileges = Privileges(privileges)

    def show_privileges(self):
        print(f"Admin {self.full_name()} privileges: {self.privileges.show()}")
