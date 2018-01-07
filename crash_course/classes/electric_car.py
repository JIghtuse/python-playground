"""A set of classes that can be used to represent electric cars."""

from car import Car

class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, size=70):
        self.size = size

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.size == 70:
            range = 240
        elif self.size == 85:
            range = 270

        print(f"This battery allows to go to approximately {range} miles on a full charge.")

    def describe(self):
        """Print a statement desribing the battery."""
        print(f"{self.size}-kWh battery")

    def upgrade_battery(self):
        if self.size != 85:
            self.size = 85


class ElectricCar(Car):
    """Represents aspects of a car specific to electric vehicles."""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")
