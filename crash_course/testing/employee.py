class Employee:
    def __init__(self, first_name, last_name, salary):
        """Store a name and annual salary."""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, raise_amount=5000):
        self.salary += raise_amount
