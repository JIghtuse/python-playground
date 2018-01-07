class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe(self):
        print(f'Restaurant "{self.name.title()}" with {self.cuisine_type} cuisine.')

    def open(self):
        print(f'Restaurant "{self.name.title()}" is open.')

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, number_of_clients):
        self.number_served += number_of_clients


class IceCreamStand(Restaurant):
    def __init__(self, name, flavors):
        super().__init__(name, "ice cream")
        self.flavors = flavors

    def show_flavors(self):
        print(f"{self.name} ice cream stand has following flavors: {' '.join(self.flavors)}")

