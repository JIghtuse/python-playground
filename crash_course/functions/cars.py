import car
from car import make_car
from car import make_car as mk
import car as c
from car import *

car = car.make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

car = mk('subaru', 'outback', color='blue', tow_package=True)
print(car)

car = c.make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
